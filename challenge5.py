#prefix is a string
#array is String array[]
#return an array containing only the strings that do not start
#with the prefix

import requests as req
import sys
import json
import iso8601 as iso
import datetime
import re
token = "1a2af3d66e856fb82eeaa392304976fe"
getUrl = "http://challenge.code2040.org/api/dating"
postUrl = "http://challenge.code2040.org/api/dating/validate"
reqkey = {"token":token}

request = req.post(getUrl,json=reqkey)

myJSON = json.loads(request.text)
datestamp = myJSON['datestamp']
interval = myJSON['interval']
print("datestamp: " + datestamp)
date = iso.parse_date(datestamp)
change = datetime.timedelta(seconds=interval)
date += change
print(date.isoformat())
postDate = date.isoformat()
postDate = postDate[0:-6] + "Z"

postKey = {"token":token, "datestamp": postDate}
postReq = req.post(postUrl, json=postKey)
print(postReq.text)





