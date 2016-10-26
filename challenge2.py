import requests as req
import sys
import json

token = "1a2af3d66e856fb82eeaa392304976fe"
getUrl = "http://challenge.code2040.org/api/reverse"
postUrl = "http://challenge.code2040.org/api/reverse/validate"
reqkey = {"token":token}

request = req.post(getUrl,json=reqkey)
origString = request.text
revstring = ""

for index in range(len(origString),-1,-1):
    revString += origString[index]
postkey = {"token":token,"string":revString}
postRequest = req.post(postUrl,json=postKey}
print(postRequest)




