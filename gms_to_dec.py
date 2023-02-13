g = int(input('Введите градусы : '))
m = int(input('Введите минуты : '))
s = float(input('Введите секунды : '))

def gms_to_dec(g, m, s):
    if 0 <= g < 360 and 0 <= m < 60 and 0 <= s < 60:
        return(g + m / 60 + s / 3600)
    else:
        return('Неверный формат ввода данных')
dec = round(gms_to_dec(g, m, s), 8)
print(dec)

input()
