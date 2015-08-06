def hash_string(keyword, bucket):
    a = 0
    for i in keyword:
        a += ord(i)
    return a % bucket

def hash_string_v2(keyword, bucket):
    a = 0
    for c in keyword:
        a = (a + ord(c)) % bucket
    return a
