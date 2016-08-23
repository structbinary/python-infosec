import urllib

local_url = "http://localhost"

fetch_url = urllib.urlopen(local_url)
#print "status code is :" +str(fetch_url.code)
#print "Item in the fetched url is :" + fetch_url.read()



web_url = "http://www.securitytube.net/groups"

args = {'operation':'view', 'groupId':10}
encoded_url = urllib.urlencode(args)
page = urllib.urlopen(web_url+"?"+encoded_url)
print page.read()

"""
Exercise : urlencode() does a bad job in handling special character in the URL
           Research on .quote() and .quote_plus and illustrate how they can help
"""


url = urllib.urlopen("http://localhost")


