saldo_awal = 5000
hutang = 50000

print('saldo ' + str(saldo_awal))
deposit = input('mau deposit berapa? ')

saldo_deposit = int(saldo_awal) + int(deposit)
keputusan = hutang - saldo_deposit

if keputusan < 0 :
    print('selamat utangmu lunas')
    print('saldo sekarang: ' + str(keputusan * -1))
elif keputusan >= 0 :
    print('kamu masih memiliki hutang!!')
    print('hutang tersisa: ' + str(keputusan))
else :
    print('error output')