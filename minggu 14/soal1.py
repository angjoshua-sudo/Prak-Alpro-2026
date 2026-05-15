n = int(input("Masukkan jumlah kategori: "))

data_aplikasi = {}
for i in range(n):
    nama_kategori = input("Masukkan nama kategori: ")
    print('Masukkan 5 nama aplikasi di kategoti', nama_kategori)

    aplikasi = []
    for j in range(5):
        nama_aplikasi = input("Nama aplikasi: ")
        aplikasi.append(nama_aplikasi)
    
    data_aplikasi[nama_kategori] = aplikasi

daftar_aplikasi_list = []

for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))

hasil = daftar_aplikasi_list[0]
for i in range(1,len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])

tabel = {}
for i in daftar_aplikasi_list:
    for j in i:
        tabel[j] = tabel.get(j,0) + 1

unik = []
sama2 = []
for key, value in tabel.items():
    if value == 2:
        sama2.append(key)
    elif value == 1:
        unik.append(key)
        
print(f"Aplikasi yang muncul di semua kategori adalah: \n{hasil}")
print(f"Aplikasi yang muncul di satu kategori adalah: \n{unik}")
print(f"Aplikasi yang muncul di dua kategori adalah: \n{sama2}")
