# -*- coding: utf-8 -*-
import numpy as np
'''
Numpay中的ndarray是一个多维数组对象，由两部分组成
-- 实际的数据
-- 描述这些数据的元数据
'''
### 矩阵加法
matrix1 = np.array([[1,2,3],[4,5,6]])
matrix2 = np.array([[1,1,1],[1,1,1]])
print(matrix1)
print(matrix1+matrix2)

vector = np.arange(0,10,2)
print(vector)

arry = np.arange(10)
print(np.sqrt(arry))
print(np.exp(arry))