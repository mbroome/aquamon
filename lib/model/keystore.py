
from google.appengine.ext import ndb

class Keystore(ndb.Model):
   point = ndb.StringProperty()
   value = ndb.FloatProperty()
   date = ndb.DateTimeProperty(auto_now_add=True)

   @classmethod
   def query_point(self, ancestor_key):
      return(self.query(ancestor=ancestor_key).order(-self.date))

