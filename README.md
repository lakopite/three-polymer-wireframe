# Three Polymer Wireframe

Interface for interacting with three-polymer component and demonstrating desired functionality

## Lifecycle
All commits to three-polymer-wireframe#master and three-polymer#master will be built and deployed (within a few minutes) to:

http://three-polymer-wireframe.s3-website-us-west-2.amazonaws.com/

## Updating three-polymer reference
three-polymer-wireframe is set to reference the latest on three-polymer#master.  To access a specific git commit, change three-polymer-wireframe/bower.json
```
"three-polymer": "lakopite/three-polymer#{{three-polymer_commit_sha}}"
```

To point back to the default mode
```
"three-polymer": "lakopite/three-polymer#master"
```