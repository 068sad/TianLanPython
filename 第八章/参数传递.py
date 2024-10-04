#将传递的参数放到一个元祖中
def fun(*n,m): #*n 是一个元组类型的形参
    print(type(n))
    for item in n:
        print(item)
    print(m)


fun(1,2,3,4,m = 23)

fun([1,2,3,4],m=25) #列表也可以传，但是只是将整个列表当作一个参数传进去

fun(*[11,22,3,44],m = 23) #*将列表进行解包

#将传递的参数放到字典中
def fun1(**m):
    print(type(m))
    for i in m.keys():
        print(i,'--->',m.get(i))

fun1(name = 'sze',age = 18,sex = '男')

dit = {'name':'sze','age':18}
fun1(**dit)  #先将字典解包后才能传入


