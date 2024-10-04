lst = [1,2,3]
print(type(str(lst)),str(lst)) #列表可以转成字符串
print(str(lst).split(','))

#数学内置函数
print(divmod(10,3)) #商和余数

print(sum([1,23,4]))

print(pow(2,3))

print(round(3.9415926,3)) #四舍五入
print(round(314.987,-1)) #-1 对个位进行四舍五入
print(round(314.546,-2)) #-2 对十位四舍五入


#迭代器内置函数
lst = [1,3,454,6567,8,4,45]
lst = sorted(lst,reverse=True)
print(lst)
lst.sort(reverse=True)
#反向 结果是一个迭代器对象，不是列表，需要转换才行
print(id(lst),lst,type(reversed(lst)),id(list(reversed(lst))),id(lst))

a = [1,2,3,4,0]
b = ['dog','cat','monkey']

obj = zip(a,b)
print(obj,list(obj))#映射的内容是一个个元组

enu = enumerate(a,start=90) #映射的内容是一个个元组
print(enu,list(enu))

#all 都为True才是True，any 都是False才是False
c = []
print(all(c),any(c))
'''
all() 和 any() 函数在处理空列表时的行为不同。
all() 函数用于检查列表中的所有元素是否都满足某个条件（通常是真值）。如果列表为空，那么 all() 函数会返回 True，因为没有任何元素不满足条件。
any() 函数用于检查列表中是否存在至少一个元素满足某个条件（通常是真值）。如果列表为空，那么 any() 函数会返回 False，因为没有元素满足条件。
'''

#next
aa = [23,43,56]
bb = ['asdf','df']
oo = zip(aa,bb)
print(next(oo))
print(next(oo))
#print(next(oo)) 超出迭代器对象啊的个数


#filter
def fun(num):
    if num % 2 == 0:
        return num

#filter是过滤掉序列中不满足条件的元素
objec = filter(fun,range(1,11)) #将range中的数都执行一次fun这个函数的操作，然后设置一个对象存放结果
print(objec,tuple(objec)) #将对象转化成元组显示出来

#map是让序列中所有的元素都执行一遍前面的函数功能
def u(x):
    return x.upper()

newlist = ['sSHDJKsd','df','sFSDf']
obj2 = map(u,newlist)
print(list(obj2))


#format
print(format(3.14,'20')) #数值型默认右对齐
print(format('hello','20')) #字符串型默认左对齐
print(format(20,'*<20')) #可以进行修改



