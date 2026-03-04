def cek_digit_belakang(d1, d2, d3):
    d1 = d1 % 10
    d2 = d2 % 10
    d3 = d3 % 10

    if d1 == d2 or d2 == d3 or d1 == d3:
        return True
    else:
        return False

print(cek_digit_belakang(30, 20, 18))
print(cek_digit_belakang(145, 5, 100))
print(cek_digit_belakang(71, 187, 18))
print(cek_digit_belakang(1024, 14, 94))
print(cek_digit_belakang(53, 8900, 658))