import webapp2

from tubetapes import MAIN_ROUTES

app = webapp2.WSGIApplication(MAIN_ROUTES, debug=True)