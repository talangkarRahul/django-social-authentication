# django-social-authentication


### To verify google token
call google method it accept the google_id and it return payload.
#### check the following code 
in your login or signup api 
``` python
from social_authentication import authentication
google_payload = auhentication.google(token)
if google_payload['email'] != request.data['email'] and google_payload['aud'] != GOOGLE_APP_ID: # check the email_id and aud in token
    return False
```

### Dependency packages
* google-auth = 1.11.3
* requests = 2.23.0
