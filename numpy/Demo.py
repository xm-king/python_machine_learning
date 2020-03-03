# -*- coding: utf-8 -*-
import numpy as np
from numpy import random as rd
'''
numpy 最主要进行矩阵相关的计算
'''

### 矩阵的创建
# npArray1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(npArray1)
# ### 矩阵的元素类型以及
# print(type(npArray1))
# print(npArray1.shape)
# print(npArray1.dtype)

### 矩阵读取文件内容
# numpyData = np.genfromtxt("data.csv",delimiter=',',dtype=str)
# #print(numpyData)
# print(numpyData.shape)
# print(numpyData[0,3])
# print(numpyData[1,0])
#
# ## 切片的用法
# print(numpyData[0:1])
# print(numpyData[:,3])
# print(numpyData[:,0:2])

## 值比较
# print(np.array([1,2,4,2,3]) == 2)

## 矩阵属性操作
# npArrayData = np.array([[1,2,3,4],[5,6,7,8]])
# print(npArrayData.dtype)
# ## 类型转换
# # npArrayData= npArrayData.astype(float)
# # print(npArrayData.dtype)
# ## 最小值
# print(npArrayData.min())
# ## 最大值
# print(npArrayData.max())
# ## 平均值
# print(npArrayData.mean())

## 求和
# print(npArrayData.sum())
# print(npArrayData.sum(axis=0))
# print(npArrayData.sum(axis=1))

## arange
# print(np.arange(10))
# print(np.arange(0,20,2))

## 矩阵变换
# npArray =np.arange(15).reshape(3,5)
# print(npArray)
# ## 矩阵维度
# print(npArray.ndim)
## 矩阵的元素数量
# print(npArray.size)
# 矩阵初始化
# print(np.zeros((3,5)))
# print(rd.random((3,5)))

## 矩阵加减乘操作
# matrix1 = np.arange(0,8).reshape(2,4)
# matrix2 = np.arange(0,8).reshape(4,2)
# print(np.dot(matrix1,matrix2))
## 矩阵其他操作
# npArray = np.floor(rd.random((3,4))*10)
# print(npArray)
## 矩阵特征值分解
npArray = np.array([[2,3],[2,1]])
a,b = np.linalg.eig(npArray)
print(a)
print(b)
