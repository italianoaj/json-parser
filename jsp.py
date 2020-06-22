#!/usr/bin/python3
import json
import sys

if len(sys.argv)!=2:
    print("Error: syntax. jsp <file>")
    sys.exit()

try:
    fp = open(sys.argv[1],)
    fw = open("../sec/sorted_log.json", "w")
except:
    print("An error has occured")
    sys.exit()

okta = json.loads(fp.read())


for i in okta:
    info='"event":{"user":"'+i['actor']['displayName']+'","email_address":"'+i['actor']['alternateId']+'","ip_address":"'+i['client']['ipAddress']+'","state":"'+i['client']['geographicalContext']['state']+'","country":"'+i['client']['geographicalContext']['country']+'","outcome":"'+i['outcome']['result']+'","date":"'+i['published']+'"}\n'
    fw.write(info)

fp.close()
fw.close()
sys.exit()