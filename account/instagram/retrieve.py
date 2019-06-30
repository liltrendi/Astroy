#!/usr/bin/env python
from robobrowser import RoboBrowser
import pandas as pd
import re
import subprocess
import sys

username=sys.argv[1]
browser=RoboBrowser(history=True,parser="html.parser")
browser.open("http://instawidget.net/generate")
forms=browser.get_forms()
form=forms[0]

if "@" in str(username):
    username=username.partition("@")[0]

form["username"]=username
form["usericon"]="false"
browser.submit_form(form)
html=str(browser.parsed)

url2="http://instawidget.net/v/user/{}".format(username)
browser.open(url2)
html2=str(browser.parsed)

if "0 followers" not in html2.lower():

    with open("casper.txt","w") as f:
        print(html,file=f)
    subprocess.call("cat casper.txt|grep center > center.txt",shell=True)
    subprocess.call("sed 's/<center>//' center.txt > final.txt",shell=True)
    subprocess.call("sed 's/<\/center>//' final.txt > widget.txt",shell=True)
    subprocess.call("sed 's/\/js\/instawidget.js/https:\/\/instawidget.net\/js\/instawidget.js/' widget.txt > results",shell=True)
    subprocess.call("rm final.txt center.txt casper.txt widget.txt",shell=True)

else:
    with open("results","w") as n:
        n.write("not found")
