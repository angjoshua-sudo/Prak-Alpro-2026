a = input("Masukkan sisi 1: ")
b = input("Masukkan sisi 2: ")
c = input("Masukkan sisi 3: ")

try:
    a = int(a)
    b = int(b)
    c = int(c)

    if a == b and a == c:
        print("3 sisi sama")
    elif a == b or b == c or a == c:
        print("2 sisi sama")
    else:
        print("Tidak ada yang sama")
except:
    print("Input harus berupa angka!")