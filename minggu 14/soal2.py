print("Pilihan Konversi:")
print("1. Konversi List menjadi Set")
print("2. Konversi Set menjadi List")
print("3. Konversi Tuple menjadi Set")
print("4. Konversi Set menjadi Tuple")
angka = int(input("Masukkan angka untuk memilih jenis konversi: "))

masuk = eval(input("Masukkan data: "))

if angka == 1:
    print(f"Tipe data: List")
    print(masuk)
    hasil = set(masuk)
    print("Tipe data: Set")
    print(hasil)
elif angka == 2:
    print(f"Tipe data: Set")
    print(masuk)
    hasil = list(masuk)
    print("Tipe data: List")
    print(hasil)
elif angka == 3:
    print(f"Tipe data: Tuple")
    print(masuk)
    hasil = set(masuk)
    print("Tipe data: Set")
    print(hasil)
elif angka == 4:
    print(f"Tipe data: Set")
    print(masuk)
    hasil = tuple(masuk)
    print("Tipe data: Tuple")
    print(hasil)
else:
    print("Pilihan tidak valid")
    