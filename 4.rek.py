def hitung_jumlah_digit(digit):
    if digit < 10:
        return digit
    else:
        return digit % 10 + hitung_jumlah_digit(digit // 10)
    
try: 
    n = int(input("Masukkan sebuah bilangan: ")) 
    print(hitung_jumlah_digit(n)) 
except: 
    print("Input harus berupa bilangan bulat.")