from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import datetime, os, cgi
from models import Movie, Feature, Kino
from google.appengine.ext import db
import util

def tmpl(name): return os.path.join(os.path.dirname(__file__), name) 

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('KoelnKino')

class CinemaList(webapp.RequestHandler):
    def get(self):
        cinemas = db.GqlQuery("SELECT * FROM Kino ORDER BY name ASC").fetch(20) 
        for c in cinemas: 
           c.url = c.get_url()

        self.response.out.write(template.render(tmpl('templates/cinemas.html'), 
                               {'kinos':cinemas } 
                                )) 
class OneCinema(webapp.RequestHandler):
    def get(self, name):
        cinema = Kino.all().filter('name =', name ) 
        self.response.out.write(template.render(tmpl('templates/cinema.html'), 
                               {'kino': cinema, 'name': name} 
                                )) 
 

class CinemaList2(webapp.RequestHandler):
    def get(self):
        cinemas = db.GqlQuery("SELECT * FROM Theater ORDER BY name ASC") 
        out = []
        a = out.append
        a('<html>')  
        a('<body>') 
        a('<ul>') 
        for c in cinemas:
           a('<li>%s</li>' % c.name)  
        a('</ul>') 
        a('</body>') 
        a('</html>')  
        self.response.out.write("\n".join(out)) 
 

class AddCinema(webapp.RequestHandler):
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
        t = Kino()
        t.name = cgi.escape(self.request.get('name'))
        t.put()
        self.redirect('/kinos/') 
        
   
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

class UserProfile(webapp.RequestHandler): 
    def get(self): 
        user = users.get_current_user()
        if user:
            users.create_logout_url(self.request.path)
            # TODO: display profile form
        else:
            users.create_login_url(self.request.path)
            # TODO: display read-only profile


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
                                        ('/kinos/', CinemaList),
                                        ('/kinos/(.*)/', OneCinema),
                                        ('/kinos/add/', AddCinema),
                                        ('/movies/add/', AddMovie),
                                        ('/today/', MoviesToday),
                                        ('/upcoming/', MoviesUpcoming), 
                                        ('/profile/', UserProfile ), 
                                  #      ('/movie/(.*)', Movielisting ),
                                        ('/movies/get_original_name/', GetIMDBName),
                                        ('/testdata/', LoadFixture),
                                     ],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()


