import requests
import json
import os

url = "https://gateway.watsonplatform.net/relationship-extraction-beta/api/v1/sire/0"
data = {"sid": "ie-en-news", "rt": "json"}

auth = None
vcap_json = os.environ.get('VCAP_SERVICES', None)
if vcap_json:
	vcap = json.loads(vcap_json)
	cred = vcap["relationship_extraction"][0]["credentials"]
	auth = (cred["username"], cred["password"])
else:
	from watson.watson_auth import re_auth
	auth = re_auth

def call_watson(txt):
	data["txt"] = txt
	r = requests.post(url, data=data, auth=auth)
	if r.status_code is not 200:
		raise IOError("error connecting to Watson API: " + str(r.status_code))
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
