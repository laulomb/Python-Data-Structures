# Assignment_8.5 mbox-short.txt:

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt" #que es esto?
fh = open(fname)
count = 0
for line in fh:
    line=line.rstrip()
    #if line == '': continue.  Si la linea esta 'vacia' continuar
    words=line.split()
    #print(words)
    if len(words) < 1: continue #Guardian code: si la linea? tiene longitud 0 (no tiene palabras):continuar
    if words[0]!='From': continue
    if words[0] == 'From':
        count=count+1
    print(words[1])

print("There were", count, "lines in the file with From as the first word")
