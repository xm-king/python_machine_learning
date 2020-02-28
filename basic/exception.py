# -*- coding: utf-8 -*-
try:
    open("no_exist.txt","r")
except IOError:
    print("IO异常:文件未找到")
finally:
    print("结束")