# 斐波那契数列

def fibonacci(a,b,n):
    if(n == 2):
        return a+b
    else:
        return fibonacci(b,a+b,n-1)

target = int(input("请输入数据:"))
result = 0
a,b = 1,1
result = fibonacci(a,b,target-1)
print(result)