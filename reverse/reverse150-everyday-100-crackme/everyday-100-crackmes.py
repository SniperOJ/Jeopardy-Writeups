#!/usr/bin/env python

import random
import sys
import base64
import string
import os


def get_random_string(length):
    random_range = string.letters + string.digits
    random_string = ""
    for i in range(length):
        random_string += random.choice(random_range)
    return random_string


def create_c_code(password):
    c_code = ''
    # TODO
    c_code += '#include <stdio.h>\n'
    c_code += '#include <string.h>\n'
    c_code += '#include <unistd.h>\n'
    c_code += '\n'
    c_code += '#define LENGTH 64\n'
    c_code += '\n'
    c_code += 'int main(){\n'
    c_code += '    char password[] = "%s";\n' % password
    c_code += '    char input_password[LENGTH + 1] = {0};\n'
    c_code += '    int length = strlen(password);\n'
    c_code += '    int size = read(0, input_password, LENGTH);\n'
    c_code += '    input_password[size - 1] = 0;\n'
    c_code += '    if (strcmp(input_password, password) == 0){\n'
    c_code += '        return 0;\n'
    c_code += '    }\n'
    c_code += '    return 1;\n'
    c_code += '}\n'
    return c_code


def save_to_file(filename, content):
    with open("./code/" + filename, "w") as f:
        f.write(content)


def remove_file(filename):
    os.system("rm -rf ./code/%s" % filename)

def get_base64(content):
    return base64.b64encode(content)

def compile_c_code(binary_filename, filename):
    os.system("gcc -o ./code/%s ./code/%s" % (binary_filename, filename))

def read_file_content(filename):
    with open("./code/" + filename, "r") as f:
        return f.read()

def printing(content):
    sys.stdout.write(content)
    sys.stdout.flush()

def get_flag():
    with open("flag") as f:
	printing(f.read())

def main():
    total = 100
    while True:
        password = get_random_string(32)
        c_code = create_c_code(password)
        filename = password + ".c"
        binary_filename = password
        save_to_file(filename, c_code)
        compile_c_code(binary_filename, filename)
        remove_file(filename)
        content = read_file_content(binary_filename)
        remove_file(binary_filename)
        encrypted = get_base64(content)
        printing(encrypted + "\n")
        printing("There is %d crackmes waiting for you!\n" % (total))
        printing("[+]Give me the flag : ")
        input_password = raw_input()
        if input_password.lower() == "exit":
            exit(0)
        if input_password == password:
            print "[+] Right!"
            total -= 1
        else:
            print "[-] Wrong!"
            total += 2
        if total < 0:
            break
    get_flag()

if __name__ == "__main__":
    main()


