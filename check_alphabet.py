s = 'azcbobobegghakl'

alpha='abcdefghijklmnopqrstuvwxyz'
iter1=0
super_str = s[0]

for letter in s:
    str1 = s[iter1:len(s)]
    prev_position=0
    k=0
    for j in str1:
        count = 0
        for l in alpha:
            if l == j:
                break
            else:
                count = count + 1
        position = count
        if position < prev_position:
            break
        else: 
            prev_position = position
            k = k+1
    if len(str1[0:k]) > len(super_str):
        super_str=str1[0:k]
    iter1 = iter1+1

print('Longest substring in alphabetical order is: ',super_str)


