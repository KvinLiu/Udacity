def hashtable_add(htable, key, value):
    hashtable_get_bucket(htable,key).append([key, value])
