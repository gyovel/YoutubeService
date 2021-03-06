from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
from redis import Redis

CLIENT_SECRETS_FILE = "../../../client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
AUTH_BUILD = ''
redis_connection=None
def get_authenticated_service():
    global AUTH_BUILD
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    if AUTH_BUILD == '':
        credentials = flow.run_console()
        AUTH_BUILD = build(API_SERVICE_NAME, API_VERSION, credentials=credentials,cache_discovery=False)
    return AUTH_BUILD

def get_redis():
    global redis_connection
    if redis_connection==None:
        redis_connection=Redis()
    return redis_connection
