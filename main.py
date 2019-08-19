import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Venue(ndb.Model):
    namer = ndb.StringProperty(required = True)
    location =  ndb.StringProperty(required = True)
    contact = ndb.StringProperty(required = True)
    genre = ndb.StringProperty(required = False)
    linktomusic = genre = ndb.StringProperty(required = False)
    concerts = genre = ndb.StringProperty(required = False)

class Band(ndb.Model):
    namer = ndb.StringProperty(required = True)
    contact = ndb.StringProperty(required = True)
    capacity = genre = ndb.StringProperty(required = False)
    accessibility = genre = ndb.StringProperty(required = False)
    venuetype = genre = ndb.StringProperty(required = False)

class Listener(ndb.Model):
    namer = ndb.StringProperty(required = True)
    contact = ndb.StringProperty(required = True)

# The main page of the app
class MainPageHandler(webapp2.RequestHandler):
  def get(self):
      # check if user logged in
      # if logged in, redirect to home page for user type (venue, band, listener)
      # else show login page
      main_template = the_jinja_env.get_template('/templates/mainpage.html')
      self.response.write(main_template.render())

# The login page
class LoginHandler(webapp2.RequestHandler):
    def get(self):
        # prompt user for login credentials
        # option for signup (redirects to signup page)
        pass

# The signup intro page
class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        # ask for user type (venue, band, listener)
        # redirects to signup page for type of user
        # different user types will be asked for different info
        pass

####################
# User type: Venue #
####################

# The signup page for users of type venue
class VenueSignUpHandler(webapp2.RequestHandler):
    def get(self):
        # prompt for venue name, location, size
        # list of info on venueapp design doc
        pass

# The home page for users of type venue
class VenueHomeHandler(webapp2.RequestHandler):
    def get(self):
        # display calendar of upcoming bookings and other stats
        # option to book/contact bands in area
        pass

# The profile page for users of type venue
class VenueProfileHandler(webapp2.RequestHandler):
    pass

###################
# User type: Band #
###################

# The signup page for users of type band
class BandSignUpHandler(webapp2.RequestHandler):
    def get(self):
        # prompt for band name, genre, link to music
        # list of info on venueapp design doc
        pass

# The home page for users of type band
class BandHomeHandler(webapp2.RequestHandler):
    def get(self):
        # display calendar of upcoming shows at venues and other stats
        # option to book at venues
        # option to 'create a tour' and select locations (venues will be suggested)
        pass

# The profile page for users of type band
class BandProfileHandler(webapp2.RequestHandler):
    pass

#######################
# User type: Listener #
#######################

# The signup page for users of type listener
class ListenerSignUpHandler(webapp2.RequestHandler):
    def get(self):
        # prompt for username, favorite venues, favorite bands, etc
        # list of info on venueapp design doc
        pass

# The home page for users of type listener
class ListenerHomeHandler(webapp2.RequestHandler):
    def get(self):
        # display venues and bands nearby using geolocation
        # show updates for favorite venues/bands
        # option to buy tickets, look up events at venues, bands
        pass

# The profile page for users of type Listener
class ListenerProfileHandler(webapp2.RequestHandler):
    pass

app = webapp2.WSGIApplication([
  ('/', MainPageHandler),
  ('/login', LoginHandler),
  ('/signup', SignUpHandler),
  # venue
  ('/signup/venue', SignupVenueHandler),
  ('/venue', VenueHomeHandler),
  ('/venue/profile',VenueProfileHandler),
  # band
  ('/signup/band', BandSignUpHandler),
  ('/band', BandHomeHandler),
  ('/band/profile', BandProfileHandler),
  # listener
  ('/signup/listener', ListenerSignUpHandler),
  ('/listener', ListenerHomeHandler),
  ('/listener/profile', ListenerProfileHandler),
])
