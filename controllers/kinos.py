from google.appengine.ext import webapp
from models import UserProfile, Kino
from settings import * 
from google.appengine.api import users
from google.appengine.ext.webapp import template
from util import tmpl
from google.appengine.ext import db
import cgi

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


class KinoEdit(webapp.RequestHandler):
    def get(self): 
        context = {}  
        user = users.get_current_user() 
        if user: 
            profile = UserProfile.gql("WHERE user = :1",  users.get_current_user()).get()
            if profile:
                context['profile'] = profile 
        page = template.render(tmpl('templates/kinoform.html'),context) 
        self.response.out.write(page) 
   
    def post(self):      
       
        name = cgi.escape(self.request.get('name')) 
        k = Kino(name=name)
        k.geo = db.GeoPt(
                           float(self.request.get('lat',0)),
                           float(self.request.get('long',0)) )
        if self.request.get('adress',None):
            profile.adress = self.request.get('adress')

        k.put()
        self.redirect('/kinos/') 

