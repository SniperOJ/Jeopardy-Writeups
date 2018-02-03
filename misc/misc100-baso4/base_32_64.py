import base64
import random
import os
import sys

with open("flag.txt","r") as file:
	flag=file.read()
for i in range(0,20):
	if random.randint(0,1):
		flag=base64.b64encode(flag)
	else:
		flag=base64.b32encode(flag)
with open("flag_encode.txt","w") as file:
	file.write(flag)
