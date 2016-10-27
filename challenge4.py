import requests as req
import sys
import json

token = "1a2af3d66e856fb82eeaa392304976fe"
getUrl = "http://challenge.code2040.org/api/prefix"
postUrl = "http://challenge.code2040.org/api/prefix/validate"
reqkey = {"token":token}

request = req.post(getUrl,json=reqkey)

myJSON = json.loads(request.text)
prefix = myJSON['prefix']
array = myJSON['array']

print("prefix: " + prefix)
print(array)
postArray = []

for index in range(0,len(array),1):
    if(array[index].count(prefix) == 0):
        postArray.append(array[index])

postKey = {"token":token, "array": postArray}
print(postArray)
postReq = req.post(postUrl, json=postKey)
print(postReq.text)





