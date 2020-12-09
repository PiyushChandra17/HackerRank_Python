import re
v = 'aeiou'
c = 'qwrtypsdfghjklzxcvbnm'
regex = '(?<=[' + c + '])([' + v + ']{2,})[' + c + ']'
match = re.findall(regex,input(),re.I)

if match:
    print(*match,sep='\n')
else:
    print(-1)
