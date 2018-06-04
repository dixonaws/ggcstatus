# ggcstatus
# https://github.com/dixonaws/ggcstatus
#

# ggcstatus.py
# Publish to topic ccdtw/ggcstatus using Greengrass core sdk
# This lambda function will retrieve underlying platform information and send
# a status message along with the platform information to the topic <vehicle_vin>/ggcstatus
# The function will sleep for five seconds, then repeat.  Since the function is
# long-lived it will run forever when deployed to a Greengrass core.  The handler
# will be invoked if run from the command line

import greengrasssdk
import platform
from threading import Timer
import time
import json
import time
import datetime
import socket
import memcache
import os

# Create a greengrass core sdk client
client = greengrasssdk.client('iot-data')

# Retrieving platform information to send from Greengrass Core
# open the ccdtw configuration file, read the VIN there, and close
fileVinConfig=open('/etc/ccdtw/vehicle_vin.conf', 'r')
strVehicleVin=fileVinConfig.read()
fileVinConfig.close()

strPlatform = platform.platform()

strStatus="Greengrass Core connected"

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
strIpAddress=str(s.getsockname()[0])

strGgcVersion="1.5.0"

# set the IoT topic where messages will be published
strTopic = 'connectedcar-v2/vehicles'

# When deployed to a Greengrass core, this code will be executed immediately
# as a long-lived lambda function (must be configured in the Greengrass Group to
# run as a long-lived function.  The code will enter the infinite while loop
# below. If you execute a 'test' on the Lambda Console, this test will fail by hitting the
# execution timeout of three seconds.  This is expected as this function never returns
# a result.

def send_status():
    strEpochTime=str(int(time.time()))

    try:
        strMessage='{  "messageType": "ggcstatus", "time": "' + strEpochTime + '", "vin":"' + strVehicleVin + '", "platform":"' + strPlatform + '", "ggc_version":"' + strGgcVersion +'", "ip_address": "' + strIpAddress + '", "status": "' + strStatus + '"}'
    except TypeError:
        # we'll get this error if memcache is not installed (e.g., we are testing in the Lambda console)
        strMessage = '{ "time": "' + strEpochTime + '", "vehicle_vin":"<testing>", "platform":"' + strPlatform + '"}'

    print 'I am going to publish the following message ( ' + strMessage + ') to topic ' + strTopic
    client.publish(topic=strTopic, payload=strMessage)

    # Asynchronously schedule this function to be run again in 5 seconds
    Timer(5, send_status).start()

# Start executing the function above
send_status()

# This is a dummy handler and will not be invoked
# Instead the code above will be executed in an infinite loop for our example
def function_handler(event, context):
    return

def lambda_handler(event, context):
    try:
        return 'Publishing message from host ' + strVehicleVin + ', (platform: ' + strPlatform + ')'
    except TypeError:
        return 'Publishing message from host <testing>, (platform: ' + strPlatform + ')'

