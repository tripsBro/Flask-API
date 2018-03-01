import requests
from flask import Flask


var = requests.get("http://127.0.0.1:5000/user/rahul")
print "var: ", var
# print "var type: ", type(var), "history: ", var.history, "get state: ", var.__getstate__()
print "Inspect element: ", var.text # if error then .text.encode('utf-8') for text and .text.encode('ISO-8859-1') for HTML.
# print "headers: ", var.headers
# print "cookies:m ", var.cookies.get_dict()