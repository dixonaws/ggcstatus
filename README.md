# ggcstatus
Long running Lambda function to report basic connectivity status to IoT Cloud every 5 seconds. 
Part of the connectedcar-v2 package. Publishes status every 5 seconds to the "connectedcar-v2/vehicles" 
topic in your AWS account. Your Greengrass group must be configured with a subscription to publish 
from this Lambda to the IoT Cloud.

Note that the project directory must include the following 
greengrasssdk directories in order to run the program or deploy
 to Lambda using deploy.sh. You can download the SDK from the AWS IoT console,
 and find the directories in the aws_greengrass_core_sdk/examples/HelloWorld/greengrassHelloWorld folder
- greengrasssdk/
- greengrass_common/
- greengrass_ipc_python_sdk/ 


