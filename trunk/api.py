from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext.webapp import template
import datetime, cgi
from import_models import Import
from google.appengine.ext import db
import util

from controllers import api


application = webapp.WSGIApplication(
   [
    ('/api/kinos/', api.KinoList),
    ('/api/kinos/(.*)/', api.KinoDetail),
  #  ('/api/kinos/(.*)/features/', api.KinoDetailFeatures),

    # kinos
#    ('/kinos/add/', kinos.KinoEdit),
 
    # movies
#    ('/movies/add/', movies.AddMovie),

#    ('/movies/get_original_name/', GetIMDBName),


    # development 
    # inserts test data into the datastore. call only once 
#    ('/testdata/', LoadFixture), 
   ], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
  main()
