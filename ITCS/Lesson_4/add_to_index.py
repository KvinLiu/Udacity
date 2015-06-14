def add_to_index(index, keyword, url):
    for i in index:
        if i[0] == keyword:
            i[1].append(url)
            return
    index.append([keyword, [url]])
