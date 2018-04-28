#!/usr/bin/python

import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

# Set the vehicle VIN in a memache key
mc.set('VIN', 'WBA3B9G59ENR92112')

print 'Vehicle VIN: ' + mc.get('VIN')
