#!/usr/bin/env python
import urllib.request, urllib.error, urllib.parse
import re, sys
import urllib.request, urllib.error, urllib.parse
from html.parser import HTMLParser

url = input("Enter an URL: ")
res = urllib.request.Request(url)
content = urllib.request.urlopen(res).read().decode('utf-8')

pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+[-a-zA-Z0-9._]+")
emails = re.findall(pattern, content)
print(emails)


class myParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if(tag == "a"):
            for a in attrs:
                if(a[0] == "href"):
                    link = a[1]
                    print(link)
                    newParse = myParser()
                    newParse.feed(link)

url = input("Enter an URL: ")
req = urllib.request.Request(url)
handle = urllib.request.urlopen(req)
parser = myParser()
parser.feed(handle.read().decode('utf-8'))

