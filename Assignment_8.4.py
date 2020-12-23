# Assignment_8.4  romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst=list()

for line in fh:
    line=line.rstrip()
    lstw = line.split()
#print(lstw)
    for word in lstw:
        #print(word)
        if not word in lst:
            lst.append(word)
        lst.sort()
print(lst)
#print(len(lst))
