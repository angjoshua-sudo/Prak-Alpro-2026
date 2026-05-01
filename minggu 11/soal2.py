temp = []
while True:
    angka = input("Masukkan angka: ")
    if angka == "done":
        break
    else:
        x = int(angka)
        temp.append(x)

total = 0
for i in range(len(temp)):
    total += temp[i]

akhir = total/len(temp)
print(f'Rata-rata dari bilangan tersebut adalah: {akhir}')
