import os
import logging
import cherrypy
   
import pprint
pp = pprint.PrettyPrinter(indent=4)
   
import infrastructure.loghandlers
   
import aquamonconfig
   
import interface.data
import interface.healthcheck
   
logger = logging.getLogger('aquamon')
   

####################################################
# configs paths
apiDocPath = '%s/../sphinx/_build/html' % os.path.dirname(__file__)
coveragePath = '%s/../test/coverage' % os.path.dirname(__file__)
unittestPath = '%s/../test/report.txt' % os.path.dirname(__file__)
docIndexPath = '%s/../test/index.html' % os.path.dirname(__file__)
uiIndexPath = '/opt/aquamon/'

Config = aquamonconfig.Config()

def setupLogs(logRootDir=None):
   infrastructure.loghandlers.setupLogging(logRootDir)

def setupRoutes(localUI=False, disableConfigLoader=False):
   Config.load()

   mapper = cherrypy.dispatch.RoutesDispatcher()
   
   ####################################################
   # url routes
   
   # healthcheck route
   mapper.connect('healthcheck',
                  '/healthcheck',
                  controller=interface.healthcheck.HealthcheckHandler)
  
   mapper.connect('data',
                  '/data',
                  controller=interface.data.DataHandler)
 
   conf = {
           #'/v3.0/docs/api': {
           #       'tools.staticdir.on': True,
           #       'tools.staticdir.dir': apiDocPath,
           #       'tools.staticdir.index': 'index.html'
           #},
           #'/v3.0/docs/coverage': {
           #       'tools.staticdir.on': True,
           #       'tools.staticdir.dir': coveragePath,
           #       'tools.staticdir.index': 'index.html'
           #},
           #'/v3.0/docs/unittests': {
           #       'tools.staticfile.on': True,
           #       'tools.staticfile.filename': unittestPath
           #},
           #'/v3.0/docs/index.html': {
           #       'tools.staticfile.on': True,
           #       'tools.staticfile.filename': docIndexPath
           #},
           '/': {
                 'request.dispatch': mapper
           },
   }

   if localUI:
      conf['/'] = {
                     'tools.staticdir.on': True,
                     'tools.staticdir.dir': uiIndexPath,
                     'tools.staticdir.index': 'index.html',
                  }
   
   
   return(conf)

