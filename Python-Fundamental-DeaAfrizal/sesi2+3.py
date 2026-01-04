import random
from libr import welcome_message

welcome_message("Welcome to my game!!!")

user_name = input("Masukan namamu: ")
keputusan = input(f"Halo {user_name}, Apakah kamu ingin bermain game? [y/n] ")

while keputusan != "y" and keputusan != "n":
    keputusan = input("Pilih diantara [y/n]: ")
    
if keputusan == "y" :
    print("Oke, mari kita bermain tebak angka")
elif keputusan == "n" :
    print("Baiklah, mungkin kita bisa bermain lain waktu")
    exit()

while True:
    angka = random.randint(1, 3)
    user_answer = int(input("pilih angka diantara 1 - 3: "))

    if angka == user_answer :
        print(f"Selamat {user_name} tebakanmu benar, angka dari tebakan adalah {angka} !!!")
    elif angka != user_answer and angka <= 3 and angka >= 1 :
        print(f'''Maaf {user_name}, tebakanmu salah
        Jawaban yang benar adalah {angka}, sedangkan jawabanmu adalah {user_answer}''')
    while angka < 1 and angka > 3 :
        angka = input("Pilih diantara 1-3: ")
        
    playing = input(f"Apakah kamu ingin melanjutkan permainan?[y/n]: ")
    while playing != "y" :
        if playing == "n" :
            break
        playing = input("Masukan jawaban antara [y/n]: ")