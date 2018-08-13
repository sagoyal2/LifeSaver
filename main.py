import webapp2
import jinja2
import os
import ExtraMethods
import Keys
import logging

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True) #creates environment variable for HTML rendering

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/app.html')
        self.response.write(template.render())

    def post(self):
        latitudeInput = self.request.get('latitudeInput')
        longitudeInput = self.request.get('longitudeInput')
        logging.info(latitudeInput)
        logging.info(longitudeInput)
        return webapp2.redirect("/report")


class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/register.html')
        self.response.write(template.render())
    def post(self):
        logging.info("POST METHOD WAS CALLED")

        # url = self.request.get('#url')

        first_name = self.request.get('first_name')
        last_name = self.request.get('last_name')
        work_zipcode = self.request.get('work_zipcode')
        home_zipcode = self.request.get('home_zipcode')
        email = self.request.get('email')
        phone_number = self.request.get('phone_number')
        phone_carrier = self.request.get('phone_carrier')

        logging.info("FILE NAME: " + first_name)
        logging.info("FILE PATH: " + email)
        logging.info("DETAILS: " + phone_carrier)

        #DOES SOMETHING WITH EMAIL HERE !!!
        logging.info("Message Sent")


        data = {
            "first_name" : first_name,
            "last_name" : last_name,
            "work_zipcode" : work_zipcode,
            "home_zipcode" : home_zipcode,
            "email" : email,
            "phone_number" : phone_number,
            "phone_carrier" : phone_carrier
        }

        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('templates/register_test.html')

        logging.info("NEW PAGE IS ABOUT TO RENDER")

        self.response.write(template.render(data))


        """
        self.response.headers['Content-Type'] = 'text/html'
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/rhf.html')
        self.response.write(template.render())
        """


class RHFHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/rhf.html')
        self.response.write(template.render())

class ReportHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('templates/report.html')

        data = {
            "firebase_apiKey" : Keys.firebase_apiKey,
            "firebase_authDomain" : Keys.firebase_authDomain,
            "firebase_databaseURL" : Keys.firebase_databaseURL,
            "firebase_projectId" : Keys.firebase_projectId,
            "firebase_storageBucket" : Keys.firebase_storageBucket,
            "firebase_messagingSenderId" : Keys.firebase_messagingSenderId
        }

        self.response.write(template.render(data))

    def post(self):
        logging.info("POST METHOD WAS CALLED")

        # url = self.request.get('#url')
        details = self.request.get('details')
        fileName = self.request.get('fileNameInput')
        filePath = self.request.get('filePathInput')
        fileURL = self.request.get('fileURLInput')

        logging.info("FILE NAME: " + fileName)
        logging.info("FILE PATH: " + filePath)
        logging.info("DETAILS: " + details)

        #DOES SOMETHING WITH EMAIL HERE !!!
        logging.info("EMAIL SENT")


        data = {
            # "url":url,
            "fileName":fileName,
            "filePath":filePath,
            "fileURL":fileURL,
            "details":details,
            # firebase_apiKey : Keys.firebase_apiKey,
            # firebase_authDomain : Keys.firebase_authDomain,
            # firebase_databaseURL : Keys.firebase_databaseURL,
            # firebase_projectId : Keys.firebase_projectId,
            # firebase_storageBucket : Keys.firebase_storageBucket,
            # firebase_messagingSenderId : Keys.firebase_messagingSenderId
        }

        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('templates/report_test.html')

        logging.info("NEW PAGE IS ABOUT TO RENDER")

        self.response.write(template.render(data))

        # self.response.headers['Content-Type'] = 'text/html'
        # template = jinja_env.get_template('static/rhf.html')
        # self.response.write(template.render())


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
        self.response.write(ExtraMethods.getNearbyZipCodesJSON("60565", 5))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/register', RegisterHandler),
    ('/RHF', RHFHandler),
    ('/report', ReportHandler),
    ('/creators', CreatorsHandler),
    ('/aboutUs', AboutUsHandler),
    ('/test', TestHandler)
    ], debug=True)
