# pylint: skip-file
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


def prefix(d, prefix):
    if type(d) is dict:
        ret = {}
        for key in d.keys():
            ret[prefix + key] = d[key]
        return ret
    elif type(d) is list:
        ret = []
        for item in d:
            ret.append(prefix + item)
        return ret
    else:
        return False


class FilterModule(object):
    def filters(self):
        return {
            # prefix
            'prefix': prefix,
        }
