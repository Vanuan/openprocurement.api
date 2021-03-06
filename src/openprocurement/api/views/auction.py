# -*- coding: utf-8 -*-
from cornice.service import Service
from openprocurement.api.models import Award
from openprocurement.api.utils import (
    save_tender,
    apply_patch,
)
from openprocurement.api.validation import (
    validate_tender_auction_data,
)


auction = Service(name='Tender Auction', path='/tenders/{tender_id}/auction', renderer='json')


@auction.get(renderer='json', permission='auction')
def get_auction(request):
    """Get auction info.

    Get tender auction info
    -----------------------

    Example request to get tender auction information:

    .. sourcecode:: http

        GET /tenders/4879d3f8ee2443169b5fbbc9f89fa607/auction HTTP/1.1
        Host: example.com
        Accept: application/json

    This is what one should expect in response:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "dateModified": "2014-10-27T08:06:58.158Z",
                "bids": [
                    {
                        "value": {
                            "amount": 500,
                            "currency": "UAH",
                            "valueAddedTaxIncluded": true
                        }
                    },
                    {
                        "value": {
                            "amount": 485,
                            "currency": "UAH",
                            "valueAddedTaxIncluded": true
                        }
                    }
                ],
                "minimalStep":{
                    "amount": 35,
                    "currency": "UAH"
                },
                "tenderPeriod":{
                    "startDate": "2014-11-04T08:00:00"
                }
            }
        }

    """
    tender = request.validated['tender']
    if tender.status != 'active.auction':
        request.errors.add('body', 'data', 'Can\'t get auction info in current tender status')
        request.errors.status = 403
        return
    return {'data': tender.serialize("auction_view")}


@auction.patch(content_type="application/json", permission='auction', validators=(validate_tender_auction_data), renderer='json')
def patch_auction(request):
    """Set urls for access to auction.
    """
    apply_patch(request, src=request.validated['tender_src'])
    return {'data': request.validated['tender'].serialize("auction_view")}


@auction.post(content_type="application/json", permission='auction', validators=(validate_tender_auction_data), renderer='json')
def post_auction(request):
    """Report auction results.

    Report auction results
    ----------------------

    Example request to report auction results:

    .. sourcecode:: http

        POST /tenders/4879d3f8ee2443169b5fbbc9f89fa607/auction HTTP/1.1
        Host: example.com
        Accept: application/json

        {
            "data": {
                "dateModified": "2014-10-27T08:06:58.158Z",
                "bids": [
                    {
                        "value": {
                            "amount": 400,
                            "currency": "UAH"
                        }
                    },
                    {
                        "value": {
                            "amount": 385,
                            "currency": "UAH"
                        }
                    }
                ]
            }
        }

    This is what one should expect in response:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "dateModified": "2014-10-27T08:06:58.158Z",
                "bids": [
                    {
                        "value": {
                            "amount": 400,
                            "currency": "UAH",
                            "valueAddedTaxIncluded": true
                        }
                    },
                    {
                        "value": {
                            "amount": 385,
                            "currency": "UAH",
                            "valueAddedTaxIncluded": true
                        }
                    }
                ],
                "minimalStep":{
                    "amount": 35,
                    "currency": "UAH"
                },
                "tenderPeriod":{
                    "startDate": "2014-11-04T08:00:00"
                }
            }
        }

    """
    apply_patch(request, save=False, src=request.validated['tender_src'])
    tender = request.validated['tender']
    bids = sorted(tender.bids, key=lambda i: (i.value.amount, i.date))
    bid = bids[0].serialize()
    award_data = {
        'bid_id': bid['id'],
        'status': 'pending',
        'value': bid['value'],
        'suppliers': bid['tenderers'],
    }
    award = Award(award_data)
    tender.awards.append(award)
    save_tender(request)
    return {'data': tender.serialize(tender.status)}
