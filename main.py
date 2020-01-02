import telegram
import bitmex
import requests, json

# client = bitmex.bitmex(test=True, api_key='LAqUlngMIQkIUjXMUreyu3qn',api_secret='chNOOS4KvNXR_Xq4k4c9qsfoKWvnDecLATCRlcBwyKDYnWgO')
client = bitmex.bitmex()
# client.from_url(none, ' https://testnet.bitmex.com/api/v1')
# print(1)
# result = client.Quote.Quote_get(symbol="XBTUSD", reverse=True, count=1).result()
# print(2)

response = requests.get("https://testnet.bitmex.com/api/v1/announcement").json()
print(response)