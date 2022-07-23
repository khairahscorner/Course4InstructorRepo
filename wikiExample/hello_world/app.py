import json
import wikipedia

print("loading function")

def lambda_handler(event, context):
	"""Wikipedia summariser"""
	if "body" in event:
		event = json.loads(event["body"])
	entity = event["entity"]
	res = wikipedia.summary(entity, sentences=1)
	print(f"context: {context}, event: {event}")
	print(f"response from wiki api: {res}")
	response = {
		"statusCode": "200",
		"headers": {"Content-type": "application/json"},
		"body": json.dumps({"message": res})
	}
	return response
