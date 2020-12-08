import re
def fun(s):
    a = re.match(r'[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$',s)
    return (a)

def filter_mail(emails):