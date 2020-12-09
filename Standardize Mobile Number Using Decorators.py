def wrapper(f):
    def fun(l):
        f(map(lambda x:'+91 ' + x[-10:-5] + ' ' + x[-5:],l))
    return fun

@wrapper