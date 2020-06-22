#!/usr/bin/python3
import json
import sys

if len(sys.argv)!=2:
    print("Error: syntax. jsp <file>")
    sys.exit()

print(sys.argv[1])

try:
    fp = open(sys.argv[1],)
except:
    print("An error has occured")
    sys.exit()

okta = json.loads(fp.read())

for i in okta:
    print(i['actor']['displayName']+" "+i['actor']['alternateId']+" "+i['client']['ipAddress']+" "+i['client']['geographicalContext']['state']+" "+i['client']['geographicalContext']['country']+" "+i['outcome']['result']+" "+i['published'])

fp.close()
sys.exit()