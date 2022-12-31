a = input('Введите слово: ')

b = a[0]

if b == 'a' or b == 'e' or b == 'u' or b == 'i' or b == 'o':
    print(a + 'way')
else:
    print(a[1:] + a[0] + 'ay')
