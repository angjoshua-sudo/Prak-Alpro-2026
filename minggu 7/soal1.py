n = int(input("masukkan bilangan yang ingin dicari prima terdekatnya: "))

if n <= 2:
    print(f"tidak ada bilangan prima yang lebih kecil dari: {n}")
else:
    for i in range(n-1, 1, -1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(f"input n={n}, maka prima terdekat < {n} adalah {i}")
            break
