import webapp2
import jinja2
import os
import ExtraMethods

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True) #creates environment variable for HTML rendering

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/app.html')
        self.response.write(template.render())

class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write("Needs subscribe page")

class RHFHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/rhf.html')
        self.response.write(template.render())

class ReportHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('web-dictaphone-gh-pages/index.html')
        self.response.write(template.render())

class CreatorsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/creators.html')
        self.response.write(template.render())

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/aboutUs.html')
        self.response.write(template.render())

class TestHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        # latitudeLongitude = [41.717713, -88.151134]
        # # self.response.write(ExtraMethods.latLonToZIP(latitudeLongitude[0], latitudeLongitude[1]))
        # self.response.write(ExtraMethods.latLonToAddress(latitudeLongitude[0], latitudeLongitude[1]))
        self.response.write(ExtraMethods.getNearbyZipCodesJSON(60565, 3))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/register', RegisterHandler),
    ('/RHF', RHFHandler),
    ('/report', ReportHandler),
    ('/creators', CreatorsHandler),
    ('/aboutUs', AboutUsHandler),
    ('/test', TestHandler)
    ], debug=True)
