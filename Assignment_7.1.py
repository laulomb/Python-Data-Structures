# Assignment_7.1.py   words.txt
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line=line.rstrip()
    line=line.upper()
    print(line)
