from google.appengine.ext import webapp

class AddMovie(webapp.RequestHandler):
     def get(self):
        self.response.out.write("""
      <html>
        <body>
          <form method="post">
            <div><input type="text" name="name" /></div>
            <div><input type="submit" value="Sign Guestbook" /></div>
          </form>
        </body>
      </html>""")

     def post(self):
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

