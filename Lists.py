mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

for x in mylist:
    print("List entry %d" % x)


mylist2 = [4,5,6,7,8,9,10]

for y in mylist2:
    print("List2 entry %d" % y)


fulllist = mylist + mylist2
for z in fulllist:
    print("FullList entry %d" % z)