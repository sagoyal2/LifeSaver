from google.appengine.ext import db

class Subscriber(db.Model):
    name = db.StringProperty(required=True)
    location = db.StringProperty(required=True)
    birthdate = db.DateProperty()
    weight_in_pounds = db.IntegerProperty()
    spayed_or_neutered = db.BooleanProperty()
