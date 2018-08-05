import webapp2
# import jinja2
# import os

# jinja_env = jinja2.Environment(
#     loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
#     extensions=['jinja2.ext.autoescape'],
#     autoescape=True) #creates environment variable for HTML rendering

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        return self.response.write("TEST")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
