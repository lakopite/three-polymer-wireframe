
from datetime import datetime
import json
import os
import boto3
from botocore.client import Config

s3 = boto3.resource('s3')

settings = {
	'site-bucket': 'arup-model-test-data',
	'data-folder': 'three-polymer-wireframe'
}

mybucket = s3.Bucket(settings['site-bucket'])

class Error(Exception):
  pass

class WrongNameError(Error):
  pass

class MissingModelInfoKeysError(Error):
  pass

class InvalidUnitsError(Error):
  pass

class MissingPayloadKeysError(Error):
  pass

class EmptyVerticesError(Error):
  pass

class EmptyMetadataError(Error):
  pass

class AlreadyInBucketError(Error):
  pass

def validateJson(postData):
    #postData defined in app.py
	try:
		#must insert wrong name error? or just on front-end?
		if "modelInformation" not in postData or "payload" not in postData:
			raise KeyError
		if "units" not in postData["modelInformation"] or "name" not in postData["modelInformation"]:
			raise MissingModelInfoKeysError
		valid_units = ["metric", "imperial"]
		if postData["modelInformation"]["units"] not in valid_units:
			raise InvalidUnitsError
		payload_elems = postData["payload"]
		for i in payload_elems:
			if "vertices" not in i.keys() or "metadata" not in i.keys():
				raise MissingPayloadKeysError
			if not i["vertices"]:
			  	raise EmptyVerticesError
			if not i["metadata"]:
			  	raise EmptyMetadataError
		#this might have to be tweaked
		for obj in mybucket.objects.all():
			if obj.key == postData["modelInformation"]["name"] + ".json":
				raise AlreadyInBucketError
	except WrongNameError:
		return {"error": "File must be a .json -or- name of file does not match name within document"}
	except KeyError:
		return {"error": "'modelInformation' and 'payload' properties are required"}
	except MissingModelInfoKeysError:
		return {"error": "'modelInformation' must contain 'units' and 'name'"}
	except InvalidUnitsError:
	  	return {"error": "'units' values must be either 'imperial' or 'metric'"}
	except MissingPayloadKeysError:
	  	return {"error": "'payload' must include 'vertices' and 'metadata' for each element"}
	except EmptyVerticesError:
	  	return {"error": "'vertices' data is empty"}
	except EmptyMetadataError:
	  	return {"error": "'metadata' field is empty"}
	except AlreadyInBucketError:
		{"error": "File with this name already exists in S3 bucket. Please rename file and try again." }
	else:
		return {"success": "File is valid for upload"}
		#return mybucket.put_object(Key=settings["data-folder"] + "/" + "testing-chalice.json", Body=str(postData))
