import requests
import json
from watson.watson_auth import re_auth
cred = re_auth

url = "https://gateway.watsonplatform.net/relationship-extraction-beta/api/v1/sire/0"
data = {"sid": "ie-en-news", "rt": "json"}


def call_watson(txt):
	data["txt"] = txt
	r = requests.post(url, data=data, auth=cred)
	if r.status_code is not 200:
		print("error with Watson API")
		#TODO raise exception
		pass
	pruned = prune_watson_output(r.text)
	return pruned

def prune_watson_output(watson_output):
	data = json.loads(watson_output)
	sents = data["doc"]["sents"]["sent"]
	usd_parses = []
	if type(sents) is not list:
		sents = [sents]
	for sent in sents:
		usd_parses.append(sent["usd_dependency_parse"])
	return usd_parses
