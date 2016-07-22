
import logging
from google.appengine.ext import ndb


import pprint
pp = pprint.PrettyPrinter(indent=4)

from model.keystore import Keystore

logger = logging.getLogger('aquamon.' + __name__)

class Controller():
   def __init__(self, requestConfig={}):
      pass
   #   application.Config = cumulusconfig.Config()

   def get(self, requestConfig={}):
      response = []

      rec = Keystore.query(Keystore.point==requestConfig['point']).fetch()

      #pp.pprint(rec)
      #logger.info(rec)
      for row in rec:
         pp.pprint(row)
         r = {'point': row.point, 'value': row.value, 'time': row.date.strftime("%s")}
         response.append(r)


      return(response)

   def put(self, requestConfig={}):
      response = {}
      pp.pprint(requestConfig)

      for k in requestConfig:
         pp.pprint(k)
         rec = Keystore(point=k, value=requestConfig[k])
         rec.put()

      response['bob'] = 'test'
      return(response)

