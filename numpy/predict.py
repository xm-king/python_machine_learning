# -*- coding: utf-8 -*-
import numpy as np
c,v = np.loadtxt("data.csv",delimiter=",",usecols=(6,7),unpack=True)

#计算成交量加权平均价格
vwap = np.average(c,weights=v)
print("VWAP = %f"%(vwap))

#算术平均值函数
means = np.mean(c)
print("Means = %f"%(means))

#时间加权平均价格
#t = np.array(len(c))
#print("TWAP = %f"%(np.average(c,weights=t)))

#虚招最大值和最小值
print("MAX:%f"%(np.max(c)))
print("MIN:%f"%(np.min(c)))