
import cherrypy
import logging
import json
import urllib

import infrastructure.requestutils

import controller.keystore

logger = logging.getLogger('aquamon.' + __name__)

class KeystorePointHandler(infrastructure.requestutils.DefaultHandler):
   def GET(self, **args):
      keystore = controller.keystore.Controller(args)
      r = keystore.get(args)

      response = {'status': 'success', 'data': r, 'message': None}

      return(json.dumps(response))

class KeystoreHandler(infrastructure.requestutils.DefaultHandler):
   def GET(self, **args):
      keystore = controller.keystore.Controller(args)
      r = keystore.get(args)

      response = {'status': 'success', 'data': r, 'message': None}

      return(json.dumps(response))

   def PUT(self, **args):
      # do our best to find the body of the request in whatever
      # form it was passed to us
      if args.has_key('body'):
         content = args['body']
      else:
         content = urllib.unquote_plus(cherrypy.request.body.read())
         if len(content) <= 0:
            for k in cherrypy.request.body_params:
               content = k
               break

      requestConfig = json.loads(content)

      keystore = controller.keystore.Controller(args)

      r = keystore.put(requestConfig)

      response = {'status': 'success', 'data': r, 'message': None}

      return(json.dumps(response))

