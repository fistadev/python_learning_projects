# data = [ { "country": [
#         { "city": "New York", "state": "NY" },
#         { "city": "Boston", "state": "MA" }
#   ]},
#   { "country": [
#         { "city": "Quebec", "state": "QC" },
#         { "city": "Toronto", "state": "ON" }
#   ]} ]
#
# for i in theJSON:
#
#     for j in i["country"]:
#         return data

import urllib.request
webUrl = urllib.request.urlopen("http://www.google.com")
results = webUrl.read()
print(results)