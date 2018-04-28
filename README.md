# ggcstatus
Long running Lambdas function to report basic connectivity status to IoT Cloud.

Note that the project directory must include the following 
greengrasssdk directories in order to run the program or deploy
 to Lambda using deploy.sh. You can download the SDK from the AWS IoT console,
 and find the directories in the aws_greengrass_core_sdk/examples/HelloWorld/greengrassHelloWorld folder
- greengrasssdk/
- greengrass_common/
- greengrass_ipc_python_sdk/ 