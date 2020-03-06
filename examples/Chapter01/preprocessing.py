import numpy as np
from sklearn import preprocessing

data = np.array([[ 3, -1.5,  2, -5.4],
                 [ 0,  4,  -0.3, 2.1],
                 [ 1,  3.3, -1.9, -4.3]])

# mean removal 把每个特征的平均值移除，保证特征均值为0，即标准化处理，消除特征彼此间的偏差
data_standardized = preprocessing.scale(data)
print("\nMean =", data_standardized.mean(axis=0))
print("Std deviation =", data_standardized.std(axis=0))

# min max scaling 范围缩放
data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled = data_scaler.fit_transform(data)
print("\nMin max scaled data:\n", data_scaled)

# normalization 归一化
data_normalized = preprocessing.normalize(data, norm='l1')
print("\nL1 normalized data:\n", data_normalized)

# binarization 二值化
data_binarized = preprocessing.Binarizer(threshold=1.4).transform(data)
print("\nBinarized data:\n", data_binarized)

# one hot encoding 独热编码
encoder = preprocessing.OneHotEncoder()
encoder.fit([[0, 2, 1, 12], [1, 3, 5, 3], [2, 3, 2, 12], [1, 2, 4, 3]])
encoded_vector = encoder.transform([[2, 3, 5, 3]]).toarray()
print("\nEncoded vector:\n", encoded_vector)

