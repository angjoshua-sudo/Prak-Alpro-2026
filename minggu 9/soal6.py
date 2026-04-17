import random
import string
kalimat = input("Masukkan kalimat: ")
mail =[]
nama = []

kata = kalimat.split()
for i in kata:
    bersih = i.strip(".,!?;:'\"()")

    if "@" in bersih:
        mail.append(bersih)

for j in mail:
    depan = j.split("@")[0]
    nama.append(depan)

    karakter = string.ascii_letters + string.digits
    password = ''

    for l in range(8):
        password += random.choice(karakter)

    print(f'{j} username: {depan} , password: {password}')      

#Berikut adalah daftar email dan nama pengguna dari mailing list: anton@mail.com dimiliki oleh antonius budi@gmail.co.id dimiliki oleh budi anwari slamet@getnada.com dimiliki oleh slamet slumut matahari@tokopedia.com dimiliki oleh toko matahari