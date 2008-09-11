from google.appengine.ext import db

class Kino(db.Model):
    name = db.StringProperty()
    adress = db.PostalAddressProperty()
    coordinates = db.GeoPtProperty() 

class Movie(db.Model):
    name = db.StringProperty()
    imdb = db.LinkProperty() 
 

class Feature(db.Model):
    movie = db.ReferenceProperty(reference_class=Movie)
    kino = db.ReferenceProperty(reference_class=Kino)
    datetime = db.DateTimeProperty() 

class UserProfile(db.Model):
    user = db.UserProperty()
    movielens_url = db.LinkProperty()
    coordinates = db.GeoPtProperty() 
 
