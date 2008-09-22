from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext.webapp import template
import datetime, cgi
from models import Movie, Feature, Kino, UserProfile
from google.appengine.ext import db
import util

from controllers import users, kinos, movies, features

def tmpl(name): util.tmpl(name) 

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('KoelnKino')
       
   

class LoadFixture(webapp.RequestHandler): 
    def get(self): 
        import testdata
        

class GetIMDBName(webapp.RequestHandler): 
    def get(self): 
        if self.request.get('q'): 
            name = util.get_imdb_name(self.request.get('q'))
            self.response.out.write(name)
        else: 
            self.response.out.write('Pass Name as param q.')

application = webapp.WSGIApplication(
   [
    ('/', MainPage),

    # kinos
    ('/kinos/', kinos.KinoList),
    ('/kinos/add/', kinos.KinoEdit),
    ('/kinos/(.*)/', kinos.KinoDetail),
 
    # movies
    ('/movies/add/', movies.AddMovie),
    ('/movies/(.*)/', movies.MovieDetail),
    ('/movies/', movies.MovieList),
    ('/today/', features.FeatureList),
    ('/upcoming/', movies.MoviesUpcoming), 
    ('/features/(.*)/', features.FeatureDetail ),  

    # ('/movie/(.*)', Movielisting ),
    ('/movies/get_original_name/', GetIMDBName),

    # users 
    ('/profile/', users.UserProfileController ), 

    # development 
    # inserts test data into the datastore. call only once 
    ('/testdata/', LoadFixture), 
   ], debug=True)

def main():
   run_wsgi_app(application)

if __name__ == "__main__":
  main()
