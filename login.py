from oauth2client.client import flow_from_clientsecrets
import httplib2
import json
import requests


# upgrade to credentials based on authorization code
def upgrade_to_credentials(authorization_code):
    oauth_flow = flow_from_clientsecrets('client_secret.json', scope='')
    oauth_flow.redirect_uri = 'postmessage'
    credentials = oauth_flow.step2_exchange(authorization_code)
    return credentials


# get json from access token
def token_info(access_token):
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    return result


# execute if the user is already logged in
def is_already_logged_in(login_session):
    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    return stored_credentials is not None and stored_gplus_id is not None


# execute if the user is logged in as owner
def is_logged_in_as_owner(login_session, item_user_id):
    return (is_already_logged_in(login_session) and
            (item_user_id == login_session.get('id', None)))


# get user info from google oauth
def get_user_info(access_token):
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    return answer.json()


# update session based on google oauth
def update_login_session(login_session, credentials, gplus_id, user_info):
    login_session['credentials'] = credentials
    login_session['gplus_id'] = gplus_id
    login_session['username'] = user_info['name']
    login_session['picture'] = user_info['picture']
    login_session['id'] = 'GOOGLE_ID_' + user_info['id']
