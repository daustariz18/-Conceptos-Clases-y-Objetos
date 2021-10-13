# 3 numeros diferentes

number = 3333
h = abs(number)
mylist = [int(x) for x in str(h)]
a = len(set(mylist))
if a > 2:
    result = 'n'
else:
    result = 'y'

print(result)
