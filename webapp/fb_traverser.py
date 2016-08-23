import mechanize
import cookielib

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
url = 'https://www.facebook.com/login/'
br.open(url)
for form in br.forms():
    print form

br.select_form(nr=0)
br.form['email'] = 'sandeepmahto3@gmail.com'
br.form['pass'] = '*******'
br.submit()
br.response().read()
for link in br.links():
    print link.url + ":" + link.text

"""
Exercise1: Explore the concept of mechanize.CookieJar
           How is it useful?
           Sample Code to illustrate its functionality

Exercise2: Explore http://seleniumhq.org/support/
           Can u automate the current example in it?

Exercise3: Explore Zolera soap infrastructure(http://pywebsvcs.sourceforge.net/zsi.html)
           Attack web services on webgoat
"""