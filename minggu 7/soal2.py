n = int(input("masukkan nilai n: "))
print(f"n = {n}")

for i in range(n, 0, -1):
    hasil = 1
    for j in range(i, 0, -1):
        hasil *=  j
    print(hasil, end=" ")

    for k in range(i, 0, -1):
        print(k, end=" ")
    print()
