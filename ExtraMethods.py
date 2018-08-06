import Keys
import json
import urlfetch

# getNearbyZipCodes(ZIP code, distance)
# ZIP Code API

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

#https://developers.google.com/maps/documentation/geocoding/intro
def latLonToZIP(latitude, longitude):
    google_url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&result_type=postal_code&key=%s" % (str(latitude), str(longitude), Keys.google_key)
    urlContent = urlfetch.fetch(google_url).content
    response = json.loads(urlContent)
    return str(response["results"][0]["address_components"][0]["short_name"])
