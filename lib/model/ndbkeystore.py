
from google.appengine.ext import ndb

class Keystore(ndb.Model):
   point = ndb.StringProperty()
   value = ndb.FloatProperty()
   date = ndb.DateTimeProperty(auto_now_add=True)

   @classmethod
   def query_point(self, ancestor_key):
      return(self.query(ancestor=ancestor_key).order(-self.date))


class Model():
   def get(self, requestConfig={}):
      response = []

      rec = Keystore.query(Keystore.point==requestConfig['point']).fetch()

      for row in rec:
         r = {'point': row.point, 'value': row.value, 'time': row.date.strftime("%s")}
         response.append(r)

      return(response)

   def put(self, requestConfig={}):
      response = {}

      for k in requestConfig:
         rec = Keystore(point=k, value=requestConfig[k])
         rec.put()

      response['status'] = 'done'
      return(response)

