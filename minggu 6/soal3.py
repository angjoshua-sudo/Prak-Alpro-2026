import math
print("Program penghitung IPS Mahasiswa")
jumlah_matkul = int(input("Berapa jumlah mata kuliah? "))

i = 1 
total = 0
error=False

while i <= jumlah_matkul:
    huruf = input(f"Nilai Mk {i}: ")
    i = i + 1

    if huruf == "A":
        nilai = 4
    elif huruf == "B":
        nilai = 3
    elif huruf == "C":
        nilai = 2
    elif huruf == "D":
        nilai = 1
    else:
        print("Nilai harus A, B, C, atau D!")
        error = True
        break

    total += nilai*3

if not error:
    ips = total / (jumlah_matkul*3)

    print(f"Nilai IPS anda semester ini {round(ips,2)}")

