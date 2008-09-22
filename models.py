from google.appengine.ext import db
from google.appengine.api import users
from util import sluggify

class Kino(db.Model):
    """Movie-Theater"""
    name = db.StringProperty(required=True)
    adress = db.PostalAddressProperty()
    geo = db.GeoPtProperty() 
    slug = db.StringProperty()

    @property 
    def get_url(self): 
        """This can be used in templates cause it's a property""" 
        return '/kinos/%s/' % self.slug 

    def put(self):  
        """Overide put so that slug gets updated by name""" 
        self.slug = sluggify(self.name) 
        super(Kino, self).put()  

class Movie(db.Model):
    name = db.StringProperty(required=True)
    imdb = db.LinkProperty() 

    def rating_by_user(self, user): 
        return MLRating.gql('WHERE user = :1 and movie = :2', user, self).fetch(1)[0].mlrating 

class Feature(db.Model):
    movie = db.ReferenceProperty(reference_class=Movie, collection_name="features")
    kino = db.ReferenceProperty(reference_class=Kino, collection_name="features")
    datetime = db.DateTimeProperty() 
    going = db.ListProperty(users.User) 

    @property
    def get_url(self):
        return '/features/%s/' % self.key().id()

class MLRating(db.Model): 
    """A Movie-Rating as pulled from movielens.org.

       Should be a Float between 1 and 5."""
    movie = db.ReferenceProperty(reference_class=Movie, collection_name="ratings")
    user = db.UserProperty()
    mlrating = db.FloatProperty() 

    # TODO: validate mlrating
    
class UserProfile(db.Model):
    user = db.UserProperty(required=True)
    movielens_url = db.LinkProperty()
    adress = db.StringProperty()  
    geo = db.GeoPtProperty() 
 
    @property 
    def features(self): 
        """Returns a query objects of all the Features this user is attending."""
        return Feature.gql('WHERE going = :1', self.user) 
 
    @property 
    def ratings(self): 
        """Returns a query-object of all the ratings of the user this profile blongs to""" 
        return MLRating.gql('WHERE user = :1', self.user) 
   
