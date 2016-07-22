import sys
import os
sys.path.insert(0, 'external/cherrypy.zip')
sys.path.insert(0, 'external/six.zip')
sys.path.insert(0, 'external/routes.zip')
sys.path.insert(0, 'external/repoze.zip')

import cherrypy
import wsgiref.handlers 


scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
sys.path.append(scriptPath + '/lib/')

import application

app = cherrypy.tree.mount(None, '/', config=application.setupRoutes())
wsgiref.handlers.CGIHandler().run(app)

