import os
import sys
import json
import base64
import threading
import logging
import time
import RPi.GPIO as GPIO

import pprint
pp = pprint.PrettyPrinter(indent=4)

from infrastructure.exceptions import *

from aquamonconfig import config as Config
import background.readswitch
import background.readtemp
import infrastructure.httpreq

logger = logging.getLogger('aquamon.' + __name__)

interval = 300

class Monitor(threading.Thread):
   def __init__(self):
      self.threadName = 'Monitor'

      self.req = infrastructure.httpreq.HTTPReq()
      self.probes = {}
      self.probes['readswitch'] = background.readswitch.Check()
      self.probes['readtemp'] = background.readtemp.Check()

      threading.Thread.__init__(self, name=self.threadName)

   def run(self):
      logger.info('starting the monitor run loop: %s' % self.threadName)

      while True:
         data = []
         for monitor in Config.config['monitor']:
            response = {}
            if self.probes.has_key(Config.config['monitor'][monitor]['function']) and not Config.config['monitor'][monitor].has_key('disabled'):
               try:
                  response = self.probes[Config.config['monitor'][monitor]['function']].check(monitor, Config.config['monitor'][monitor])
               except Exception, e:
                  pp.pprint(e)

               #pp.pprint(response)
               data.append(response)
         self.post(data)
         time.sleep(interval)

   def post(self, data):
      url = 'https://aquamon-1376.appspot.com/keystore'
      pp.pprint(data)

      request = {}
      for rec in data:
         request[rec['point']] = rec['value']
      pp.pprint(request)
      r = self.req.put(url, json.dumps(request))
      pp.pprint(r)

def cleanup():
   print 'cleanup!'
   GPIO.cleanup()
   os._exit(True)


