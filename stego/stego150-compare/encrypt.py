#!/usr/bin/env python

import qrcode
from PIL import Image
import random
import sys

if len(sys.argv) != 5:
    print "Usage : "
    print "        python encrypt.py [Secret] [Input Image] [Output Image] [Channel]"
    print "Tip : "
    print "        Channel : 0->Red , 1->Green , 2->Blue"
    print "Author : "
    print "        WangYihang <wangyihanger@gmail.com>"
    exit(-1)


secret = sys.argv[1]
srcName = sys.argv[2]
dstName = sys.argv[3]
channel = int(sys.argv[4])

if channel < 0 or channel > 2:
    print "[-] Channel error!"

print "[+] Secret : [%s]" % (secret)
print "[+] Creating qrcode image..."
secretIm = qrcode.make(secret)
print "[+] Opening src image..."
srcIm = Image.open(srcName)
print "[+] Converting src image to RGB mode"
srcIm = srcIm.convert("RGB")

width = srcIm.size[0]
height = srcIm.size[1]

secretIm = secretIm.resize((width, height))
print "[+] src image size : %s" % (str(secretIm.size))

print "[+] encrypting..."
for x in range(height):
    for y in range(width):
        secretPixel = secretIm.getpixel((x, y))
        srcPixel = srcIm.getpixel((x,y))
        srcPixel = list(srcIm.getpixel((x, y)))
        secretTargetX = x % height
        secretTargetY = y % width
        if secretPixel == 255: # actually it is 255
            srcPixel[channel] += random.randint(0, 10)
            srcIm.putpixel((secretTargetX, secretTargetY), tuple(srcPixel))

print "[+] Success!"
print "[+] Saving..."
srcIm.save(dstName)
print "[+] Finished!"
