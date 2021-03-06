from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import urllib
import json
import base64
from cvapi import cogcv
from flipkart import flipkartsearch
from amazon import bing_search
@csrf_exempt
def detect(request):
	# initialize the data dictionary to be returned by the request
	data = {"success": False}
	#reqd = {"got": "none"}
	img='readimg/image.png'.decode('base64')
	# check to see if this is a post request
	if request.method == "POST":
		# check to see if an image was uploaded
		if request.FILES.get("image", None) is not None:
			# grab the uploaded image
			img = _grab_image(stream=request.FILES["image"])

		# otherwise, assume that a URL was passed in
		else:
			# grab the URL from the request
			url = request.POST.get("url", None)

			# if the URL is None, then return an error
			if url is None:
				data["error"] = "No URL provided."
				return JsonResponse(data)

			# load the image and convert
			img = _grab_image(url=url)

		# update the data dictionary
		
		text=cogcv('imagedata.jpg')
		data = {"text": text}
		if text	is None:
			return JsonResponse(data)		
		data["success"] = True
		tup=flipkartsearch(text)
		data['title']=tup[1]
		data['amount']=tup[2]
		data['curr']=tup[3]
		data['link']=tup[4]
		data['amazonlink']=bing_search(text+'amazon')

	# return a JSON response
	return JsonResponse(data)
	#return JsonResponse(reqd)
def _grab_image(stream=None, url=None):
	# if the path is not None, then load the image from disk
	
	# otherwise, the image does not reside on disk	
		# if the URL is not None, then download the image
	if url is not None:
		resp = urllib.urlopen(url)
		data = resp.read()

		# if the stream is not None, then the image has been uploaded
	elif stream is not None:
		data = stream.read()
	f = open("imagedata.jpg", "wb")	
	f.write(data)	
	f.close()
	return data
		# convert the image to a NumPy array and then read it into
		# OpenCV format
	# return the image
	