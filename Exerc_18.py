i = 0
cont = 0
while True:
    num = int(input('Entre com os valores: '))
    if num > 80:
        if num >= 10:
            if num <= 150:
                cont = cont +1
        break
print('Result: ', num, cont)