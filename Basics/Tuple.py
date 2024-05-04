# Same as list but cannot add element (Immutable)

li = [1, 2, 3, 4]
li.append(10)
print(li)

tpl = (1, 1, 2, 3, 4)
# tpl[0] = 10 # throw an error
print(tpl)
print(tpl.count(1))

tpl2 = (1, 2, 3)
a, b, c = tpl2
print(a, b, c)