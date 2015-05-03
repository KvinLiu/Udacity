def crawl_web(seed, max_depth):
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth += 1
    return crawled

def crawl_web(seed, max_depth):
    tocrawl = [[seed]]
    crawled = []
    depth = 0
    while depth < max_depth:
        tocrawl.append([])
        while tocrawl[depth]:
            page = tocrawl[depth].pop()
            if page not in crawled:
                union(tocrawl[depth + 1], get_all_links(get_page(page)))
                crawled.append(page)
        depth += 1
    return crawled
