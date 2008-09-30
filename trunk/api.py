from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext.webapp import template
import datetime, cgi
#from import_models import Import
from google.appengine.ext import db
import util

from controllers import api

# ULR-Config for the JSON-API 
# Mostly supposed to be used in Ajax-calls. 

application = webapp.WSGIApplication(
   [
    ('/api/kinos/', api.KinoList),
    ('/api/kinos/([a-z]*)/features/', api.KinoDetailFeature),
    ('/api/kinos/(.*)/', api.KinoDetail),

   ], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
