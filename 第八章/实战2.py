s = input('请输入一个字符串：')

def fun(s):
    lst = list()
    for item in s:
        if item.isdigit():
            lst.append(item)
        else:
            continue
    sum = 0
    for i in range(len(lst)):
        sum += int(lst[i])
    return lst,sum

l,v = fun(s)
print(l,v)