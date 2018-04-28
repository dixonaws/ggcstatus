# ggcstatus
# https://github.com/dixonaws/ggcstatus
#

# ggcstatus.py
# Publish to topic <vehicle_vin>/ggcstatus using Greengrass core sdk
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


# Creating a greengrass core sdk client
client = greengrasssdk.client('iot-data')

# Retrieving platform information to send from Greengrass Core
my_platform = platform.platform()


# When deployed to a Greengrass core, this code will be executed immediately
# as a long-lived lambda function (must be cionfigured in the Greengrass Group to
# run as a long-lived function.  The code will enter the infinite while loop
# below. If you execute a 'test' on the Lambda Console, this test will fail by hitting the
# execution timeout of three seconds.  This is expected as this function never returns
# a result.

def send_status():
    strEpochTime=str(int(time.time()))
    strVehicleVin='WBA3B9G59ENR92112'
    strTopic = 'ccdtw/' + strVehicleVin + '/ggcstatus'
    strMessage='{ "time": "' + strEpochTime + '", "vehicle_vin":"' + strVehicleVin + '", "platform":"' + my_platform + '"}'

    print 'I am going to publish the following message: ' + strMessage
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
    return