angka= input("masukkan list angka: ")
temp = []

angka = angka.split(",")    
for i in range(len(angka)):
    angka[i] = angka[i].strip()
    angka[i] = angka[i].strip('[]')
    x = int(angka[i])
    temp.append(x)

temp.sort(reverse=True)

print(f"3 angka terbaik adalah: {temp[0]}, {temp[1]}, dan {temp[2]}.")

