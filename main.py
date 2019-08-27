import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# The main page of the app
class MainPageHandler(webapp2.RequestHandler):
  def get(self):
      # check if user logged in
      # if logged in, redirect to home page for user type (venue, band, listener)
      # else show welcome page with option to login

      # render the main page template
      main_template = the_jinja_env.get_template('/templates/mainpage.html')
      self.response.write(main_template.render())

# The login page
class LoginHandler(webapp2.RequestHandler):
    def get(self):
        # prompt user for login credentials
        # option for signup (redirects to signup page)

        # render the login page template
        login_template = the_jinja_env.get_template('/templates/login.html')
        self.response.write(login_template.render())

class NoUserHandler(webapp2.RequestHandler):
    def get(self):
        login_url = users.create_login_url('/')
        self.redirect(login_url)

# The signup intro page
class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        # ask for user type (venue, band, listener)
        # redirects to signup page for type of user
        # different user types will be asked for different info
        # handlers for specific signup pages can be found under user type section

        # render the signup page template
        signup_template = the_jinja_env.get_template('/templates/signup.html')
        self.response.write(signup_template.render())

####################
# User type: Venue #
####################

# add commenting and description of class Venue here
class Venue(ndb.Model):
    namer = ndb.StringProperty(required = True)
    location =  ndb.StringProperty(required = True)
    contact = ndb.StringProperty(required = True)
    genre = ndb.StringProperty(required = False)
    linktomusic = genre = ndb.StringProperty(required = False)
    concerts = genre = ndb.StringProperty(required = False)

# The signup page for users of type venue
class VenueSignUpHandler(webapp2.RequestHandler):
    def get(self):
        # prompt for venue name, location, size
        # list of info on venueapp design doc

        # render the venue signup page
        venuesignup_template = the_jinja_env.get_template('/templates/venuesignup.html')
        self.response.write(venuesignup_template.render())

# The home page for users of type venue
class VenueHomeHandler(webapp2.RequestHandler):
    def get(self):
        # display calendar of upcoming bookings and other stats
        # option to book/contact bands in area

        # render the venue home page
        venuehome_template = the_jinja_env.get_template('/templates/venuehome.html')
        self.response.write(venuehome_template.render())

# The profile page for users of type venue
class VenueProfileHandler(webapp2.RequestHandler):
    # display the profile page of current user (type venue)

    # render the venue profile page
    venueprofile_template = the_jinja_env.get_template('/templates/venueprofile.html')
    self.response.write(venueprofile_template.render())

###################
# User type: Band #
###################

# add commenting and description of class Band here
class Band(ndb.Model):
    namer = ndb.StringProperty(required = True)
    contact = ndb.StringProperty(required = True)
    capacity = genre = ndb.StringProperty(required = False)
    accessibility = genre = ndb.StringProperty(required = False)
    venuetype = genre = ndb.StringProperty(required = False)

# The signup page for users of type band
class BandSignUpHandler(webapp2.RequestHandler):
    def get(self):
        # prompt for band name, genre, link to music
        # list of info on venueapp design doc

        # render the band signup page
        bandsignup_template = the_jinja_env.get_template('/templates/bandsignup.html')
        self.response.write(bandsignup_template.render())

# The home page for users of type band
class BandHomeHandler(webapp2.RequestHandler):
    def get(self):
        # display calendar of upcoming shows at venues and other stats
        # option to book at venues
        # option to 'create a tour' and select locations (venues will be suggested)

        # render the band home page
        bandhome_template = the_jinja_env.get_template('/templates/bandhome.html')
        self.response.write(bandhome_template.render())

# The profile page for users of type band
class BandProfileHandler(webapp2.RequestHandler):
    # display the profile page of current user (type band)

    # render the band profile page
    bandprofile_template = the_jinja_env.get_template('/templates/bandprofile.html')
    self.response.write(bandprofile_template.render())

#######################
# User type: Listener #
#######################

# add commenting and description of class Listener here
class Listener(ndb.Model):
    namer = ndb.StringProperty(required = True)
    contact = ndb.StringProperty(required = True)

# The signup page for users of type listener
class ListenerSignUpHandler(webapp2.RequestHandler):
    def get(self):
        # prompt for username, favorite venues, favorite bands, etc
        # list of info on venueapp design doc

        # render the listener signup page
        listenersignup_template = the_jinja_env.get_template('/templates/listenersignup.html')
        self.response.write(listenersignup_template.render())

# The home page for users of type listener
class ListenerHomeHandler(webapp2.RequestHandler):
    def get(self):
        # display venues and bands nearby using geolocation
        # show updates for favorite venues/bands
        # option to buy tickets, look up events at venues, bands

        # render the listener home page
        listenerhome_template = the_jinja_env.get_template('/templates/listenerhome.html')
        self.response.write(listenerhome_template.render())

# The profile page for users of type Listener
class ListenerProfileHandler(webapp2.RequestHandler):
    # display the profile page of current user (type listener)

    # render the band profile page
    listenerprofile_template = the_jinja_env.get_template('/templates/listenerprofile.html')
    self.response.write(listenerprofile_template.render())


app = webapp2.WSGIApplication([
  ('/', MainPageHandler),
  ('/login', LoginHandler),
  ('/nouser', NoUserHandler),
  ('/signup', SignUpHandler),
  # venue
  ('/signup/venue', SignupVenueHandler),
  ('/venue', VenueHomeHandler),
  ('/venue/profile', VenueProfileHandler),
  # band
  ('/signup/band', BandSignUpHandler),
  ('/band', BandHomeHandler),
  ('/band/profile', BandProfileHandler),
  # listener
  ('/signup/listener', ListenerSignUpHandler),
  ('/listener', ListenerHomeHandler),
  ('/listener/profile', ListenerProfileHandler),
])
