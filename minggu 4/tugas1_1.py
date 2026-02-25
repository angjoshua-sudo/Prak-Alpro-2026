pembelian = input()

try:
    pembelian = int(pembelian)
    if pembelian >= 100000:
        print ("True")
    else:
        print ("False")
except:     
    print("input harus berupa angka!")
