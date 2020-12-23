# Assignment_9.4    mbox-short.txt:

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di=dict()
mails=[]

for line in handle:
    line=line.rstrip()
    words=line.split()
    #print(words) Listas por linea
    if len(words) < 1: continue #Guardian code: si la linea tiene longitud 0 (no tiene palabras):continuar
    if words[0]!='From': continue
    if words[0]=='From':   #Si la primera palabra de la lista (words) es 'From' :
        mail=words[1]      #guardo la segunda palabra como la variable mail,
        mails.append(mail) #y la agrego a la lista mails.
#print(mails) Lista con todos los mails que hay en el texto, repetidos.

for m in mails:
    di[m]=di.get(m,0) + 1   #Hago el histograma.

M=None  #Creo 2 variables vacias: M=mail mas repetido y L es el numero de veces de ese mail.
L=None
#Two itineration variables: m(key),n(value) pair.
for m,n in di.items():
    if L is None or n>L:
        L=n
        M=m
print(M,L) #Resultado: el mail que mas mando mails, y el numero de veces.
