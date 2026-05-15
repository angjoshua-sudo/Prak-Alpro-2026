data = eval(input("Data: "))
data_nim = ()
data_nama_depan =()

nama, nim, alamat = data
for i in nim:
    data_nim += (i,)

bagi_nama = nama.split()
nama_depan = bagi_nama[0]
for i in range (1, len(nama_depan)):
    data_nama_depan += (nama_depan[i],)

print()
print(f"NIM    : {nim}")
print(f"NAMA   : {nama}")
print(f"ALAMAT : {alamat}")
print()
print(f"NIM: {data_nim}")
print()
print(f"NAMA DEPAN: {data_nama_depan}")
print()
print(f"NAMA TERBALIK: {bagi_nama[::-1]}")
