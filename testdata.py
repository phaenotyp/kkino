from google.appengine.ext import db
from models import Kino, Movie, Feature
from datetime import datetime

# Kinos anlegen
met = Kino(name="Metropolis") 
met.put() 

dom = Kino(name="Cinedom") 
dom.put() 

# Movies
bkr = Movie(name="Be Kind Rewind", imdb="http://www.imdb.com/title/tt0799934/")
bkr.put()

bp = Movie(name="Block Party", imdb="http://www.imdb.com/title/tt0425598/")
bp.put()

# Features 
Feature( movie=bkr,kino=met, datetime=datetime(2008,9,12,20,15)).put() 
Feature( movie=bp,kino=met, datetime=datetime(2008,9,12,19,00)).put() 
Feature( movie=bp,kino=dom, datetime=datetime(2008,9,12,17,30)).put() 

