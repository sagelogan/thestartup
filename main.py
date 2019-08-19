import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

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

# The signup page
class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        # ask for user type (venue, band, listener)
        # displays signup page for type of user
        # different user types will be asked for different info
        pass

# The home page for users of type venue
class VenueHomeHandler(webapp2.RequestHandler):
    def get(self):
        # display calendar of upcoming bookings and other stats
        # option to book/contact bands in area
        pass

# The home page for users of type band
class BandHomeHandler(webapp2.RequestHandler):
    def get(self):
        # display calendar of upcoming shows at venues and other stats
        # option to book at venues
        pass

# The home page for users of type listener
class ListenerHomeHandler(webapp2.RequestHandler):
    def get(self):
        # display venues and bands nearby using geolocation
        # show updates for favorite venues/bands
        # option to buy tickets, look up events at venues, bands
        pass

app = webapp2.WSGIApplication([
  ('/', MainPageHandler),
  ('/login', LoginHandler),
  ('/signup', SignUpHandler),
  ('/venue', VenueHomeHandler),
  ('/band', BandHomeHandler),
  ('/listener', ListenerHomeHandler),
  ('/venueprofile',VenueProfileHandler),
  ('/bandprofile', BandProfileHandler),
  ('/listenerprofile', ListenerProfileHandler),
])
