kalimat = input("Masukkan kalimat: ")

kalimat = kalimat.split(' ')

pendek=kalimat[0]
panjang=kalimat[0]

for kata in kalimat:
    kata = ''.join([i for i in kata if i.isalpha()])
    if len(kata) < len(pendek):
        pendek = kata
    if len(kata) > len(panjang):
        panjang = kata

print(f'terpendek: {pendek}, terpanjang: {panjang}')