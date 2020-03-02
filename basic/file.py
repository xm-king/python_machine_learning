# -*- coding: utf-8 -*-
f = open("../.gitignore","r")
while True:
    line = f.readline()
    if (line !=''):
        print(line)
    else:
        break
f.close()