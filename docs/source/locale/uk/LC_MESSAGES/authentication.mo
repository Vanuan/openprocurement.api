��          \      �       �   ;   �                  0  *  ;   [  w   �  >    �   N     �             �  >  b   <  �   �                                       API key is username to use with Basic Authenication scheme. API keys Authentication Owner tokens Some of the API requests (especially the ones that are read-only GET requests) do not require any authenication.  The other ones, that modify data into the database, require broker authentication via API key.  Additionally, owner tokens are issued to facilitate multiple actor roles upon object creation. The token is issued when object is created in the database: You can see the `access` with `token` in response.  Its value can be used to modify objects further under "Owner role": Project-Id-Version: openprocurement.api 0.5
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2014-12-16 10:43+0200
PO-Revision-Date: 2014-12-16 12:32+0300
Last-Translator: 
Language-Team: LANGUAGE <LL@li.org>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Generator: Poedit 1.5.4
 Ключ API - це ім’я користувача, що буде використовуватись зі схемою Базової аутентифікації. Ключі API Аутентифікація Токени власника Деякі запити API (особливо GET запити лише для читання) не потребують аутентифікації. Інші, ті, які модифікують дані у базі даних, потребують аутентифікації брокера через ключ API. Додатково видаються токени власника, щоб забезпечити кілька ролей дійових осіб при створенні об’єкта. Токен видається, коли об'єкт створюється в базі даних: У відповіді є  `access` з `token`. Це значення можна використати для модифікації об’єктів у "ролі Власника": 