import logging

import pprint
pp = pprint.PrettyPrinter(indent=4)

from infrastructure.loghandlers import audit

logger = logging.getLogger('cumulus3.' + __name__)

class InstanceObject():
   def __init__(self, config):
      self.config = config
      if self.config.has_key('instanceid'):
         self.remap()

   def remap(self):
      # now add all of self.config[] as properties to this object
      for k in self.config:
         self.__dict__[k] = self.config[k]
      if not self.config.has_key('instanceid'):
         raise('no instance id: %s' % self.config)

   def to_json(self):
      r = {}
      for k in self.config:
         if not k == '_id':
            r[k] = self.config[k]
      return(r)

   def __repr__(self):
      return('<InstanceObject id: %s>' %
              (
                 self.instanceid
              )
            )

class ResourceRecordSet():
   def __init__(self, recordset):
      self.data = []
      for rset in recordset:
         record = {'name': rset.name, 
                   'type': rset.type, 
                   'records': rset.resource_records, 
                   'aliaszone': rset.alias_hosted_zone_id,
                   'aliasdest': rset.alias_dns_name,
                   'ttl': rset.ttl}
         self.data.append(record)

#class AvailabilityZoneObject():
#   def __init__(self, zone):
#      self.data = zone


#class SecurityGroupObject():
#   def __init__(self, config):
#      self.config = config
#      self.remap()
#
#   def remap(self):
#      # now add all of self.config[] as properties to this object
#      for k in self.config:
#         self.__dict__[k] = self.config[k]
#
#   def __repr__(self):
#      return('<SecurityGroupObject id: %s>' %
#              (
#                 self.id
#              )
#            )

class UserLogObject():
   def __init__(self, config):
      self.config = config.copy()
      del(self.config['_id'])

      if self.config.has_key('userid'):
         self.remap()

   def remap(self):
      # now add all of self.config[] as properties to this object
      for k in self.config:
         self.__dict__[k] = self.config[k]

      if not self.config.has_key('userid'):
         raise('no user id: %s' % self.config)

   def __repr__(self):
      return('<UserLogObject id: %s>' %
              (
                 self.userid
              )
            )


#class VolumeObject():
#   def __init__(self, config):
#      self.config = config
#      self.remap()
#
#   def remap(self):
#      # now add all of self.config[] as properties to this object
#      for k in self.config:
#         self.__dict__[k] = self.config[k]
#
#   def __repr__(self):
#      return('<VolumeObject id: %s>' %
#              (
#                 self.id
#              )
#            )

class ElasticIPObject():
   def __init__(self, config):
      self.config = config
      self.remap()

   def remap(self):
      # now add all of self.config[] as properties to this object
      for k in self.config:
         self.__dict__[k] = self.config[k]

   def __repr__(self):
      return('<ElasticIPObject id: %s>' %
              (
                 self.id
              )
            )


