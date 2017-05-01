#!/usr/bin/env python

from pwn import *
import base64
import hashlib
import os


def get_md5(word):
    m = hashlib.md5()
    m.update(word)
    return m.hexdigest()


def get_password(filename):
    command = "objdump -d %s | head -n 154 | tail -n 10 > data.dat" % filename
    # print command
    os.system(command)
    with open("data.dat", "r") as f:
        content = list(f)
        str1 = content[0].split("$")[1].split(",")[0][2:].decode("hex")
        str2 = content[3].split("$")[1].split(",")[0][2:].decode("hex")
        str3 = content[6].split("$")[1].split(",")[0][2:].decode("hex")
        str4 = content[9].split("$")[1].split(",")[0][2:].decode("hex")
        return (str4 + str3 + str2 + str1)[::-1]

history = []

Io = remote("www.sniperoj.cn", 30019)

for i in range(101):
    print "[" + "-" * 32 + "]"
    print "[+] [%d] Times" % i
    encrypted = Io.readuntil("==")
    # print "[+] Encrypted : %s" % encrypted
    elf = base64.b64decode(encrypted)
    elf_hash = get_md5(elf)
    filename = "crackme"
    with open(filename, "wb") as f:
        f.write(elf)
    password = get_password(filename)
    print "[+] Password : [%s]" % (password)
    print "[+] %s" % Io.readline()
    Io.sendline(password)
    print "[+] %s" % Io.readline()[:-1]
    print "[+] Result : %s" % Io.readline()[:-1]

Io.interactive()
