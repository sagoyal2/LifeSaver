#This file allows us to import modules that
#wouldn't otherwise be accessible in App Engine
#including some Google APIs

# appengine_config.py
from google.appengine.ext import vendor

# Add any libraries install in the "lib" folder.
vendor.add('lib')
