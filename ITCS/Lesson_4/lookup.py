index = [['udacity', ['http://www.udacity.com', 'http://www.udacity.com/login']], ['baidu', ['http://www.baidu.com', 'http://www.baidu.com/login']]]

def lookup(index, keyword):
    for i in index:
        if keyword == i[0]:
            return i[1]
    return []
