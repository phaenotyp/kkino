from google.appengine.ext import webapp
from models import UserProfile
from settings import * 
from google.appengine.api import users
from google.appengine.ext.webapp import template
from util import tmpl

class UserProfileController(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            #users.create_logout_url(self.request.path)
            profile = UserProfile.gql("WHERE user = :1",  users.get_current_user()).get()
            self.response.out.write(template.render(tmpl('templates/edit_profile.html'), {'user': user, 'api_key': GOOGLE_MAPS_KEY}))
        else:
            #users.create_login_url(self.request.path)
            self.response.out.write('<a href="%s">Login</a>' % users.create_login_url(self.request.uri))
            # TODO: display read-only profile

