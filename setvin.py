#!/usr/bin/python

import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

# open the ccdtw configuration file, read the VIN there, and close
fileVinConfig=open('/etc/ccdtw/vehicle_vin.conf', 'r')

strVin=fileVinConfig.read()
fileVinConfig.close()


print 'ccdtw configuration: /etc/ccdtw/vehicle_vin.conf has VIN: ' + strVin 

# Set the vehicle VIN in a memache key
mc.set('VIN', strVin)

# Retrieve the vehicle VIN from memcache
print 'Vehicle VIN: ' + mc.get('VIN')

