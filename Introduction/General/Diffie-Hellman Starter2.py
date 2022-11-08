p = 28151

for g in range (2,p):
    for x in range (1,p-1):
     if pow (g,x,p) ==1:
        break
    if x ==(p-2):
            print(g)
            break