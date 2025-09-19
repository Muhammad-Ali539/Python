a=int(input('Enter a Number:'))
b=int(input('Enter a Number:'))
c=int(input('Enter a Number:'))
if a>b and a>c:
    print('a is largest')
elif b>a and b>c:
    print('B is largest')
elif c<a and c>b:
    print('C is largest')
else:
    print('Some numbers are equal')