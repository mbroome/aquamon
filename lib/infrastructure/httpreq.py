import urllib
import urllib2
import urlparse
import socket
import time
import json
import sys
import logging

logger = logging.getLogger(__name__)

import pprint
pp = pprint.PrettyPrinter(indent=4)

# we need to make sure we don't follow redirects so build a new opener
class NoRedirection(urllib2.HTTPErrorProcessor):
   def http_response(self, request, response):
      return response

   https_response = http_response


# by default, urllib2 only deals with GET and POST
# so we subclass it and make it handle other methods
class RequestWithMethod(urllib2.Request):
    def __init__(self, url, method, data=None, headers={}, origin_req_host=None, unverifiable=False):
        self._method = method

        # build up a copy of the full request
        u = urlparse.urlparse(url)
        self._the_request = "%s %s HTTP/1.1\n" % (method, u.path)
        for h in headers:
           self._the_request += "%s: %s\n" % (h, headers[h])
        self._the_request += "\n"
        if data:
           self._the_request += data

        urllib2.Request.__init__(self, url, data, headers, origin_req_host, unverifiable)

    def get_method(self):
        if self._method:
            return self._method
        else:
            return urllib2.Request.get_method(self) 

class HTTPReq():
   def __init__(self, timeout=10):
      self.timeout = timeout
      self.AcceptTypes = {}
      self.AcceptTypes['json'] = 'application/json'
      self.AcceptTypes['xml'] = 'application/xml'
      self.AcceptTypes['text'] = 'text/plain'
      self.AcceptTypes['csv'] = 'text/csv'

   def accept2type(self, accept):
      for k in self.AcceptTypes:
         try:
            if self.AcceptTypes[k] == accept:
               return(k)
         except:
            pass
      return('json')

   def _query(self, req):
      start = end = 0
      code = -1
      rheaders = {}
      ret = None
      retheaders = None

      try:
         opener = urllib2.build_opener(NoRedirection)
      except Exception, e:
         logger.exception(e)
         sys.exit(0)

      try:
         start = time.time()
         response = opener.open(req, timeout=self.timeout)

         end = time.time()
         code = response.code
         retheaders = response.info()
      except urllib2.URLError, e:
         if hasattr(e, 'reason'):
            logger.exception('url: %s error: %s' % (req, e))
            ret = str(e.reason)
         else:
            code = e.code
            retheaders = e.info()
            ret = e.read()
         raise e
      except IOError, e:
         if hasattr(e, 'reason'):
            reason = e.reason
         elif hasattr(e, 'code'):
            code = e.code
            rheaders = e.info()
         else:
            logger.exception(e)
         raise e

      try:
         ret = response.read()
      except:
         pass

      try:
         for r in retheaders.items():
            rheaders[r[0].lower()] = r[1]
      except:
         pass

      return dict(content=ret, status=code, headers=rheaders, speed=(end - start), request=req._the_request)

   def get(self, url, data=None, headers={}, type=None):
      req = None
      try:
         if self.AcceptTypes[type]:
            headers['Accept'] = self.AcceptTypes[type]
            req = RequestWithMethod(url, 'GET', headers=headers)
      except:
         req = RequestWithMethod(url, 'GET', headers=headers)

      return(self._query(req))

   def post(self, url, data, headers={}, type=None):
      req = None
      try:
         if self.AcceptTypes[type]:
            headers['Accept'] = self.AcceptTypes[type]
            req = RequestWithMethod(url, 'POST', data=data, headers=headers)
      except Exception, e:
         req = RequestWithMethod(url, 'POST', data=data, headers=headers)
         #logger.exception(e)

      return(self._query(req))

   def delete(self, url, data=None, headers={}, type=None):
      req = None
      try:
         if self.AcceptTypes[type]:
            headers['Accept'] = self.AcceptTypes[type]
            req = RequestWithMethod(url, 'DELETE', headers=headers)
      except:
         req = RequestWithMethod(url, 'DELETE', headers=headers)

      return(self._query(req))

   def put(self, url, data, headers={}, type=None):
      req = None
      try:
         if self.AcceptTypes[type]:
            headers['Accept'] = self.AcceptTypes[type]
            req = RequestWithMethod(url, 'PUT', data=data, headers=headers)
      except:
         req = RequestWithMethod(url, 'PUT', data=data, headers=headers)

      return(self._query(req))


