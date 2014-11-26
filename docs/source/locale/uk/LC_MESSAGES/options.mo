��          t      �         �    ,   �     
  �     &       3  (   �     �     �       >    �  ]  d   
  
   �
  �  �
    X  �   u  (   +     T     l     z                       
              	                       In addition to providing fields and their values in a request, you may also specify options to control how your request is interpreted and how the response is generated.  For GET requests, options are specified as URL parameters prefixed with `opt_`.  For POST or PUT requests, options are specified in the body, inside the top-level options object (a sibling of the data object).  The option specified in the body overrides the `opt_` one from URL parameter. List of extra fields to include in response. Options Provides the response in "pretty" output.  In the case of JSON this means doing proper line breaking and indentation to make it readable.  This will take extra time and increase the response size so it is advisable only to use this during debugging. Returns the output in JSON-P format instead of plain JSON, to allow requests to come from within browsers and work around the "same origin policy." The function named as the value of the `opt_jsonp` parameter will be called with a single argument, a JavaScript object representing the response. These options can be used in combination in a single request, though some of them may conflict in their impact on the response. `?opt_fields=comma,separated,field,list` `?opt_jsonp=myCallback` `?opt_pretty` `options: { pretty: true }` Project-Id-Version: openprocurement.api 0.1
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2014-11-04 09:37+0200
PO-Revision-Date: 2014-11-25 11:01+0300
Last-Translator: 
Language-Team: LANGUAGE <LL@li.org>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Generator: Poedit 1.5.4
 Крім надання полів та їхніх значень у запиті ви можете ще вказати опції для контролю над тим, як буде оброблятись запит і як буде генеруватись відповідь. Для GET запитів, опції вказуються як URL параметри з префіксом `opt_`. Для POST чи PUT запитів опції вказуються в тілі, всередині об’єктів опцій вищого рівня (схожих на обє’кт даних). Опція вказана в тілі перевизначає `opt_` опцію з URL параметра. Список додаткових полів, що міститимуться у відповіді. Опції Надає відповідь у форматі "pretty". У випадку з JSON це означає правильне розбиття рядків і відступи для зручності читання. Це займе додатковий час і збільшить розмір відповіді, тому краще буде використовувати цю опцію тільки під час налагоджування (debugging). Повертає відповідь у форматі JSON-P замість простого JSON, щоб дозволити запитам приходити з браузерів і працювати навколо "однакової політики походження (same origin policy)." Функція названа так само як значення параметра `opt_jsonp` буде викликана з одним аргументом - JavaScript об’єктом, що представляє відповідь. Ці опції можна комбінувати в одному запиті, хоча деякі з них можуть викликати конфлікт у відповіді. `?opt_fields=comma,separated,field,list` `?opt_jsonp=myCallback` `?opt_pretty` `options: { pretty: true }` 