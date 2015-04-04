def Hello():
    print "What you want to say: "
    a = raw_input("->>>")
    b = raw_input("-->>")
    return "Hello, %r, %r"  %(a, b)


print Hello()
