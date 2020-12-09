import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    maxdepth = max(maxdepth,level+1)

    for child in elem:
        depth(child,level+1)

if __name__ == '__main__':