import requests as req
import sys
import json

token = "1a2af3d66e856fb82eeaa392304976fe"
getUrl = "http://challenge.code2040.org/api/haystack"
postUrl = "http://challenge.code2040.org/api/haystack/validate"
reqkey = {"token":token}

request = req.post(getUrl,json=reqkey)

myJSON = json.loads(request.text)
print(myJSON)
needle = myJSON['needle']
haystack = myJSON['haystack']
position = -1
print("needle: " + needle)
print(haystack)
count = 0
for index in range(0,len(haystack),1):
    if(haystack[index] == needle):
        position = count
    count += 1
if (position == -1):
    print("this failed")
    sys.exit()
else:

    postKey = {"token":token, "needle": position}
    print("entry: " + haystack[position])
    print("position: " + str(position))
    postReq = req.post(postUrl, json=postKey)
    print(postReq.text)





