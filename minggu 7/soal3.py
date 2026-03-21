tinggi = int(input('masukkan tinggi: '))
lebar = int(input('masukkan lebar: '))

print(f"tinggi = {tinggi}, lebar = {lebar}")

l = tinggi * lebar
awal = 1
akhir = lebar
for i in range(1, tinggi+1):
    for j in range(awal, akhir+1):
        print(j, end=" ")
    print()
    awal += lebar
    akhir += lebar

