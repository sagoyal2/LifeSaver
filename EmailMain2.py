#EmailMain2 is the same as EmailMain except it fixes most/all of the errors!!

import ExtraMethods
import logging
#The commented lines below need to be discussed- they should work for now

#FOLLOW THIS FOR THE LIBRARIES BELOW https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27#vendoring
#RUN THIS CODE "pip install -t lib/ <library_name>"
import httplib2
from httplib2 import Http
import os
import Database

# from apiclient import discovery
from googleapiclient import discovery

#FOLLOW THIS https://stackoverflow.com/questions/18267749/importerror-no-module-named-apiclient-discovery
#FOLLOW THIS TOO: https://developers.google.com/api-client-library/python/start/installation

# from apiclient.discovery import build
from googleapiclient.discovery import build

import oauth2client
from oauth2client import file, client, tools


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
except:
    flags = None
#this last statement was an attempt to fix a runtime error

SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Quickstart'



def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    # cwd_dir = os.getcwd()
    #
    # credential_dir = os.path.join(cwd_dir)
    # if not os.path.exists(credential_dir):
    #     os.makedirs(credential_dir)
    # credential_path = os.path.join(credential_dir,
    #                                'credentials.json')
    #
    #
    # store = oauth2client.file.Storage(credential_path)
    #
    # credentials = store.get()

    #https://stackoverflow.com/questions/36119453/webapp2-read-only-file-system-error
    #https://www.pythonforbeginners.com/cheatsheet/python-file-handling
    filename = "credentials.json"
    file = open(filename, "r")

    jsonString = ""
    for line in file:
        jsonString += line

    # import json
    # realJson = json.loads(jsonString)

    #https://oauth2client.readthedocs.io/en/latest/source/oauth2client.client.html
    #credentials = oauth2client.client.AccessTokenCredentials.from_json(jsonString)
    credentials = oauth2client.client.Credentials.new_from_json(jsonString)


    # logging.info(credentials)
    #
    # if not credentials or credentials.invalid:
    #     flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    #     flow.user_agent = APPLICATION_NAME
    #
    #     if flags:
    #         credentials = tools.run_flow(flow, store, flags)
    #     else: # Needed only for compatability with Python 2.6
    #         credentials = tools.run(flow, store)
    #     print 'Storing credentials to ' + credential_path
    return credentials

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
from httplib2 import Http

# from apiclient import errors
from googleapiclient import errors


# from apiclient.discovery import build
from googleapiclient.discovery import build
credentials = get_credentials()
service = build('gmail', 'v1', http=credentials.authorize(Http()))

def SendMessage(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print 'Message Id: %s' % message['id']
    return message
  except errors.HttpError, error:
    print 'An error occurred: %s' % error


def CreateMessage(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64 encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  #return {'raw': base64.b64encode(message.as_string())}
  #https://stackoverflow.com/questions/26663529/invalid-value-for-bytestring-error-when-calling-gmail-send-api-with-base64-encod
  return {'raw': base64.b64encode(message.as_string()).replace('/','_').replace('+','-')}


# https://stackoverflow.com/questions/41403458/how-do-i-send-html-formatted-emails-through-the-gmail-api-for-python
def CreateHTMLMessage(sender, to, subject, message_html):
  message = MIMEText(message_html, 'html')
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  #return {'raw': base64.b64encode(message.as_string())}
  #https://stackoverflow.com/questions/26663529/invalid-value-for-bytestring-error-when-calling-gmail-send-api-with-base64-encod
  return {'raw': base64.b64encode(message.as_string()).replace('/','_').replace('+','-')}


# Recipient, subject, and content should be passed in as strings
def SendOneEmail(recipient, subject, content):
    # https://stackoverflow.com/questions/14698119/httpexception-deadline-exceeded-while-waiting-for-http-response-from-url-dead
    from google.appengine.api import urlfetch
    urlfetch.set_default_fetch_deadline(45)

    testMessage = CreateMessage('lifesaverprojectdemo@gmail.com', recipient, subject, content)
    logging.info(testMessage)
    #https://stackoverflow.com/questions/26663529/invalid-value-for-bytestring-error-when-calling-gmail-send-api-with-base64-encod
    # testMessage['raw'] = testMessage['raw'].replace('/','_').replace('+','-');
    # logging.info(testMessage)
    testSend = SendMessage(service, 'me', testMessage)

# Recipient, subject, and content should be passed in as strings
def SendOneHTMLEmail(recipient, subject, content):
    # https://stackoverflow.com/questions/14698119/httpexception-deadline-exceeded-while-waiting-for-http-response-from-url-dead
    from google.appengine.api import urlfetch
    urlfetch.set_default_fetch_deadline(45)

    testMessage = CreateHTMLMessage('lifesaverprojectdemo@gmail.com', recipient, subject, content)
    logging.info(testMessage)
    #https://stackoverflow.com/questions/26663529/invalid-value-for-bytestring-error-when-calling-gmail-send-api-with-base64-encod
    # testMessage['raw'] = testMessage['raw'].replace('/','_').replace('+','-');
    # logging.info(testMessage)
    testSend = SendMessage(service, 'me', testMessage)

# Will send an email to everybody with the specific zip code, using subject/content to draft the email
def sendAlertsHome(zipCode, subject, content):
    #queries once for home zip code
    q1 = Database.Subscriber.query(Database.Subscriber.home_zipcode == zipCode).fetch()
    logging.info(q1)
    # I don't think this code works @Diego, so I changed it to ^^ as a fix
    # q = Database.Subscriber.all()
    # q = q.filter(home_zipcode, zipCode)
    sendAlertsHelper(q1, subject, content)

def sendAlertsWork(zipCode, subject, content):
    #queries second time for work zip code
    q2 = Database.Subscriber.query(Database.Subscriber.work_zipcode == zipCode).fetch()
    logging.info(q2)
    # Same as before ^
    # q = Database.Subscriber.all()
    # q = q.filter(work_zipcode, zipCode)
    sendAlertsHelper(q2, subject, content)

# Will send an email to everyone in the list of queries, using subject/content to draft the email
def sendAlertsHelper(queries, subject, content):
    # I modified this to contact the user via email and/or phone, depending on what is available
    for user in queries:
        userEmail = user.email
        userPhone = user.phone_number
        userCarrier = user.phone_carrier

        if len(userEmail) > 0:
            logging.info("sent message to " + userEmail)
            #SendOneEmail(userEmail, subject, content)
            SendOneHTMLEmail(userEmail, subject, content)



        if len(userPhone) > 0 and len(userCarrier) > 0:
            SendOneHTMLEmail(ExtraMethods.getPhoneNumberEmail(userPhone, userCarrier), subject, content)
            #SendOneEmail(ExtraMethods.getPhoneNumberEmail(userPhone, userCarrier), subject, content)
            logging.info("sent message to " + userPhone)
