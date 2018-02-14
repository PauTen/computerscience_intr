def laceStrings(s1,s2):
    ns = ''
    i = 0
    while True:
        if len(s1) == i:
            return ns + s2[i:len(s2)]
        elif len(s2) == i:
            return ns + s1[i:len(s1)]
        else:
            ns = ns + s1[i] + s2[i]
        i += 1
        