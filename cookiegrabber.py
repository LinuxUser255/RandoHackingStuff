#!/usr/bin/env python3

filename = "/usr/bin/stealcookies.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
