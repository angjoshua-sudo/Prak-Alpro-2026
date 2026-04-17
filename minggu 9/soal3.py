kalimat = input("masukkan kalimat: ")
simpan = []



kalimat = kalimat.split(' ')

for kata in kalimat:
    if kata != '':
        simpan.append(kata)

simpan = ' '.join(simpan)
print(f'"{simpan}"')

