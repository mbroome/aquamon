
import logging

import pprint
pp = pprint.PrettyPrinter(indent=4)

try:
   import model.ndbkeystore as keystoreModel
except:
   import model.httpkeystore as keystoreModel

logger = logging.getLogger('aquamon.' + __name__)

class Controller():
   def __init__(self, requestConfig={}):
      self.ks = keystoreModel.Model()

   def get(self, requestConfig={}):
      response = self.ks.get(requestConfig)

      return(response)

   def put(self, requestConfig={}):
      response = self.ks.put(requestConfig)
 
      return(response)

