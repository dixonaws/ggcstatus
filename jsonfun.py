# jsonfun.py
# convert a Python dict to JSON
import json

dictCANmessages={}

dictCANmessages['version']='1.0'

jsonCANmessages=json.dumps(dictCANmessages)

print jsonCANmessages