import mechanize

url = "http://www.securitytube.net/video/3000"
br = mechanize.Browser()
br.open(url)

#Figure out all the forms which are there on this page

for form in br.forms():
    print form

#Selecting individual form

br.select_form(nr=0)
#Filling the form

br.form['q'] == 'defcon'

#submitting the form

br.submit()

#printing all the links in the page

for link in br.links():
    print link.url + ":" + link.text


"""
Exercise1: Install a vulnerable web application such as DVWA, OWASP Web Goat or other
           Use mechanize to try SQL Injection on form fields and deduce which fields are vulnerable to SQL Injection
"""

