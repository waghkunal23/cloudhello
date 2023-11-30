import webapp2
#request coming from browser ,how to send is define by webapp2
class MainPage(webapp2.RequestHandler):
#this class serve the data
    def get(self):
        self.response.write("Hello World")

app = webapp2.WSGIApplication([('/',MainPage)],debug=True)
#wsgi -server - if particular request receive by application at a given route , that route need to fetch particular data from this class
#arguments- the path , class sending DATA, error telling on