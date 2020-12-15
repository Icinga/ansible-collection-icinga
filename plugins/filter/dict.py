from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

def prefix(d, prefix):
    ret = {}
    for key in d.keys():
        ret[prefix + key] = d[key]
    return ret

class FilterModule(object):
    def filters(self):
      return {
          # prefix
          'prefix': prefix,
      }
