import random

print('WELCOME TO PLAYGROUND!')

user_name = input("Masukan namamu: ")
keputusan = input(f"Halo {user_name}, Apakah kamu ingin bermain game? [y/n] ")

if keputusan == "y" :
    print("Oke, mari kita bermain tebak angka")
elif keputusan == "n" :
    print("Baiklah, mungkin kita bisa bermain lain waktu")
    exit()
else :
    print('''Pilih diantara [y/n] !!!''')
    exit()
angka = random.randint(1, 3)
user_answer = int(input("pilih angka diantara 1 - 3: "))

if angka == user_answer :
    print(f"Selamat {user_name} tebakanmu benar, angka dari tebakan adalah {angka} !!!")
elif angka < 1 and angka > 3 :
    print("Pilih diantara 1 - 10!!")
else :
    print(f'''Maaf {user_name}, tebakanmu salah 
Jawaban yang benar adalah {angka}, sedangkan jawabanmu adalah {user_answer}''')
print("Terimakasih sudah bermain, sampai jumpa lagi")