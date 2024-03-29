from google.appengine.ext import webapp, db
from models import UserProfile
from settings import * 
from google.appengine.api import users
from google.appengine.ext.webapp import template
from util import tmpl, add_user_to_context
import logging

class UserProfileController(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            #users.create_logout_url(self.request.path)
            profile = UserProfile.gql("WHERE user = :1",  users.get_current_user()).get()
            self.response.out.write(template.render(
                tmpl('templates/edit_profile.html'), 
                {'user': user, 'profile': profile, 'api_key': GOOGLE_MAPS_KEY}))
        else:
            #users.create_login_url(self.request.path)
            self.response.out.write('<a href="%s">Login</a>' % users.create_login_url(self.request.uri))
            
            # TODO: display read-only profile

    def post(self):
        """Recieves the Userprofile-form and updates the database. """
        user = users.get_current_user()
        # get the profile of the logged in user or create a new one
        # there should be a method like get_or_create() but i cant find it 
        # in the docs
        profile = UserProfile.gql("WHERE user = :1",  user).get()
        if not profile: 
            profile = UserProfile(user=user)
            logging.debug("New user profile created for user %s" % user) 
      
        # take the posted values and update the profile with it 
        if self.request.get('mlurl',None): 
            profile.movielens_url = db.Link(self.request.get('mlurl'))       

        if self.request.get('nick',None): 
            profile.nick = self.request.get('nick') 

        if self.request.get('q',None): 
            profile.adress = self.request.get('q')       

        profile.geo = db.GeoPt( 
                           float(self.request.get('lat',0)),
                           float(self.request.get('long',0)) )   
        profile.put()
 
        # the return to the same template as the get-controller 
        # but pass a variable saved that tells the template that the
        # profile was savegd
        self.response.out.write(template.render(
             tmpl('templates/edit_profile.html'),
             {'user': user, 'profile': profile, 'saved':True, 'api_key': GOOGLE_MAPS_KEY})
        )

        
class PublicProfile(webapp.RequestHandler):
    def get(self, nick):
        context = add_user_to_context()  
          
        p = UserProfile.all().filter('nick =', nick ).get()
        if p:
            context['profile'] = p
        else: 
            context['nick'] = nick 
         
        self.response.out.write(
             template.render(tmpl('templates/public_profile.html'),
             context
        ))


