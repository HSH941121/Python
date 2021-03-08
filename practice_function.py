x=10
y=3

def get(a,b):
    c = a // b
    d = a % b
    return c,d

quotient, remainder = get(x,y)
print('몫: {0}, 나머지: {1}'.format(quotient,remainder))
