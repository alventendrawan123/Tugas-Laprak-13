def palindrom(kalimat): 
    if len(kalimat) < 2: 
        return True 
    if kalimat[0] == kalimat[-1]: 
        return palindrom(kalimat[1:-1]) 
    return False 
try: 
    tes = input("Masukkan sebuah kalimat: ") 
    tes = tes.replace(' ', '').lower() 
    if palindrom(tes): 
            print("Kalimat yang andda masukkan adalah palindrom.") 
    else: 
        print("Ini bukan kalimat palindrom.") 
except : 
    print("input yang anda masukkan salah")