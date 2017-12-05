import urllib.request, json 
etherAddress = "0x57d22b967c9dc64e5577f37edf1514c2d8985099"
link = "https://api.etherscan.io/api?module=account&action=balance&address="+etherAddress+"&tag=latest&apikey=YourApiKeyToken"
with urllib.request.urlopen(link)as url:
	data = json.loads(url.read().decode())
	if(data["status"] == "1" and data["message"] == "OK"):
		print(data["result"])