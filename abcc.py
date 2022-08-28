a=float(input('vvedi a'))
b=float(input('vvedi b'))
c=float(input('vvedi c'))
if a+b>c:
    print('moget su64estvovat')# сумма двух сторон треугольника
elif a+c>b:
    print('moget su64estvovat2')
elif b+c>a:
    print('moget su64estvovat3')
else:
    print('net ne moget')