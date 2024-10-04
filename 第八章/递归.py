def j(num):
    if num == 1:
        return 1
    else:
        sum = num * j(num - 1)
        return sum


print(j(4))


def fac(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fac(n - 1) + fac(n - 2)


for i in range(1, 11):
    print(fac(i), end=' ')
