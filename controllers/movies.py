from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template
from util import tmpl, add_user_to_context 
from settings import *

class AddMovie(webapp.RequestHandler):
    def get(self):
        """Displays a form to add a new movie to the datastore""" 
        context = { 'api_key': GOOGLE_MAPS_KEY}
        context = add_user_to_context(context) 
        self.response.out.write(template.render(tmpl('templates/addmovie.html'), context ))

    def post(self):
        """Recieves the form for a new movie and puts it into the datastore"""
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
