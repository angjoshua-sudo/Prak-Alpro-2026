bilangan = input("Masukkan suatu bilangan: ")

try:
    bilangan = int(bilangan)
    hasil = "Positif" if bilangan > 0 else "Negatif" if bilangan < 0 else "Nol" 
except:
    hasil = "Bilangan harus berupa angka!" 