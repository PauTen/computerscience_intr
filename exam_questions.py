def flatten(aList):
    output_list = []
    for element in aList:
        if isinstance(element,list):
            a = flatten(element)
            output_list = output_list + a
        else:
            output_list.append(element)
    return output_list




def applyF_filterG(L, f, g):
    list_f = list(map(f,L))
    list_g = list(map(g,list_f))
    ind = 0
    for element in list_g:
        if not element:
            L.pop(ind)
        else:
            ind += 1
            
    if L == []:
        output = -1
    else:
        output = max(L)
        
    return output

def f(i):
    return i + 2
def g(i):
    return i > 5

L = [-1,-8,0,2]
print(L)
print(applyF_filterG(L, f, g))
print(L)