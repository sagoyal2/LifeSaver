import webapp2
import jinja2
import os
import ExtraMethods
import Keys

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
        template = jinja_env.get_template('static/report.html')

        data = {
            firebase_apiKey : Keys.firebase_apiKey,
            firebase_authDomain : Keys.firebase_authDomain,
            firebase_databaseURL : Keys.firebase_databaseURL,
            firebase_projectId : Keys.firebase_projectId,
            firebase_storageBucket : Keys.firebase_storageBucket,
            firebase_messagingSenderId : Keys.firebase_messagingSenderId
        }

        self.response.write(template.render(data))

    def post(self):
        url = self.request.get('url')
        details = self.request.get('details')

        data = {
            "url":url,
            "details":details,
            firebase_apiKey : Keys.firebase_apiKey,
            firebase_authDomain : Keys.firebase_authDomain,
            firebase_databaseURL : Keys.firebase_databaseURL,
            firebase_projectId : Keys.firebase_projectId,
            firebase_storageBucket : Keys.firebase_storageBucket,
            firebase_messagingSenderId : Keys.firebase_messagingSenderId
        }

        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/report_test.html')
        self.response.write(template.render(data))

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
