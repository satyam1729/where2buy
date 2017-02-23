def cogcv(img):
    import httplib, urllib, base64,json
    string=''
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': 'cb61b5c2179546faa37990d0962cbccf', #change key
    }

    params = urllib.urlencode({
        # Request parameters
        'language': 'unk',
        'detectOrientation ': 'true',
    })

    img = open(img, 'rb').read()
    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/vision/v1.0/ocr?%s" % params, img, headers)
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
                    string=string+t+'+'    
        conn.close()
        return string
    except:
        return none   
