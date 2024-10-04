def b(name,age):
    print(name+' birthday')
    print(str(age) + 'birthday')


#关键字传参,顺序可以和形参不一样,位置传参和关键字传参可以混用，但是位置传参必须在关键字传参前面
b(age = 90,name = 'sze')
#c(name = 'szw',18)

#默认值参数,在定义的函数中给定一个默认值，如果不传参，则调用默认值，如果传参，则调用传递的参数
def fun(a = 18,b = 19):#默认值参数放最后
    temp = a
    a = b
    b = temp
    print(a,b)

fun(22)
fun(b = 90)


