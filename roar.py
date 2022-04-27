## ROAR - Ethereum blockchain token piercer
## Created by: TingiDev
## Codebase initiated on 26/04/2022

import requests
import json

# Params
url = "https://api.etherscan.io/api?"
apiKey = "3ZSDDXEPPUIDT4N2Z2TWJ7W3V8A1QB4TY9"
wei = 1000000000000000000

# Get ETH balance for account
address = "0xca86d57519dbfe34a25eef0923b259ab07986b71"
payload = {'module':'account',
           'action':'balance',
           'address':address,
           'tag':'latest',
           'apikey':apiKey}
response = requests.get(url, params=payload)
result = json.loads(response.text)['result']

# Get ERC20 transactions for account (Messi)
address = "0xca86d57519dbfe34a25eef0923b259ab07986b71"
payload = {'module':'account',
           'action':'tokentx',
           'address':address,
           'startblock':0,
           'endblock':99999999,
           'sort':'desc',
           'apikey':apiKey}
response = requests.get(url, params=payload)
result = json.loads(response.text)['result']

# Save ouput
fname = "test_account.json"
with open(fname, "w") as f:
    json.dump(result, f)

# Get ERC20 transactions for token (SNX)
payload = {'module':'account',
           'action':'tokentx',
           'contractaddress':'0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F',
           'startblock':0,
           'endblock':99999999,
           'sort':'desc',
           'apikey':apiKey}
response = requests.get(url, params=payload)
result = json.loads(response.text)['result']

# Save ouput
fname = "test_token.json"
with open(fname, "w") as f:
    json.dump(result, f)