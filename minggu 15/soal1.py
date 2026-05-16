def prima(n, bagi = 2):
    if n <= 1 :
        return(f"{n} bukan bilangan prima")
    if bagi == n :
        return(f"{n} adalah bilangan prima")
    if n % bagi == 0:
        return(f"{n} bukan bilangan prima")
    
    return prima(n, bagi+1)

n = int(input("Masukkan bilangan yang mau di cek prima atau bukan: "))
print(prima(n))
