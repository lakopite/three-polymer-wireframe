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

def validateJson():
    import json
    from datetime import datetime
    import os
    import boto3
    from botocore.client import Config

    try:
        postData = json.dumps(app.current_request.json_body)
        name = postData["modelInformation"]["name"]
        if "modelInformation" not in postData or "payload" not in postData:
            raise KeyError
    except KeyError:
        print("'modelInformation' and 'payload' properties are required")
    else:
        print("File good to upload!")
