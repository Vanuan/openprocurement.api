# -*- coding: utf-8 -*-
from openprocurement.api.models import Tender, Bid, Award, Document, Question, Complaint, Contract, get_now
from schematics.exceptions import ModelValidationError, ModelConversionError
from openprocurement.api.utils import apply_data_patch


def filter_data(data, blacklist=[], whitelist=None):
    blacklist += ['id', 'doc_id', 'date', 'dateModified', 'url', 'owner_token', 'owner']
    filter_func = lambda i: i in whitelist if whitelist else i not in blacklist
    return dict([(i, j) for i, j in data.items() if filter_func(i)])


def validate_json_data(request):
    try:
        json = request.json_body
    except ValueError, e:
        request.errors.add('body', 'data', e.message)
        request.errors.status = 422
        return
    if not isinstance(json, dict) or 'data' not in json or not isinstance(json.get('data'), dict):
        request.errors.add('body', 'data', "Data not available")
        request.errors.status = 422
        return
    return json['data']


def validate_data(request, model, partial=False):
    data = validate_json_data(request)
    if data is None:
        return
    if partial:
        data = filter_data(data)
    else:
        data = filter_data(data, blacklist=['status'])
    try:
        if partial and isinstance(request.context, model):
            new_patch = apply_data_patch(request.context.serialize(), data)
            m = model(request.context.serialize())
            m.import_data(new_patch)
            m.validate()
            if request.authenticated_userid == 'chronograph':
                data = m.serialize('chronograph')
            elif request.authenticated_userid == 'auction':
                data = m.serialize('auction_{}'.format(request.method.lower()))
            elif model == Tender:
                data = m.serialize('edit')
            else:
                data = m.serialize()
        else:
            model(data).validate(partial=partial)
    except (ModelValidationError, ModelConversionError), e:
        for i in e.message:
            request.errors.add('body', i, e.message[i])
        request.errors.status = 422
        return
    request.validated['data'] = data
    return data


def validate_tender_data(request):
    return validate_data(request, Tender)


def validate_patch_tender_data(request):
    return validate_data(request, Tender, True)


def validate_tender_auction_data(request):
    data = validate_patch_tender_data(request)
    tender = request.context
    if not tender or not isinstance(tender, Tender):
        return
    if data is not None:
        if tender.status != 'active.auction':
            request.errors.add('body', 'data', 'Can\'t report auction results in current tender status')
            request.errors.status = 403
            return
        bids = data.get('bids', [])
        #if not bids:
            #request.errors.add('body', 'data', "Bids data not available")
            #request.errors.status = 422
            #return
        tender_bids_ids = [i.id for i in tender.bids]
        if len(bids) != len(tender.bids):
            request.errors.add('body', 'bids', "Number of auction results did not match the number of tender bids")
            request.errors.status = 422
            return
        #elif not all(['id' in i for i in bids]):
            #request.errors.add('body', 'bids', "Results of auction bids should contains id of bid")
            #request.errors.status = 422
            #return
        elif set([i['id'] for i in bids]) != set(tender_bids_ids):
            request.errors.add('body', 'bids', "Auction bids should be identical to the tender bids")
            request.errors.status = 422
            return
        data['bids'] = [x for (y, x) in sorted(zip([tender_bids_ids.index(i['id']) for i in bids], bids))]
    else:
        data = {}
    if request.method == 'POST':
        now = get_now().isoformat()
        data['auctionPeriod'] = {'endDate': now}
        data['awardPeriod'] = {'startDate': now}
        data['status'] = 'active.qualification'
    request.validated['data'] = data


def validate_bid_data(request):
    return validate_data(request, Bid)


def validate_patch_bid_data(request):
    return validate_data(request, Bid, True)


def validate_award_data(request):
    return validate_data(request, Award)


def validate_patch_award_data(request):
    return validate_data(request, Award, True)


def validate_patch_document_data(request):
    return validate_data(request, Document, True)


def validate_question_data(request):
    return validate_data(request, Question)


def validate_patch_question_data(request):
    return validate_data(request, Question, True)


def validate_complaint_data(request):
    return validate_data(request, Complaint)


def validate_patch_complaint_data(request):
    return validate_data(request, Complaint, True)


def validate_contract_data(request):
    return validate_data(request, Contract)


def validate_patch_contract_data(request):
    return validate_data(request, Contract, True)


def validate_file_upload(request):
    if 'file' not in request.POST:
        request.errors.add('body', 'file', 'Not Found')
        request.errors.status = 404
    else:
        request.validated['file'] = request.POST['file']


def validate_file_update(request):
    if request.content_type == 'multipart/form-data':
        validate_file_upload(request)
