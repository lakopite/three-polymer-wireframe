# Three Polymer Wireframe

Interface for interacting with three-polymer component and demonstrating desired functionality

## Lifecycle
All commits to master branch will be built and deployed (within a few minutes) to:
http://three-polymer-wireframe.s3-website-us-west-2.amazonaws.com/

## Updating three-polymer reference
If you would like to point three-polymer-wireframe to a new version of the three-polymer component, please tag your desired three-polymer commit as a pre-release and update three-polymer-wireframe/bower.json to reflect the following pattern:
`"three-polymer": "lakopite/three-polymer#~{{three-polymer-release-number}}"W`
