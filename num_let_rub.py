#!/usr/bin/python3

rubl = [ 'ей', 'ь', 'я', 'я', 'я', 'ей' ]
kope = [ 'ек', 'йка', 'йки', 'йки', 'йки', 'ек' ]

tmm = [ 'тысяч', 'миллион', 'миллиард' ]

tmm2 = [ [ ' ', 'а ', 'и ', 'и ', 'и ', ' ' ],
        [ 'ов ', ' ', 'а ', 'а ', 'а ', 'ов ' ],
        [ 'ов ', ' ', 'а ', 'а ', 'а ', 'ов ' ] ]

words = [ [ 'ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать' , 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать' ], 
        [ '', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто' ],
        [ '', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот' ] ]

def five(x):
    if x > 5:
        return 5
    else:
        return x

if __name__ == '__main__':
    print('\nВведите число: ', end = '')
    number = input()
    number = number.replace(',', '.')
    if number.split('.')[0].lstrip('0'):
        rubli = number.split('.')[0].lstrip('0')[::-1]
    else:
        rubli = '0'
    try:
        kopeyki = number.split('.')[1][::-1].zfill(2)
    except:
        kopeyki = '0'

    if len(rubli) > 12:
        print('\nЧисло больше или равно триллиону. Слишком большое.\n')
        exit()

    # РУБЛИ
    res = ''
    for c, x in enumerate(rubli):
        if ((len(rubli) > 1 and (c + 1 == 1)) or (len(rubli) > 4 and (c + 1 == 4)) or (len(rubli) > 7 and (c + 1 == 7)) or (len(rubli) > 10 and (c + 1 == 10))) and rubli[c + 1] == '1':
            x = rubli[c + 1] + x
        x = int(x)

        if c in [6, 9, 12] and not int(rubli[c - 1]) and not int(rubli[c - 2]) and not int(rubli[c - 3]):
            res_tmp = ''
            for word in res.split(' ')[1:]:
                res_tmp += word + ' '
            res = res_tmp[:-1]

        if (x or len(rubli) == 1) and words[c % 3][x]:
            res = ('две' if c == 3 and x == 2 else ('одна' if c == 3 and x == 1 else str(words[c % 3][x]))) + (' ' + tmm[c // 3 - 1] + tmm2[c // 3 - 1][five(x)] if c in [3, 6, 9] else ' ') + res
        elif c in [3, 6, 9]:
            res = tmm[c // 3 - 1] + tmm2[c // 3 - 1][five(x)] + res

    if len(rubli) > 1 and rubli[1] == '1':
        y = rubli[1] + rubli[0]
    else:
        y = rubli[0]
    res += 'рубл' + rubl[five(int(y))] + ','

    # КОПЕЙКИ
    res1 = ''
    for c, x in enumerate(kopeyki):
        if (len(kopeyki) > 1 and (c + 1 == 1)) and kopeyki[c + 1] == '1':
            x = kopeyki[c + 1] + x
        x = int(x)

        if (x or len(kopeyki) == 1) and words[c % 2][x]:
            res1 = ('две' if c == 0 and x == 2 else ('одна' if c == 0 and x == 1 else str(words[c % 2][x])))  + ' ' + res1

    if len(kopeyki) > 1 and kopeyki[1] == '1':
        y = kopeyki[1] + kopeyki[0]
    else:
        y = kopeyki[0]

    if not res1:
        res1 = 'ноль '
    
    #res1 = kopeyki[::-1] + ' ' # копейки числом

    res1 += 'копе' + kope[five(int(y))]

    print(res, res1, '\n')
