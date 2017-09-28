# Three Polymer Wireframe

Interface for interacting with three-polymer component and demonstrating desired functionality

## Lifecycle
All commits to three-polymer-wireframe#master and three-polymer#master will be built and deployed (within a few minutes) to:

https://arup-model-viewer.firebaseapp.com/

## Accessing api in local environment
three-polymer-wireframe accesses a chalice api to retrieve model json data.
In order to connect to the dev url in your local environment, please include a file `local_settings.js` in your project's root directory with the following contents:
```
const _BACKEND_URL_ = "https://<AWS API ID>.execute-api.us-west-2.amazonaws.com/dev/"
//Replace `<AWS API ID>` with actual API ID
```

## Updating three-polymer reference
three-polymer-wireframe is set to reference the latest on three-polymer#master.  To access a specific git commit, change three-polymer-wireframe/bower.json
```
"three-polymer": "lakopite/three-polymer#{{three-polymer_commit_sha}}"
```

To point back to the default mode
```
"three-polymer": "lakopite/three-polymer#master"
```
