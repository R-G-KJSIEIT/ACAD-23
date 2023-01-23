words = 0
lines = 0
char = 0

with open ("exp3.txt",'r') as e:
    for l in e:
        words += len(l.split())
        lines += 1
        char += len(l)
print ("No of Words:\t",words,"\n","No of Lines:\t",lines,"\n","No of char\t",char,"\n")
