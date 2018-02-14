def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
    if len(L1) != len(L2):
        return False
    elif (L1 == []) and (L2 == []):
        return (None,None,None)
    dictL1 = {}
    dictL2 = {}
    for el1 in L1:
        if el1 in list(dictL1.keys()):
            dictL1[el1] += 1
        else:
            dictL1[el1] = 1
    for el2 in L2:
        if el2 in list(dictL2.keys()):
            dictL2[el2] += 1
        else:
            dictL2[el2] = 1    
    if dictL1 == dictL2:
        keyMaximum = max(dictL1, key=lambda k: dictL1[k])
        return (keyMaximum, dictL1[keyMaximum], type(keyMaximum))
    else:
        return False
            