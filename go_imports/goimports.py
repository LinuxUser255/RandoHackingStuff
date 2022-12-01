#!/usr/bin/env python3

# print the package main, "fmt" amd "net/http imports to the terminal
# that way you can copy-paste them into your text editor or IDE

import os

def cat_go_imports():
    
    cmd = 'cat '
    filename = 'i.txt'
    with open(filename, 'r') as f:
        os.system(cmd + ' ' + filename) 

    
cat_go_imports()
