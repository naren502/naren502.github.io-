# Copyright 2012 Digital Inspiration
# http://www.labnol.org/

import os
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        
    q = 'index.html'
    app = webapp2.WSGIApplication([('/', MainPage)])

    path = os.path.join (os.path.dirname (__file__), q)
    self.response.headers ['Content-Type'] = 'text/html'
    self.response.out.write (template.render (path, {}))

#def main ():
#  application = webapp.WSGIApplication ([('/(.*html)?', MainHandler)], debug=True)
#  util.run_wsgi_app (application)
#
#if __name__ == '__main__':
#  main ()
