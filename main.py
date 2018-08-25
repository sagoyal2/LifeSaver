import webapp2
import jinja2
import os
import ExtraMethods
# import EmailMain
import EmailMain2
import Database
import Keys
import logging

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True) #creates environment variable for HTML rendering

#This is the handler for the main page
class MainHandler(webapp2.RequestHandler):
    #the GET method returns the static home page
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/app.html')
        self.response.write(template.render())

    #the POST method sends an email alert based on the location of the user
    def post(self):
        #gets location of person making the report
        latitudeInput = self.request.get('latitudeInput')
        longitudeInput = self.request.get('longitudeInput')
        logging.info(latitudeInput)
        logging.info(longitudeInput)

        # if latitudeInput is "NONE" or longitudeInput is "NONE":
        #     return webapp2.redirect("/main")

        #gets address and ZIP code using extramethods
        zip = ExtraMethods.latLonToZIP(latitudeInput, longitudeInput)
        address = ExtraMethods.latLonToAddress(latitudeInput, longitudeInput)
        logging.info(zip)
        logging.info(address)

        #calls the EmailMain method to alert all users
        subject = "ALERT: SHOOTING IN YOUR %s AREA"
        content = "AVOID '%s' AND FOLLOW THESE STEPS FOR SAFETY: <a href='www.life-saver-demo.appspot.com/RHF'>www.life-saver-demo.appspot.com/RHF</a>" % (address)
        html_content = "<html><head></head><body>%s</body></html>" % (content)

        searchRadius = 10 #10 miles

        for zipCode in ExtraMethods.getNearbyZipCodesJSON(zip, searchRadius):
            #EmailMain2.sendAlertsHome(zipCode, subject % ("LOCAL"), content)
            #EmailMain2.sendAlertsWork(zipCode, subject % ("WORK"), content)
            EmailMain2.sendAlertsHome(zipCode, subject % ("LOCAL"), html_content)
            EmailMain2.sendAlertsWork(zipCode, subject % ("WORK"), html_content)


        logging.info("sent alerts!")

        logging.info("redirect to report page!")
        return webapp2.redirect("/report")

#This is the handler for the register page
class RegisterHandler(webapp2.RequestHandler):
    #the GET method returns the static register page
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/register.html')
        self.response.write(template.render())

    #the POST method adds to Datastore and returns a confirmation page/sends a notification
    def post(self):
        logging.info("POST METHOD WAS CALLED")

        first_name = self.request.get('first_name')
        last_name = self.request.get('last_name')
        work_zipcode = self.request.get('work_zipcode')
        home_zipcode = self.request.get('home_zipcode')
        email = self.request.get('email')
        phone_number = self.request.get('phone_number')
        phone_carrier = self.request.get('phone_carrier')

        # logging.info("FILE NAME: " + first_name)
        # logging.info("FILE PATH: " + email)
        # logging.info("DETAILS: " + phone_carrier)
        #
        # #DOES SOMETHING WITH EMAIL HERE !!!
        # logging.info("Message Sent")

        #CONFIRMATION NOTIFICATIONS
        if len(email) > 0:
            EmailMain2.SendOneEmail(email, "Thank you for subscribing!", "We will contact you at this email if there is ever an incident near your work or home ZIP code.")
        if len(phone_number) > 0:
            EmailMain2.SendOneEmail(ExtraMethods.getPhoneNumberEmail(phone_number, phone_carrier), "Thank you for subscribing!", "We will contact you at this phone number if there is ever an incident near your work or home ZIP code.")


        data = {
            "first_name" : first_name,
            "last_name" : last_name,
            "work_zipcode" : work_zipcode,
            "home_zipcode" : home_zipcode,
            "email" : email,
            "phone_number" : phone_number,
            "phone_carrier" : phone_carrier
        }

        newUser = Database.Subscriber(first_name=first_name, last_name=last_name, work_zipcode=work_zipcode, home_zipcode=home_zipcode, email=email, phone_number=phone_number, phone_carrier=phone_carrier)
        newUser.put()

        logging.info("Added to Datastore!")

        # return webapp2.redirect("/report")

        # COMMENTED OUT OLD TEMPLATE/TEST PAGE FOR CONFIRMATION
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('templates/register_confirmation.html')

        self.response.write(template.render(data))


        # """
        # self.response.headers['Content-Type'] = 'text/html'
        # self.response.headers['Content-Type'] = 'text/html'
        # template = jinja_env.get_template('static/rhf.html')
        # self.response.write(template.render())
        # """


#This is the handler for the Run, Hide, Fight page
class RHFHandler(webapp2.RequestHandler):
    #the GET method returns the static RHF page
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/rhf.html')
        self.response.write(template.render())

#This is the handler for the audio report page
class ReportHandler(webapp2.RequestHandler):
    #the GET method renders the Firebase credentials and displays the report page
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

    #the POST method retrieves the user's input and sends another alert
    def post(self):
        #gets location of person making the report
        latitudeInput = self.request.get('latitudeInput')
        longitudeInput = self.request.get('longitudeInput')
        logging.info(latitudeInput)
        logging.info(longitudeInput)

        #gets address and ZIP code using extramethods
        zip = ExtraMethods.latLonToZIP(latitudeInput, longitudeInput)
        address = ExtraMethods.latLonToAddress(latitudeInput, longitudeInput)
        logging.info(zip)
        logging.info(address)

        #gets details and/or file info
        details = self.request.get('details')
        fileName = self.request.get('fileNameInput')
        filePath = self.request.get('filePathInput')
        fileURL = self.request.get('fileURLInput')

        #calls the EmailMain method to alert all users
        subject = "ALERT: SHOOTING IN YOUR %s AREA"
        content = "AVOID '%s'. DETAILS FROM THE AREA INCLUDE THAT '%s'. AUDIO FROM THE AREA IS LINKED HERE '%s'. FOLLOW THESE STEPS FOR SAFETY: <a href='www.life-saver-demo.appspot.com/RHF'>www.life-saver-demo.appspot.com/RHF</a>" % (address, details, fileURL)
        html_content = """<html><head></head><body>
                            <p>%s</p>
                            <div><a href="https://life-saver-demo.appspot.com/report_notification/?address=%s&details=%s&url=%s">View this alert online</a></div>
                            </body></html>""" % (content, address, details, fileURL.replace("https://firebasestorage.googleapis.com/v0/b/life-saver-demo.appspot.com/o/audio%2F","").replace("https://firebasestorage.googleapis.com/v0/b/life-saver-demo.appspot.com/o/audio/","").replace("&","*"))
        #https://www.w3schools.com/html/html5_audio.asp

        searchRadius = 10 #10 miles

        for zipCode in ExtraMethods.getNearbyZipCodesJSON(zip, searchRadius):
            #EmailMain.sendAlerts(zipCode, subject, content)
            # EmailMain2.sendAlertsHome(zipCode, subject % ("LOCAL"), content)
            # EmailMain2.sendAlertsWork(zipCode, subject % ("WORK"), content)
            EmailMain2.sendAlertsHome(zipCode, subject % ("LOCAL"), html_content)
            EmailMain2.sendAlertsWork(zipCode, subject % ("WORK"), html_content)


        logging.info("sent alerts!")

        # data = {
        #     "fileName":fileName,
        #     "filePath":filePath,
        #     "fileURL":fileURL,
        #     "details":details,
        #     "address":address,
        #     "zip":zip
        # }
        #
        # self.response.headers['Content-Type'] = 'text/html'
        # template = jinja_env.get_template('templates/report_test.html')
        #
        # self.response.write(template.render(data))

        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/rhf.html')
        self.response.write(template.render())


class CreatorsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/creators.html')
        self.response.write(template.render())

class AboutLifeSaverHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/aboutLifeSaver.html')
        self.response.write(template.render())


#This allows us to display an email/text notification in the browswer
class ReportNotificationHandler(webapp2.RequestHandler):
    #The GET method takes queries from the URL and displays them in the web, adding audio controls
    def get(self):
        #https://stackoverflow.com/questions/5767678/appengine-get-parameters
        addressRAW = self.request.get("address")
        detailsRAW = self.request.get("details")
        fileURLRAW = self.request.get("url")

        address = addressRAW.encode('ascii','ignore')
        details = detailsRAW.encode('ascii','ignore')
        fileURL = "https://firebasestorage.googleapis.com/v0/b/life-saver-demo.appspot.com/o/audio%2F" + fileURLRAW.encode('ascii','ignore').replace("*","&")

        content = "AVOID '%s'. DETAILS FROM THE AREA INCLUDE THAT '%s'. AUDIO FROM THE AREA IS LINKED HERE '%s'. FOLLOW THESE STEPS FOR SAFETY: <a href='https://www.life-saver-demo.appspot.com/RHF'>https://www.life-saver-demo.appspot.com/RHF</a>" % (address, details, fileURL)
        html_content = """<html><head></head><body>
                            <p>%s</p>
                            <audio controls>
                            <source src="%s" type="audio/ogg">
                            Your browser does not support the audio controls element.
                            </audio>
                            </body></html>""" % (content, fileURL)

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(html_content)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/register', RegisterHandler),
    ('/RHF', RHFHandler),
    ('/report', ReportHandler),
    ('/creators', CreatorsHandler),
    ('/about', AboutLifeSaverHandler),
    ('/report_notification/', ReportNotificationHandler)
    ], debug=True)
