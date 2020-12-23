# Assignment_10.2   mbox-short.txt:

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours=[]
d=dict()

for line in handle:
    line=line.rstrip()
    words=line.split()
    if len(words) < 1: continue #Guardian code: si la linea tiene longitud 0 (no tiene palabras):continuar
    if words[0]!='From': continue
    if words[0]=='From':       #Busco las lineas que empiezan con 'From'
        h=line.find(':')       #busco los dos puntos que estan en la expresion horaria
        hour=line[h-2:h]       #variable hour=desde los dos puntos hacia atras (-2) hasta (pero no includidos) los dos puntos
        hours.append(hour)     #me quedo con 'la hora' y la agrego a la lista con todas 'las horas'
#print(hours)
for h in hours:
    d[h]=d.get(h,0) + 1        #Calculo el histograma: cuantas veces se repite cada hora
for k,v in sorted(d.items()):  
    print(k,v)
