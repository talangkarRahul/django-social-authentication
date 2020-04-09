import requests
from django.conf import settings

def google(token):
    from google.oauth2 import id_token
    from google.auth.transport import requests as grequests

    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, grequests.Request())

        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')
        return idinfo
    except ValueError:
        # Invalid token
        return False

def facebook(token):
    end_point = f'oauth/access_token?client_id={settings.FACEBOOK_ID}' \
                    f'&client_secret={settings.FACEBOOK_SECRET_KEY}&grant_type=client_credentials'
    facebook_response = requests.get(settings.FACEBOOK_BASE_URL+end_point)
    facebook_client_access_token = facebook_response.json()
    facebook_debug_endpoint = f'debug_token?input_token={token}' \
                                f'&access_token={facebook_client_access_token["access_token"]}'

    check_user = requests.get(settings.FACEBOOK_BASE_URL+facebook_debug_endpoint)
    user_data = check_user.json()
    return user_data['data']['is_valid']

def get_fb_user(token):
    """
    :param token:
    :return: {'first_name', last_name, birthday, gender, email}
    """
    fb_profile_endpoint = f'/v6.0/me/?fields=first_name,last_name,birthday,gender,email&access_token={token}'
    fb_user = requests.get(settings.FACEBOOK_BASE_URL + fb_profile_endpoint)
    return fb_user.json()