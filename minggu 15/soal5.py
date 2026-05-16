def kombinasi(n,r):
    if r == 0 or r ==n:
        return 1
    
    return kombinasi(n-1,r-1) + kombinasi(n-1,r)

n = int(input("Masukkan n: "))
r = int(input("Masukkan r: "))

print("Hasil kombiasi adalah", kombinasi(n,r))
