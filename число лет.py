b=input('Введите число лет от 1 до 99 ')
lenb=int(len(b))
if b.isdigit():
    intb = int(b)
    if lenb==2:
        jhk=int(b[1])
        if 1<=jhk<=4:
            print('Мне',b,'года')
        else:
            print('Мне',b,'лет')
    elif lenb==1:
        if 1<=intb<=4:
            print('Мне', b, 'года')
        else:
            print('Мне', b, 'лет')
    else:
        print('Введено задиапозонное число,перезапустите файл')
else:
    print('Введен текст вместо цифр,перезапустите программу')
