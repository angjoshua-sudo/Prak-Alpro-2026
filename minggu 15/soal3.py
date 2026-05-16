def ganjil(angka):
    if angka <= 0:
        return 0
    
    if angka % 2 == 0:
        return ganjil(angka-1)
    
    return angka + ganjil(angka-2)
    

angka = int(input("Masukkan angka: "))
print("Hasil deret ganjil adalah",ganjil(angka))
