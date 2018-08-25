#This file defines the Datastore model used in our project

from google.appengine.ext import ndb #imports Google Datastore

class Subscriber(ndb.Model): #defines Subscriber data type
    first_name = ndb.StringProperty(required=True) #holds user first name
    last_name = ndb.StringProperty(required=True) #holds user last name
    work_zipcode = ndb.StringProperty(required=True) #holds user work zip
    home_zipcode = ndb.StringProperty(required=True) #holds user home zip
    email = ndb.StringProperty(required=True) #holds user email
    phone_number = ndb.StringProperty(required=True) #holds user phone number as 10 digit string
    phone_carrier = ndb.StringProperty(required=True) #holds user phone carrier

# TO BE POSSIBLY IMPLEMENTED LATER
# class Report(ndb.Model): #holds notification report HTML
#     id = ndb.StringProperty(required=True)
#     report_HTML = ndb.StringProperty(required=True)
