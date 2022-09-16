"""
	Module for defining constant values.
"""
from local_secrets import firebase_config

# Configuration for lib
SESSION_SECRET = '**********'
PARAMETER_LOGGING = True
APP_NAME = '**Sample App**'
ADMIN_DASHBOARD_POST_LOGIN_PAGE = ''

SIDEBAR_TEMPLATE = 'dashboard/operations_sidebar.html'
STAFF_EMAILS = ['nishadmusthafa@gmail.com',
                ]

DATASTORE_PROJECT_ID ='cm-fortress'
GOOGLE_CLOUD_PROJECT = 'cm-fortress'
AUTH_CONFIG ={
  'firebase':{
    'api_key': firebase_config['api_key'],
    'auth_domain': firebase_config['auth_domain'],
    'project_id': firebase_config['project_id'],
    'storage_bucket': firebase_config['storage_bucket'],
    'messaging_sender_id': firebase_config['messaging_sender_id'],
    'app_id': firebase_config['app_id']
  }
}
