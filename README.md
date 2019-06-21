# roomtemp
This is Node.js 10.x script for AWS Lambda.
You have to make an Alexa skill and attach this script to the endpoint.
Alexa speaks bedroom temperature if working well.
Bedroom temperature is stored in DynamoDB. Table name is 'room-stataus' and Item is 'room' and 'room_temp'.