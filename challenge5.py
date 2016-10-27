import requests as req
import sys
import json
import iso8601 as iso
import datetime

token = "1a2af3d66e856fb82eeaa392304976fe"
getUrl = "http://challenge.code2040.org/api/dating"
postUrl = "http://challenge.code2040.org/api/dating/validate"
reqkey = {"token":token}

request = req.post(getUrl,json=reqkey)
myJSON = json.loads(request.text)

datestamp = myJSON['datestamp']
interval = myJSON['interval']
#creates a datetime object and stores in date
date = iso.parse_date(datestamp)
change = datetime.timedelta(seconds=interval)
#add my change in time to my date object
date += change
#write my date object as a string
postDate = date.isoformat()
#convert it to the correct format for the respose
postDate = postDate[0:-6] + "Z"

postKey = {"token":token, "datestamp": postDate}
postReq = req.post(postUrl, json=postKey)
print(postReq.text)





