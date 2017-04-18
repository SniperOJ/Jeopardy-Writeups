#!/usr/bin/env python

import requests
import hashlib

def getMd5(word):
    m = hashlib.md5()
    m.update(word)
    return m.hexdigest()

def getContent(filepath):
    with open(filepath, "r") as f:
        return f.read()

def login(username, password):
    url = "http://web2.sniperoj.cn:10002/index.php"
    data = {
        "username":username,
        "password":password,
    }
    response = requests.post(url, data=data)
    print response.text.split("\n")[0]

username = getContent("./evil1.txt")
password = getContent("./evil2.txt")

print "[+] Checking md5 of input files..."
if getMd5(username) == getMd5(password):
    print "[+] Checking OK!"
    print "[+] Sending..."
    login(username, password)
else:
    print "[-] Checking failed! Please use : [http://www.win.tue.nl/hashclash/]"
