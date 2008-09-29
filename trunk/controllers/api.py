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
        self.response.out.write(
           "[" + ','.join([c.json for c in cinemas]) + "]" 
        ) 

class KinoDetail(webapp.RequestHandler):
    def get(self, slug):
        k = Kino.all().filter('slug =', slug ).get() 
        self.response.out.write(
            k.json
        ) 

class KinoDetailFeature(webapp.RequestHandler):
    def get(self, slug):
        k = Kino.all().filter('slug =', slug ).get() 
        self.response.out.write(
            "{ kino:'%s', features:[%s] }" % ( 
                 k.name, 
                 ', '.join([self.feature_json(f) for f in k.features])
             )  
        ) 

    def feature_json(self, feature):
        return "{ movie:'%s', datetime:'%s', going:[%s]  }" % (
                 feature.movie.name,
                 feature.datetime.strftime("%d.%m.%Y %H:%M"), 
                 ', '.join( ["'%s'" % u.nickname() for u in feature.going] )   
               )





