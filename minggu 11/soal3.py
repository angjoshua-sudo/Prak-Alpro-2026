import re

file = input("Masukkan file: ")
try:
    handle = open(file)

    temp = []
    unik = []
    hasil = ''

    for line in handle:
        x = line.lower()
        x = re.sub(r'-', ' ', x)
        x = re.sub(r'[^a-zA-Z\s]', '', x)
        x = re.sub(r'\s+', ' ', x).strip()
        y = x.split()
        temp.extend(y)

    for k in temp:
        if k != '' and temp.count(k) == 1:
            unik.append(k)

    if len(unik) == 0:
        hasil = "tidak ada"
    elif len(unik) == 1:
        hasil = unik[0]
    elif len(unik) == 2:
        hasil = unik[0] + " dan " + unik[1]
    else:
        hasil =", ".join (unik[:-1]) + ', dan ' + unik[-1]

    print(f'Kata uniknya adalah: {hasil}.')

except:
    print("File tidak ditemukan.")
    