def kombinasi(m, n):
    if n==0 or n==m:
        return 1
    
    return kombinasi(m-1, n-1) + kombinasi(m-1, n)

try: 
    m = int(input("Masukkan nilai m: ")) 
    n = int(input("Masukkan nilai n: ")) 
    print(kombinasi(m, n)) 
except: 
    print("Inputan salah!")