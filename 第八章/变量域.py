def fun(a,b):
    s = 100
    print(s+a+b)

print(fun(10,20))
#print(s) #NameError: name 's' is not defined

ss = 100
def fun1(a,b):
    global c
    c = 199
    return ss+c+b+a

print(fun1(10,20))
print(c)
