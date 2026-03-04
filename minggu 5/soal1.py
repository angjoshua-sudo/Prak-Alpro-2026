def cek_angka(a1, a2 ,a3):
    if a1 == a2 or a2 == a3 or a1 == a3:
        return False
    elif a1 + a2 != a3 and a1 + a3 != a2 and a2 + a3 != a1:
        return False
    else:
        return True

print(cek_angka(1, 2, 3))
print(cek_angka(2, 2, 4)) 
print(cek_angka(1, 4, 6))
