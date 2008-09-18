from google.appengine.ext import db

class Kino(db.Model):
    name = db.StringProperty(required=True)
    adress = db.PostalAddressProperty()
    geo = db.GeoPtProperty() 

    def get_url(self): 
        return '/kinos/%s/' % self.name.lower() 

class Movie(db.Model):
    name = db.StringProperty(required=True)
    imdb = db.LinkProperty() 

class Feature(db.Model):
    movie = db.ReferenceProperty(reference_class=Movie, collection_name="features")
    kino = db.ReferenceProperty(reference_class=Kino, collection_name="features")
    datetime = db.DateTimeProperty() 

class UserProfile(db.Model):
    user = db.UserProperty(required=True)
    movielens_url = db.LinkProperty()
    adress = db.StringProperty()  
    geo = db.GeoPtProperty() 
