import requests
import pandas as pd
import json


item_ids = [173108, 173109, 173110, 173170, 173171, 173172, 173173]
item_prices = {}


with open('config.json', 'r') as f:
	config = json.load(f)

def get_api():	
	session = requests.session()
	try:
		req = session.get(f"https://eu.api.blizzard.com/data/wow/connected-realm/{config['REALM_ID']}/auctions?namespace=dynamic-eu&locale=en_US&access_token={config['ACCESS_TOKEN']}")
		result = req.json()
		df = pd.DataFrame(result['auctions'])
	except requests.exceptions.RequestException as e:
		print(e)
	
	items = []
	
	df2 = pd.DataFrame()
	for index, row in df.iterrows():
		if row['item']['id'] in item_ids:
			print(f"{row['item']['id']} IS IN IDS")
			df2 = df2.append(row)
	
	print(df2)
	
	return item_prices


get_api()