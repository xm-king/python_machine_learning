# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
idCardInfo = pd.read_csv("idcard.csv")
plt.plot(idCardInfo['confidence'],idCardInfo['money'],c="red")
plt.xlabel("confidence")
plt.ylabel("money")
plt.title("confidence-money")
plt.show()
## 折线图

## 区域画多图

## 其它操作