from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext.webapp import template
import datetime, cgi
from models import Movie, Feature, Kino, UserProfile
from google.appengine.ext import db
import util

from controllers import users, kinos

def tmpl(name): util.tmpl(name) 

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('KoelnKino')
       
   
class AddMovie(webapp.RequestHandler):
     def get(self): 
        self.response.out.write("""
      <html>
        <body>
          <form method="post">
            <div><input type="text" name="name" /></div>
            <div><input type="submit" value="Sign Guestbook" /></div>
          </form>
        </body>
      </html>""")
    
     def post(self):      
         t = Movie()
         t.name = cgi.escape(self.request.get('name'))
         t.put()
         self.redirect('/kinos/') 
 

class MoviesToday(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        feats = db.GqlQuery("SELECT * FROM Feature ORDER BY datetime DESC") 
        for feat in feats:
            self.respose.out.write( feat.movie.name )

        self.response.out.write('KoelnKino')

class MoviesUpcoming(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        showings = db.GqlQuery("SELECT * FROM Showing ORDER BY datetime DESC") 
        for showing in showings:
            self.respose.out.write( showing.movie.name )

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
    ('/kinos/', kinos.KinoList),
    ('/kinos/(.*)/', kinos.KinoDetail),
    ('/kinos/add/', kinos.KinoAdd),
    ('/movies/add/', AddMovie),
    ('/today/', MoviesToday),
    ('/upcoming/', MoviesUpcoming), 
    ('/profile/', users.UserProfileController ), 
    # ('/movie/(.*)', Movielisting ),
    ('/movies/get_original_name/', GetIMDBName),
    ('/testdata/', LoadFixture),
   ], debug=True)

def main():
   run_wsgi_app(application)

if __name__ == "__main__":
  main()
