from xadrez.utils.Hashset import HashSet

x = [0, 1 ,2 ,3 ,4 ,5]
a = HashSet()

for i in x:
    a.add(i)


y = [3, 4 , 5 , 6 , 7 ,8 , 9]
b = HashSet()

for i in y:
    b.add(i)

a.display()
b.display()

b.ExceptWith(a)
b.display()


# aa = set(y)
# wd = set(x)

# dd = sorted(list(aa - wd))
# xx = (wd | aa) - set(dd)
# print(dd)
# print(xx)



