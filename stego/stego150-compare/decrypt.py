#!/usr/bin/env python

from PIL import Image
import sys

def printPixel(pixel):
    R = pixel[0]
    G = pixel[1]
    B = pixel[2]
    print "[%s][%s][%s]" % (R, G, B)

def compare(srcPixel, dstPixel, channel):
    return (srcPixel[channel] == dstPixel[channel])

if len(sys.argv) != 4:
    print "Usage : "
    print "        python decrypt.py [Input Image1] [Input Image2] [Channel]"
    print "Tip : "
    print "        Channel : 0->Red , 1->Green , 2->Blue"
    print "Author : "
    print "        WangYihang <wangyihanger@gmail.com>"
    exit(-1)

print "[+] Opening image1..."
srcIm = Image.open(sys.argv[1])
print "[+] Opening image2..."
dstIm = Image.open(sys.argv[2])
channel = int(sys.argv[3])

if channel < 0 or channel > 2:
    print "[-] Channel error!"


width = srcIm.size[0]
height = srcIm.size[1]

if width != dstIm.size[0] or height != dstIm.size[1]:
    print "[-] The size of the two images is not suit!"
    exit(-2)


print "[+] Image size : %s" % str((srcIm.size))


print "[+] Converting image1 to RGB mode..."
srcIm = srcIm.convert("RGB")
print "[+] Converting image2 to RGB mode..."
dstIm = dstIm.convert("RGB")

print "[+] Creating new image to hold qrcode..."
resIm = Image.new("RGB", (width, height), (0, 0, 0))

print "[+] decrypting..."
counter = 0
for x in range(height):
    for y in range(width):
        srcPixel = srcIm.getpixel((x, y))
        dstPixel = dstIm.getpixel((x, y))
        if not compare(srcPixel, dstPixel, channel):
            resIm.putpixel((x, y), (255, 255, 255))
            counter += 1

print "[+] [%d] differences found!" % (counter)
print "[+] Saveing qrcode image..."
resIm.save("./result.png")
print "[+] Showing the qrcode..."
resIm.show()
