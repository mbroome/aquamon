import os
import logging
import cherrypy

import pprint
pp = pprint.PrettyPrinter(indent=4)

import interface.keystore
import interface.home

logger = logging.getLogger('aquamon')

mapper = cherrypy.dispatch.RoutesDispatcher()


def setupRoutes():
   mapper.connect('keystore',
                  '/keystore/{point}',
                  controller=interface.keystore.KeystorePointHandler)

   mapper.connect('keystore',
                  '/keystore',
                  controller=interface.keystore.KeystoreHandler)

   mapper.connect('home',
                  '/',
                  controller=interface.home.HomeHandler)

   conf = {
           '/': {
                 'request.dispatch': mapper
           },
   }


   return(conf)

