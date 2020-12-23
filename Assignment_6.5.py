# Assignment 6.5:
text = "X-DSPAM-Confidence: 0.8475"
pos=text.find(':')
#print(pos)
x = text[pos+1:]
fx = float(x)
print(fx)
