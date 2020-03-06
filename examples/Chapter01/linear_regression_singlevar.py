import numpy as np

filename = "data_singlevar.txt"
X = []
y = []
with open(filename, 'r') as f:
    for line in f.readlines():
        xt, yt = [float(i) for i in line.split(',')]
        X.append(xt)
        y.append(yt)

# Train/test split
num_training = int(0.8 * len(X))
num_test = len(X) - num_training

# Training data
## 训练数据集,用来建立模型
X_train = np.array(X[:num_training]).reshape((num_training,1))
y_train = np.array(y[:num_training])

# Test data
## 测试数据集,用来验证模型对未知数据的学习效果
X_test = np.array(X[num_training:]).reshape((num_test,1))
y_test = np.array(y[num_training:])

# Create linear regression object
from sklearn import linear_model

# 创建线性回归对象
linear_regressor = linear_model.LinearRegression()

# Train the model using the training sets
# 对训练数据集训练模型
linear_regressor.fit(X_train, y_train)

# Predict the output
# 对测试数据集进行预测
y_test_pred = linear_regressor.predict(X_test)

# Plot outputs
import matplotlib.pyplot as plt

plt.scatter(X_test, y_test, color='green')
plt.plot(X_test, y_test_pred, color='black', linewidth=4)
plt.xticks(())
plt.yticks(())
plt.show()

# Measure performance
import sklearn.metrics as sm

## 平均绝对误差,给定数据集的所有数据点的绝对误差平均值
print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_test_pred), 2))
## 均方误差,给定数据集的所有数据点的误差的平方的平均值
print("Mean squared error =", round(sm.mean_squared_error(y_test, y_test_pred), 2))
## 中位数绝对误差,给定数据集的所有数据点的误差的中位数
print("Median absolute error =", round(sm.median_absolute_error(y_test, y_test_pred), 2))
## 解释方差分,用于衡量我们的模型对数据集波动的解释能力
print("Explain variance score =", round(sm.explained_variance_score(y_test, y_test_pred), 2))
## R方得分，指确定性相关系数，用于衡量模型对未知样本预测的效果
print("R2 score =", round(sm.r2_score(y_test, y_test_pred), 2))

# Model persistence
import _pickle as pickle

## 保存数据模型
output_model_file = '3_model_linear_regr.pkl'

with open(output_model_file, 'w') as f:
    pickle.dump(linear_regressor, f)

with open(output_model_file, 'r') as f:
    model_linregr = pickle.load(f)

y_test_pred_new = model_linregr.predict(X_test)
print("\nNew mean absolute error =", round(sm.mean_absolute_error(y_test, y_test_pred_new), 2))

