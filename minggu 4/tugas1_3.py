a = input("Masukkan bilangan pertama: ")
b = input("Masukkan bilangan kedua: ")
c = input("Masukkan bilangan ketiga: ")

try:
    a = int(a)
    b = int(b)
    c = int(c)
    
    if a > b and a > c:
        print("Terbesar : ",a)
    elif b > a and b > c:
        print("Terbesar : ",b)
    elif c > a and c > b:
        print("Terbesar : ",c)
    else:
        print("Ada bilangan yang sama besar")
except:
    print("Input harus berupa angka!")