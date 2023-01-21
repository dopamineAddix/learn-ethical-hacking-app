import socket
import requests
import pprint
import json

hostname = input('Input a domain name: ')
ipaddress = socket.gethostbyname(hostname)

print(f'IP Address : {ipaddress}')

request_url = 'https://ipxapi.com/api/ip?ip=' + ipaddress

headers = {
   'Accept': "application/json",
   'Content-Type': "application/json",
   'Authorization': "Bearer 6657|sPHW9sEFnNMOYfuYlLWOjgVqgnLWkYdKrs7cqd3F",
   'cache-control': "no-cache"
}

response = requests.request("GET", request_url, headers=headers)

geolocation = response.content.decode()
geolocation = json.loads(geolocation)
for k,v in geolocation.items():
	pprint.pprint(str(k) + ' : ' + str(v))
