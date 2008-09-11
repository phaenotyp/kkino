from google.appengine.api.urlfetch import fetch 

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
         
    
    
