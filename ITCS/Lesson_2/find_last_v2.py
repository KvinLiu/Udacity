def find_last(s,r):
    if s.find(r) == -1:
       return -1
    else:
       n = 0
       while s.find(r,n) != -1:
             n = n + 1
       return n - 1





#print find_last('aaaa', 'a')
#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 3

#print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0




