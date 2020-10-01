import urllib.request, json

from os import system, name
import time

api = "https://api.covid19india.org/state_district_wise.json"

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def fetchjson(url):
	resp = urllib.request.urlopen(url)
	return(json.loads(resp.read().decode()))

def printinfo():
		js = fetchjson(api)
		clear()
		i = 0
		for state in js:
			i+=1
			print("{}- {}: ".format(i,state))
			total = 0
			death = 0
			recovered = 0
			active = 0
			for x in js[state]["districtData"]:
				total+= js[state]["districtData"][x]["confirmed"]
				death+= js[state]["districtData"][x]["deceased"]
				recovered+= js[state]["districtData"][x]["recovered"]
				active+= js[state]["districtData"][x]["active"]

			print("	Confirmed : " + str(total))
			print("	Deceased  : " + str(death))
			print("	Recoveries: " + str(recovered)) 
			print("	Active    : " + str(active))
			


while True:
    printinfo()
    time.sleep(10)
