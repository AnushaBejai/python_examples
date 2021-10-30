text = "X-DSPAM-Confidence:    0.8475";
zap=text.find(':')
print(zap)
z=(text[19: ])
print(z)
var=z.strip()
var=float(var)
print(var)
