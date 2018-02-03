#!/usr/bin/env python

import base64

def main():
	with open("flag_encode.txt") as f:
		data = f.read()
	
	n = ""
	steps = []
	
	while True:
		# Base16
		try:
			print "[?] using base16 deocde"
			n = base64.b16decode(data)
			print "[+] %s" % (n)
			steps.append(16)
			data = n
			continue
		except:
			pass
		# Base32
		try:
			print "[?] using base32 deocde"
			n = base64.b32decode(data)
			print "[+] %s" % (n)
			steps.append(32)
			data = n
			continue
		except:
			pass
		# Base64
		try:
			print "[?] using base64 deocde"
			n = base64.b64decode(data)
			print "[+] %s" % (n)
			steps.append(64)
			data = n
			continue
		except:
			pass
		break

	print "[+] flag found : %s" % (n)
	print "[+] steps : %s" % (steps)
	
if __name__ == "__main__":
	main()