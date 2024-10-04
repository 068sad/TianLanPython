ch = input('请输入一个字符串：')
def fun(ch):
    list = ['hello','world','how','are','you']
    for item in list:
        if ch == item:
            return True
        else:
            continue
    return False

if fun(ch):
    print('exist')
else:
    print('not')
