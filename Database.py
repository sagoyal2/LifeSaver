from google.appengine.ext import db #imports Google Datastore

class Subscriber(db.Model): #defines Subscriber data type
    first_name = db.StringProperty(required=True) #holds user first name
    last_name = db.StringProperty(required=True) #holds user last name
    work_zipcode = db.StringProperty(required=True) #holds user work zip
    home_zipcode = db.StringProperty(required=True) #holds user home zip
    email = db.StringProperty(required=True) #holds user email
    phone_number = db.StringProperty(required=True) #holds user phone number as 10 digit string
    phone_carrier = db.StringProperty(required=True) #holds user phone carrier
