import json
from pprint import pprint

f = open('animals.txt', 'r')
pets = json.loads(f.read())
f.close()

pprint(pets)

# from xml.dom import minidom
#
# f = open('animals.txt', 'r')
# pets = minidom.parseString(f.read())
# f.close()

# names = pets.getElementsByTagName('name')
# for name in type:
# 	print name.firstChild.nodeValue

# import requests
# response = requests.get("http://placekitten.com/")
#
# # print the header information from the response
# print response.headers

# import requests
# body = {'Name': 'Rahul', 'Age': '22'}
# response = requests.get("http://codecademy.com/learn-http/")
# print response
# response = requests.post("http://codecademy.com/learn-http/", data = body )
# print "new response: ", response

# import requests
#
# # Make a GET request here and assign the result to kittens:
# kittens = requests.get('http://placekitten.com/')
#
# print kittens.text[559:1000]

# from urllib2 import Request, urlopen, URLError
#
# request = Request('file:///home/rahul/autoNav/README.md')
# request.add_data("go!")
#
# try:
#     response = urlopen(request)
#     kittens = response.read()
#     print kittens
#
# except URLError, e:
#     print 'No kittez. Got an error code:', e
#  # #---------------

# ----without requests lib--------

# from urllib2 import urlopen
#
# # Open http://placekitten.com/ for reading on line 4!
# kittens = urlopen('http://placekitten.com')
# print kittens
# response = kittens.read()
# body = response
#
#
# # Add your 'print' statement here!
# print body
# #------------------------