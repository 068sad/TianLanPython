def fun(num):
    sum = 0
    odd = 0
    evel = 0
    for i in range(1,num+1):
        if i % 2 == 0:
            evel += i
        else:
            odd += i
    sum = odd + evel
    return sum,odd,evel

#多个返回值的情况下，会将返回值存储在一个元组中
result = fun(10)
print(result)

#解包赋值
a,b,c = fun(10)
print(a,b,c)