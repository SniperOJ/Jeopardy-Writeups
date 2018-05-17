#### BaSO4
该题目目的在于考察选手脚本编写能力, 以及考察新手同学的知识面广度
BaSO4 联想到 Base64, 23333
题目提供文件为一个字符串, 如果熟悉 BaseN 编码的话, 是可以反应上来应该怎么解的
这个题目在构建的时候是对 flag 进行X次的 BaseN 编码, 其中 N 在 {16, 32, 64} 中随机选取一个记为 F
也就是说, flag 被如下编码函数序列进行编码
{baseF1, baseF2, ... ,baseFX}
而解决这个题就是编码的逆过程, 问题在于如何判定在编码的时候到底使用了哪一个函数进行编码
关于这个问题, 给出两个方案:
1. base64, base32, base16 这三种编码方式在生成的输出字符串字符集方面是有差异的, 可以通过这个差异在解码的时候对该使用的解码函数进行选择
2. base64, base32, base16 这三种编码方式生成输出的字符集越来越少, 因此当编码样本足够大的时候
假设使用了 base64 进行编码, 密文中包含了 base16/base32 中本身不存在的字符, 使用 base32/base32 进行解码是会报错的
因此利用高级语言的 try/catch 这个特点即可解决这个问题, 下面给出 Python 语言的解码脚本
```
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
```
