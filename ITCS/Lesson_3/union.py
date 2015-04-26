def union_1(l1, l2):
    a = 0
    while a < len(l2):
        if l2[a] not in l1:
            l1.append(l2[a])
        a += 1
    return l1

def union_2(l1, l2):
    for e in l2:
        if e not in l1:
            l1.append(e)
    return l1
