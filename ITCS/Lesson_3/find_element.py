def find_element(p,t):
    i = 0
    while i < len(p):
        if p[i] == t:
            return i
        i += 1
    return -1

def find_elemnt_1(p,t):
    i = 0
    for e in p:
        if e == t:
            return i
        i += 1
    return -1
