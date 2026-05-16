def polindrom(kalimat):
    kalimat = kalimat.lower()
    kalimat = kalimat.replace(' ','')

    if len(kalimat) <=1:
        return(f"Kalimat adalah polindrom")
    
    if kalimat[0] != kalimat[-1]:
        return(f"Kalimat bukan polindrom")
    
    return polindrom(kalimat[1:-1])

kalimat = input("Masukkan kalimat: ")
print(polindrom(kalimat))
