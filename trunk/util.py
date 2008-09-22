from google.appengine.api.urlfetch import fetch 
import os

altname_url = 'http://www.imdb.com/alternatename/?q=%s'
aka_search_url = u'http://www.imdb.com/find?q=%s;s=tt;site=aka'

def get_imdb_name(aka): 
    from urllib import quote_plus
    resp = fetch(aka_search_url % quote_plus(unicode(aka))) 
    if resp.status_code == 200: 
        import re 
        m = re.compile('<h1>(.*)<').match(resp.content) 
        return resp.content 
        # TODO: get the h1, extract the orignal title and return it
    return 'Clockwork Orange'

def get_user_movies(user): 
    #from google.appengine.api import users
    resp = fetch(user.movielens_url)
    if resp.status_code == 200:  
        pass
        # TODO: parse via feedparser 
         
def tmpl(name): return os.path.join(os.path.dirname(__file__), name)


def sluggify(name):  
    return name.lower().replace(' ', '-')

def add_user_to_context(context={}): 
    """Takes a dictionary and add a key user to it if a user is logged in.
       Otherwise it adds a key loginurl.

       Returns the altered dictionary.""" 
    from google.appengine.api import users
    user = users.get_current_user() 
    if user:
         context['user'] = user  
         context['logouturl'] = users.create_logout_url("/") 
    else: 
         context['loginurl'] = users.create_login_url("/") 
    return context 
