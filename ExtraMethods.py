import Keys
import json
from google.appengine.api import urlfetch

import urllib
import urllib2

import logging

#returns a list of zip codes within distance of ZIP
#https://docs.python.org/2/howto/urllib2.html
def getNearbyZipCodesJSON(ZIP, distance): #NOTE that ZIP is string, distance is number
    templateUrl = "http://www.zipcodeapi.com/rest/%s/radius.json/%s/%s/miles?minimal"
    zip_url = templateUrl % (Keys.zip_key, ZIP, str(distance))
    req = urllib2.Request(zip_url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    jsonText = json.loads(the_page)
    refined = jsonText["zip_codes"]
    return refined

# SOURCE: https://www.makeuseof.com/tag/email-to-sms/
# First is SMS, Second is MMS (use the first!)
# Alltel: sms.alltelwireless.com | mms.alltelwireless.com
# AT&T: txt.att.net | mms.att.net
# Boost Mobile: sms.myboostmobile.com | myboostmobile.com
# Cricket Wireless: txt.att.net | mms.att.net
# MetroPCS: mymetropcs.com | mymetropcs.com
# Project Fi: msg.fi.google.com
# Republic Wireless: text.republicwireless.com
# Sprint: messaging.sprintpcs.com | pm.sprint.com
# Ting: message.ting.com
# T-Mobile: tmomail.net
# US Cellular: email.uscc.net | mms.uscc.net
# Verizon Wireless: vtext.com | vzwpix.com
# Virgin Mobile: vmobl.com | vmpix.com

#dictionary of carriers to email extensions
phoneCarrierDictionary = {
    "Alltel":"sms.alltelwireless.com",
    "AT&T":"txt.att.net",
    "Boost Mobile":"sms.myboostmobile.com",
    "Cricket Wireless":"txt.att.net",
    "MetroPCS":"mymetropcs.com",
    "Project Fi":"msg.fi.google.com",
    "Republic Wireless":"text.republicwireless.com",
    "Sprint":"messaging.sprintpcs.com",
    "Ting":"message.ting.com",
    "T-Mobile":"tmomail.net",
    "US Cellular":"email.uscc.net",
    "Verizon Wireless":"vtext.com",
    "Virgin Mobile":"vmobl.com"
}

#inputs a phone number and carrier and outputs the email address for that number
def getPhoneNumberEmail(phoneNumber, phoneCarrier):
    if phoneCarrier in phoneCarrierDictionary:
        return phoneNumber + "@" + phoneCarrierDictionary[phoneCarrier]
    return ""

#converts latitude and longitude to ZIP
#https://developers.google.com/maps/documentation/geocoding/intro
def latLonToZIP(latitude, longitude):
    google_url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&result_type=postal_code&key=%s" % (str(latitude), str(longitude), Keys.google_key)
    urlContent = urlfetch.fetch(google_url).content
    logging.info(google_url)
    response = json.loads(urlContent)
    response = response["results"]
    response = response[0]
    response = response["address_components"]
    response = response[0]
    response = response["short_name"]
    return str(response)

#converts latitude and longitude to address
#https://developers.google.com/maps/documentation/geocoding/intro
def latLonToAddress(latitude, longitude):
    google_url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&result_type=street_address&key=%s" % (str(latitude), str(longitude), Keys.google_key)
    urlContent = urlfetch.fetch(google_url).content
    response = json.loads(urlContent)
    return str(response["results"][0]["formatted_address"])
