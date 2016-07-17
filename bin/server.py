#!/usr/bin/python
import os
import sys
import argparse
import logging
import time

import cherrypy


import pprint
pp = pprint.PrettyPrinter(indent=4)

# account for where we live including the lib path
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
sys.path.append(scriptPath + '/../lib/')

import application
import background.monitor

logger = logging.getLogger('aquamon')

def parseArgs():
   parser = argparse.ArgumentParser(description='aquamon')
   parser.add_argument('--debug', action="store_true", dest="debug")

   parser.add_argument('-p', action="store", dest="port", default=80, help='Port to listen on')
   parser.add_argument('--ui', action="store_true", dest="localui", default=False, help='Enable local ui')

   args = parser.parse_args()
   return(args)

if __name__ == '__main__':
   args = parseArgs()

   # define a basic server config to use if not running in debug mode
   serverConfig={
      'engine.autoreload.on': False,
      #'engine.SIGHUP': None,
      #'engine.SIGTERM': None,

      'server.socket_host': '0.0.0.0',
      'server.thread_pool': 10,

      'log.screen' : False,
      'log.access_file': '/var/log/aquamon/access.log', # disable access logging
      'log.error_file': '/var/log/aquamon/error.log',
      'tools.log_tracebacks.on': True
   }

   # set the port based on args
   serverConfig['server.socket_port'] = int(args.port)

   # if we are running in debug mode, do a simple start
   application.setupLogs()
   logger.info('Started')

   # run a real config
   cherrypy.tree.mount(None, '/', config=application.setupRoutes(localUI=args.localui))
   cherrypy.config.update(serverConfig)

   mon = background.monitor.Monitor()
   mon.daemon = True
   mon.start()

   if hasattr(cherrypy.engine, 'signal_handler'):
      cherrypy.engine.signal_handler.set_handler('SIGTERM', listener=background.monitor.cleanup)
      cherrypy.engine.signal_handler.set_handler('SIGINT', listener=background.monitor.cleanup)

      cherrypy.engine.signal_handler.subscribe()

   try:
      cherrypy.engine.start()
      cherrypy.engine.block()
   finally:
      background.monitor.cleanup()

