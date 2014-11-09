#Name:  parseHTMLimages.py
#Purpose:  Parses and reports image tags out of a given URL
#Usage:  parseHTMLimages.py <URL>
#Example:  parseHTMLimages.py "http://www4.ncsu.edu/~lgtateos"
#Author:  Jon Burroughs (jdburrou)
#Date:  4/12/2012

import sys, urllib2
sys.path.append("C:/Temp")
import BeautifulSoup as bs

# Get URL from user
url = sys.argv[1]

# Slurp HTML
html = urllib2.urlopen(url).read()
soup = bs.BeautifulSoup(html)
images = soup.findAll('img')

# Print report
print "%d images found." % len(images)
for img in images :
    print "image src:", img.get('src')
    