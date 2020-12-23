# Assignment_7.2.py   mbox-short.txt
fname = input("Enter file name: ")
fh = open(fname)

nspam=0
fespam=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    f=line.find(':')
    espam=line[f+1:]
    fespam=fespam + float(espam)
    nspam=nspam+1

#print(nspam)
#print(fespam)

avgSpam=fespam/nspam
stavg=str(avgSpam)
print('Average spam confidence: ' + stavg)
