from chalice import Chalice, NotFoundError, ChaliceViewError
import boto3
import json

app = Chalice(app_name='three-polymer-wireframe-api')

s3 = boto3.resource('s3')

settings = {
	'site-bucket': '$INSERT-BUCKET-NAME-HERE$',
	'data-folder': '$INSERT-DATA-FOLDER-HERE$'
}

def getModelNames(_bucket,_prefix):
	s3_objects_resp = s3.meta.client.list_objects(Bucket=_bucket, Prefix=_prefix)
	s3_objects = s3_objects_resp.get('Contents', [])
	while s3_objects_resp['IsTruncated']:
		s3_objects_resp = s3.meta.client.list_objects(Bucket=_bucket, Prefix=_prefix, Marker=_existing_s3_objects_resp["Contents"][-1]['Key'])
		s3_objects += s3_objects_resp.get('Contents', [])
	return [i['Key'].replace(_prefix,"").replace(".json","") for i in s3_objects if not i['Key'] == _prefix]

@app.route('/get-model-data/{modelname}', methods=['GET'], cors=True)
def getModelData(modelname):
	try:
		print "in get model data"
		json_object = s3.Object(settings['site-bucket'],settings['data-folder']+"/" + modelname+".json")
		file_content = json_object.get()['Body'].read().decode('utf-8')
	except:
		raise NotFoundError(modelname)
	try:
		json_content = json.loads(file_content)
		return json.dumps(json_content)
	except:
		return ChaliceViewError()

@app.route('/get-models', methods=['GET'], cors=True)
def getModels():
    try:
    	result = json.dumps(getModelNames(settings['site-bucket'],settings['data-folder']+"/"))
    	return result
    except:
    	raise ChaliceViewError()