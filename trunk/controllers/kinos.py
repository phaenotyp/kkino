from google.appengine.ext import webapp
from models import UserProfile
from settings import * 
from google.appengine.api import users
from google.appengine.ext.webapp import template
from util import tmpl
from google.appengine.ext import db

class KinoList(webapp.RequestHandler):
    def get(self):
        cinemas = db.GqlQuery("SELECT * FROM Kino ORDER BY name ASC").fetch(20) 
        for c in cinemas: 
           c.url = c.get_url()

        self.response.out.write(template.render(tmpl('templates/cinemas.html'), 
                               {'kinos':cinemas } 
                                )) 
class KinoDetail(webapp.RequestHandler):
    def get(self, name):
        cinema = Kino.all().filter('name =', name ) 
        self.response.out.write(template.render(tmpl('templates/cinema.html'), 
                               {'kino': cinema, 'name': name} 
                                )) 


class KinoAdd(webapp.RequestHandler):
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

