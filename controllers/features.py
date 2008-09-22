from google.appengine.ext import webapp
from models import UserProfile, Feature
from settings import * 
from google.appengine.api import users
from google.appengine.ext.webapp import template
from util import tmpl
from google.appengine.ext import db
import cgi

class FeatureList(webapp.RequestHandler):
    def get(self):
        feats = Feature.all().fetch(50)  

        # denormalize the length of going into the feature object
        # 
        for f in feats:
            if len(f.going) > 0:
                f.goers = len(f.going)  

        self.response.out.write(template.render(tmpl('templates/featurelist.html'), 
                               {'features':feats, 'len':len(feats) } 
                                )) 

class FeatureDetail(webapp.RequestHandler):
    def get(self, id):
        k = db.Key.from_path('Feature', int(id))
        f = db.get(k)
        #f = Feature.all().filter('Key =', k ).get()
        
        context = { 'feature' : f }
        user = users.get_current_user() 
        if user:
            context['user'] = user
            if user in f.going: 
                context['going'] = True 
 
        page = template.render(tmpl('templates/featuredetail.html'),context) 
        self.response.out.write(page) 

    def post(self,id):  
        """Adds or removes the current user from the list of users going to this feature."""
        k = db.Key.from_path('Feature', int(id))
        f = db.get(k)
        context = { 'feature' : f }
        user = users.get_current_user() 
        if user:
            context['user'] = user
            if self.request.get('going') == 'true':     
                f.going.append(user) 
                f.put() 
                context['going'] = True 
            else: 
                try:
                    del f.going[f.going.index(user)] 
                    f.put() 
                except: 
                    pass
        page = template.render(tmpl('templates/featuredetail.html'),context) 
        self.response.out.write(page) 

class FeatureEdit(webapp.RequestHandler):
    def get(self): 
        context = {}  
        # get the logged-in user and try to fetch the according profile
        # from db, if it exists. pass to the template
        user = users.get_current_user() 
        if user: 
            profile = UserProfile.gql("WHERE user = :1",  users.get_current_user()).get()
            if profile:
                context['profile'] = profile 
        page = template.render(tmpl('templates/featureform.html'),context) 
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
