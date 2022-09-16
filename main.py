"""
    The main module to create flask object
    and run the app.
"""
import site
import os
from datetime import datetime

import constants
import gaelib
from gaelib.auth import auth
from gaelib.utils import web
from app.urls import admin_dashboard, sample_entity_api
from gaelib.env import get_staff_phones


# The Flask app object
app = web.startup(parameter_logging=True,
                  client_logging=True)

template_path = os.path.join(gaelib.__path__[0], 'dashboard/templates')
app.jinja_loader.searchpath.append(template_path)

# # App URLs
app.register_blueprint(admin_dashboard)
app.register_blueprint(sample_entity_api)


def login_callback(user):
  # Add logic here to be performed after
  # using the user after login is done. 
  if user.email in constants.STAFF_EMAILS or user.phone in get_staff_phones():
    user.update(role=1)
    user.put()



auth.configure_login_callback(login_callback)


if __name__ == '__main__':
  # This is used when running locally only. When deploying to Google App
  # Engine, a webserver process such as Gunicorn will serve the app. This
  # can be configured by adding an `entrypoint` to app.yaml.
  app.run(host='0.0.0.0', port=8080, debug=True)
