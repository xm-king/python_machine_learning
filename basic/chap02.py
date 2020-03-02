# -*- coding: utf-8 -*-

## 根据给定的年月日以数字形式打印出日期
'''
months =['January','February','March','April','May','June','July','August','September','October','November','December']
## 以1-3的数字作为结尾的列表
ending = ['st','nd','rd'] + 17 * ['th'] +['st','nd','rd'] + 7 *['th'] + ['st']
year = input("Year:")
month = int(input("Moth(1-12):"))
day = int(input("Day(1-31):"))
print("%s-%s-%s%s"%(year,months[month-1],day,ending[day-1]))
'''

data= {"name":"xiangmin","age":33}
print("%(name)s,%(age)s"%data)

for key in data:
    print("key:%s,value:%s"%(key,data.get(key)))
