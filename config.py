import json

credentials = None
with open('credentials.json', 'r') as f:
    credentials = json.loads(f.read())

HOST = 'runtime.sagemaker.us-east-1.amazonaws.com'
REGION = 'us-east-1'
# replace the url below with the sagemaker endpoint you are load testing
SAGEMAKER_ENDPOINT_URL = credentials['endpoint']
ACCESS_KEY = credentials['access_key']
SECRET_KEY = credentials['secret_key']
SESSION_KEY = credentials['session_key']
# replace the context type below as per your requirements
CONTENT_TYPE = 'application/json'
METHOD = 'POST'
SERVICE = 'sagemaker'
SIGNED_HEADERS = 'content-type;host;x-amz-date'
CANONICAL_QUERY_STRING = ''
ALGORITHM = 'AWS4-HMAC-SHA256'
