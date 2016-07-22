import json

import infrastructure.httpreq

class Model():
   def __init__(self):
      self.req = infrastructure.httpreq.HTTPReq()
      self.url = 'https://aquamon-1376.appspot.com/keystore/'

   def get(self, requestConfig={}):
      response = []

      rec = self.req.get(self.url + requestConfig['point'])
      if rec['status'] == 200:
         response = json.loads(rec['content'])

      return(response)

   def put(self, requestConfig={}):
      response = {}


      response['status'] = 'done'
      return(response)

