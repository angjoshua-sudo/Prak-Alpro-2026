kalimat = input("masukkab kalimat: ")
cari = input("masukkan jumlah kata yang ingin dicari: ")
hasil = 0

kalimat = kalimat.lower()
kalimat = kalimat.split(" ")
cari = cari.lower()

for kata in kalimat:
    kata = ''.join([i for i in kata if i.isalpha()])
    if kata == cari:
        hasil += 1

print(F'kata {cari} ada {hasil} buah') 