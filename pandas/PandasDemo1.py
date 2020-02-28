import pandas as pd
### Panda索引
# data = pd.read_csv("titanic_train.csv")
# print(data.head())
# print(data[['Age',"Fare"]][:5])
# print((data.index))
# print(data.iloc[0:5])
# print((data['Age']>70).sum())

### GroupBy操作
df = pd.DataFrame({"Key":['A','B',"C",'A','B',"C",'A','B',"C"],
                   "data":[1,2,3,6,2,3,4,2,2]})
print(df.groupby("Key").sum())