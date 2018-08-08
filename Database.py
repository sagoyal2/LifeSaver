from google.appengine.ext import db #imports Google Datastore

class Subscriber(db.Model): #defines Subscriber data type
    name = db.StringProperty(required=True) #holds user name
    zipcode = db.StringProperty(required=True) #holds user zip
    email = db.StringProperty() #holds user email
    phone_number = db.StringProperty() #holds user phone number as 10 digit string
    phone_carrier = db.StringProperty() #holds user phone carrier
