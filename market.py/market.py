import urllib.request, json 
from operator import itemgetter
with urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=0") as url:
    data = json.loads(url.read().decode())
    list = []
    for x in data:
    	if(x["total_supply"] == "null" or x["max_supply"] == "null" or x["total_supply"] is None or x["max_supply"] is None):
    		continue
    	z = float(x["total_supply"])
    	y = float(x["max_supply"])
    	res = y-z
    	percent = z/y
    	if(res == 0):
    		continue
    	#print("{0:3} {1:20}  max: {2:15} total: {3:15} res: {4:15} perc: {5:3}%".format(x["rank"],x["id"], x["max_supply"],x["total_supply"],res,percent))
    	#print(x["id"],"\t",x["rank"], x["max_supply"],x["total_supply"], "\t\tErgibt: ", res, "\t\t Prozent: ",percent,"%")
    	q = (x["rank"],x["id"], x["max_supply"],x["total_supply"],res,percent)
    	list.append(q)
    list = sorted(list, key=itemgetter(5))
    for x in list:
    	print("{0:3} {1:20}  max: {2:15} total: {3:15} res: {4:15} perc: {5:3}%".format(x[0],x[1], x[2],x[3],x[4],x[5]))
