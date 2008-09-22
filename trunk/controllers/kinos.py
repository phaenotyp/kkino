from google.appengine.ext import webapp
from models import UserProfile, Kino, Feature
from settings import * 
from google.appengine.api import users
from google.appengine.ext.webapp import template
from util import tmpl, add_user_to_context
from google.appengine.ext import db
import cgi

class KinoList(webapp.RequestHandler):
    def get(self):
        cinemas = db.GqlQuery("SELECT * FROM Kino ORDER BY name ASC").fetch(20) 
        context = {'kinos':cinemas, 'api_key': GOOGLE_MAPS_KEY   } 
        context = add_user_to_context(context) 
        self.response.out.write(
            template.render(tmpl('templates/kinolist.html'), 
            context )) 

class KinoDetail(webapp.RequestHandler):
    def get(self, slug):
        k = Kino.all().filter('slug =', slug ).get() 
        context = {'kino': k, 'slug': slug  } 
        context = add_user_to_context(context)
        self.response.out.write(
               template.render(tmpl('templates/kinodetail.html'), 
                    context 
               )) 
    

class KinoEdit(webapp.RequestHandler):
    def get(self): 
        context = {}  
        user = users.get_current_user() 
        if user: 
            context['user'] = user
            context['logouturl'] = users.create_logout_url(self.request.url)
            profile = UserProfile.gql("WHERE user = :1",  users.get_current_user()).get()
            if profile:
                context['profile'] = profile 
        else:
             context['logouturl'] = users.create_login_url(self.request.url)
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

