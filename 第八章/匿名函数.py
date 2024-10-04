s = lambda a,b:a+b
print(type(s),s(10,20))


l = [1,2,3,4,5]
lst = list()
for i in range(5):
    result = lambda x:x[i] #x是形式参数
    print(result(l)) #l是世实际参数



ls = ['dsfsdf','ddfs']
ls.sort(key=lambda x: len(x),reverse=True)
print(ls)

