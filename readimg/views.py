from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import urllib
import json
@csrf_exempt
def detect(request):
	# initialize the data dictionary to be returned by the request
	data = {"success": False}

	# check to see if this is a post request
	if request.method == "POST":
		# check to see if an image was uploaded
		if request.FILES.get("image", None) is not None:
			# grab the uploaded image
			image = _grab_image(stream=request.FILES["image"])

		# otherwise, assume that a URL was passed in
		else:
			# grab the URL from the request
			url = request.POST.get("url", None)

			# if the URL is None, then return an error
			if url is None:
				data["error"] = "No URL provided."
				return JsonResponse(data)

			# load the image and convert
			image = _grab_image(url=url)

		# update the data dictionary
		data["success"] = True

	# return a JSON response
	return JsonResponse(data)

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

	return data
		# convert the image to a NumPy array and then read it into
		# OpenCV format
	# return the image
	