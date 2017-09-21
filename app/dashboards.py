import requests
import yaml
import os
import sys
import time
import json

y=None
url=None

try:
    y=os.environ["DASHBOARDS"]
except:
    print "DASHBOARDS env variable is not defined"
    sys.exit(1)

try:
    grafana=os.environ["GRAFANA"]
except:
    grafana="http://admin:admin@grafana:3000"

try:
    dashboards=y.split(",")
except Exception as e:
    print "ERROR: "+str(e.message)
    sys.exit(1)

template="""
{
  "dashboard": %DASHBOARD%,
  "message": "",
  "overwrite":false
}
"""

def render(data):
    return template.replace("%DASHBOARD%",data)


def registerDB():
    postURL=grafana+"/api/datasources"
    print postURL
    data={
        "name":"influxdb",
        "type":"influxdb",
        "url":"http://influxdb:8086",
        "access":"proxy",
        "basicAuth": False,
        "isDefault": True,
        "database":"cadvisor"
    }
    requests.post(postURL,data=json.dumps(data),headers={"Content-Type": "application/json"},timeout=5)
    #print response.content

def post(dashboard):
    postURL=grafana+"/api/dashboards/db"
    response=requests.post(postURL,data=dashboard,headers={"Content-Type": "application/json"},timeout=5)
    if response.status_code!=200:
        print "WARNING: Failed to import dashboard :"+str(response.content)
    
while True:
    registerDB()
    for url in dashboards:
        try:
            response=requests.get(url.strip())
            dashboard=render(response.content)
            try:
                post(dashboard)
            except  Exception as e:
                print "WARNING: problem with "+str(grafana)+":"+ str(e.message)
        except  Exception as e:
            print "WARNING: problem with "+str(url)+":"+ str(e.message)
    time.sleep(60)