def print_formatted(n):
    width = len('{0:b}'.format(n))
    for i in range(1,n+1):
        print('{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}'.format(i=i,width=width))
if __name__ == '__main__':