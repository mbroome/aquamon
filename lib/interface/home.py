
import cherrypy
import logging
import json
import urllib

import infrastructure.requestutils

logger = logging.getLogger('aquamon.' + __name__)

class HomeHandler(infrastructure.requestutils.DefaultHandler):
   def GET(self, **args):

      return('aquamon')
