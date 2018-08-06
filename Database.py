from google.appengine.ext import db #imports Google Datastore

class Subscriber(db.Model): #defines Subscriber data type
    name = db.StringProperty(required=True) #holds user name
    zipcode = db.StringProperty(required=True) #holds user zip
    email = db.StringProperty(required=True) #holds user email
    phone_number = db.StringProperty(required=True) #holds user phone number
    phone_carrier = db.StringProperty(required=True) #holds user phone carrier
