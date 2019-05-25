def cetak_gambar(number):
    for x in range(number):
        if x == 0 or x == (number-1):
            print(number*'X ')
        else:
            string2 = (number // 2)*'= '
            print(string2+'X '+string2)
cetak_gambar(31)