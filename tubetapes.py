import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
  def get(self):
    template = jinja_environment.get_template('main_pages/index.html')
    self.response.out.write(template.render())

class AboutPage(webapp2.RequestHandler):
  def get(self):
    template = jinja_environment.get_template('main_pages/about.html')
    self.response.out.write(template.render())

MAIN_ROUTES = [
  ('/', MainPage),
  ('/about', AboutPage)
]