BMI = float(input("masukkan target BMi yang diinginkan: "))
tinggi = float(input("masukkan tinggi badan dalam meter: "))
berat = BMI * (tinggi**2)

print(f"Berat badan yang dibutuhkan untuk mencapai BMI adalah {berat:.2f} kg")

