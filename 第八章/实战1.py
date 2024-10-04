import random

lit = [random.randint(1,101) for _ in range(1,11)]
print(lit)
max = 0
for i in range(len(lit)):
    if lit[i] > max:
        max = lit[i]
    else:
        continue

print(f'max value is {max}')