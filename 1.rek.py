def prima(n, i=2): 
    if n == 2: 
        return True 
    elif n < 2 or n % i == 0: 
        return False 
    elif i * i > n: 
        return True 
    else: 
        return prima(n, i + 1) 

def tes_prima(): 
    
    try: 
        n = int(input("Masukkan bilangan: ")) 
        if prima(n): 
            print(f"Bilangan {n} adalah bilangan prima.") 
        else: 
            print(f"Bilangan {n} bukan bilangan prima.") 
    except ValueError: 
        print("Inputan wajib bilangan bulat.") 
tes_prima() 