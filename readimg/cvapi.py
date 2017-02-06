import httplib, urllib, base64,json

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'cb61b5c2179546faa37990d0962cbccf',
}

params = urllib.urlencode({
    # Request parameters
    'language': 'unk',
    'detectOrientation ': 'true',
})

data = open('r.jpg', 'rb').read()
conn = httplib.HTTPSConnection('api.projectoxford.ai')
conn.request("POST", "/vision/v1.0/ocr?%s" % params, data, headers)
response = conn.getresponse()
data = response.read()
d=json.loads(data)
jsonr=d['regions']
for item in jsonr:
    jsonl1=item['lines']
    for item1 in jsonl1:
        jsonl2=item1['words']
        for item2 in jsonl2:
            t=item2['text']
            print(t)
conn.close()
