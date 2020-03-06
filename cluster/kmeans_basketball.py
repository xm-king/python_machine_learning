# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


'''
数据集
X表示二维矩阵数据，篮球运动员比赛数据
第一列表示球员每分钟助攻数,
第二列表示球员每分钟得分
'''
X = [[0.0888, 0.5885], [0.1399, 0.8291], [0.0747, 0.4974], [0.0983, 0.5772], [0.1276, 0.5703], [0.1671, 0.5835], [0.1906, 0.5276], [0.1061, 0.5523], [0.2446, 0.4007], [0.167, 0.477], [0.2485, 0.4313], [0.1227, 0.4909], [0.124, 0.5668], [0.1461, 0.5113], [0.2315, 0.3788], [0.0494, 0.559], [0.1107, 0.4799], [0.2521, 0.5735], [0.1007, 0.6318], [0.1067, 0.4326], [0.1956, 0.428]]
## 聚类算法，参数n_clusters = 3，聚成3类
clf = KMeans(n_clusters=3)
## 直接对数据进行聚类，聚类不需要进行预测
y_pred = clf.fit_predict(X)
myfont = fm.FontProperties(fname=r'simkai.ttf')
# 获取第一列和第二列数据 使用for循环获取 n[0]表示X第一列
x = [n[0] for n in X]
y = [n[1] for n in X]

plt.figure(figsize=(10,5))
# 绘制散点图 参数：x横轴 y纵轴 c=y_pred聚类预测结果 marker类型 o表示圆点 *表示星型 x表示点
plt.scatter(x, y, c=y_pred, marker='x')
# 绘制标题
plt.title("Kmeans-篮球数据",fontproperties=myfont,fontsize=18)
plt.xlabel("每分钟助攻数",fontproperties=myfont,fontsize=18)
plt.ylabel("每分钟得分数",fontproperties=myfont,fontsize=18)
# 显示图形
plt.show()