s= 'avbobsdasdasdsbobdasdbobdasda'
i = 0
count = 0
while i <= len(s)-2:
    if s[i:i+3] == 'bob':
        count += 1
    i += 1
print("Number of times bob occurs is: ",count)