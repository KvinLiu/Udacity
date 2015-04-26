def find_element(l, p):
    if p in l:
        return l.index(p)
    return -1

# make some test
print find_element([1,2,3,4,5], 5)
# should be 4
print find_element(['hello', 'world', 'I', 'am', 'here', '!'], '?')
# should be -1
