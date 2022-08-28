a=float(input('vvedi a'))
b=float(input('vvedi b'))
c=float(input('vvedi c'))
if a+b>c or a+c>b or c+b>a: # так красивее
    print('может существовать')
else:
    print('не может существовать')