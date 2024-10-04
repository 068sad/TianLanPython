ch = input('请输入一个字符串：')

def fun(ch):
    lst = list()
    for item in ch:
        if item >= 'A' and item <= 'Z':
            lst.append(chr(ord(item)+32))
        elif item >= 'a' and item <= 'z':
            lst.append((chr(ord(item) - 32)))
        else:
            lst.append(item)
    cha = ''.join(lst)
    print(cha)


fun(ch)
print(ord('A'),ord('a')) #ord unicode码