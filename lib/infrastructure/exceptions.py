import logging
import time

logger = logging.getLogger('aquamon.' + __name__)

import pprint
pp = pprint.PrettyPrinter(indent=4)

# the base class all exceptions derive from
class BaseException(Exception):
   def __init__(self, message):
      super(BaseException, self).__init__(message)

   def to_json(self):
      return(self.message)

# lockerbox exceptions
class BucketAccessException(BaseException):
   def __init__(self, message):
      super(BucketAccessException, self).__init__(message)
      self.statuscode = 403

class BucketPermissionException(BaseException):
   def __init__(self, message):
      super(BucketPermissionException, self).__init__(message)
      self.statuscode = 403

class LockerboxKeyException(BaseException):
   def __init__(self, message):
      super(LockerboxKeyException, self).__init__(message)
      self.statuscode = 403

# consul exceptions
class ConsulConnectException(BaseException):
   def __init__(self, message):
      super(ConsulConnectException, self).__init__(message)
      self.statuscode = 500

class ConsulLookupException(BaseException):
   def __init__(self, message):
      super(ConsulLookupException, self).__init__(message)
      self.statuscode = 404

# security exceptions
class SecurityAccessException(BaseException):
   def __init__(self, message):
      super(SecurityAccessException, self).__init__(message)
      self.statuscode = 401

class ADConnectionException(BaseException):
   def __init__(self, message):
      super(ADConnectionException, self).__init__(message)
      self.statuscode = 500

class ADLoginException(BaseException):
   def __init__(self, message):
      super(ADLoginException, self).__init__(message)
      self.statuscode = 500

class GroupAccessException(BaseException):
   def __init__(self, message):
      super(GroupAccessException, self).__init__(message)
      self.statuscode = 403

# content validations exceptions
class ValidationException(BaseException):
   def __init__(self, message):
      super(ValidationException, self).__init__(message)
      self.statuscode = 500

# instance exceptions
class InstanceCreateException(BaseException):
   def __init__(self, message):
      super(InstanceCreateException, self).__init__(message)
      self.statuscode = 500

class InstanceDeleteException(BaseException):
   def __init__(self, message):
      super(InstanceDeleteException, self).__init__(message)
      self.statuscode = 500

class InstanceLookupException(BaseException):
   def __init__(self, message):
      super(InstanceLookupException, self).__init__(message)
      self.statuscode = 404

class MetaDataException(BaseException):
   def __init__(self, message):
      super(MetaDataException, self).__init__(message)
      self.statuscode = 500

class InstanceException(BaseException):
   def __init__(self, message):
      super(InstanceException, self).__init__(message)
      self.statuscode = 500

class SecurityGroupException(BaseException):
   def __init__(self, message):
      super(SecurityGroupException, self).__init__(message)
      self.statuscode = 500

class SecurityGroupRuleException(BaseException):
   def __init__(self, message):
      super(SecurityGroupRuleException, self).__init__(message)
      self.statuscode = 404

class ZoneException(BaseException):
   def __init__(self, message):
      super(ZoneException, self).__init__(message)
      self.statuscode = 500

class VolumeException(BaseException):
   def __init__(self, message):
      super(VolumeException, self).__init__(message)
      self.statuscode = 500

class InstanceTypeException(BaseException):
   def __init__(self, message):
      super(InstanceTypeException, self).__init__(message)
      self.statuscode = 500

class InstanceImageException(BaseException):
   def __init__(self, message):
      super(InstanceImageException, self).__init__(message)
      self.statuscode = 500

class InstanceNetworkException(BaseException):
   def __init__(self, message):
      super(InstanceNetworkException, self).__init__(message)
      self.statuscode = 500

# config exceptions
class ZuulException(BaseException):
   def __init__(self, message):
      super(ZuulException, self).__init__(message)
      self.statuscode = 500

class ConfigOptionException(BaseException):
   def __init__(self, message):
      super(ConfigOptionException, self).__init__(message)
      self.statuscode = 500

class RemoteAPIException(BaseException):
   def __init__(self, message):
      super(RemoteAPIException, self).__init__(message)
      self.statuscode = 500

class KeyLookupException(BaseException):
   def __init__(self, message):
      super(KeyLookupException, self).__init__(message)
      self.statuscode = 404

class LibrarianException(BaseException):
   def __init__(self, message):
      super(LibrarianException, self).__init__(message)
      self.statuscode = 500

