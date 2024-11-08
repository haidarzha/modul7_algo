import math
x = False  
def not_prime(n):
    if n == 1:  # khusus untuk angka 1
        print(n, "bukan bilangan prima")
        return
    
    # jika n bilangan genap dan lebih dari 2 maka bukan bilangan prima
    if n % 2 == 0 and n > 2: 
        print(n, "bukan bilangan prima")
        return
    
    # cek pembagi ganjil dari 3 hingga akar kuadrat n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            print(n, "bukan bilangan prima")
            return
    
    # jika tidak ada pembagi, maka n adalah bilangan prima
    is_prime(n)

# fungsi untuk mencetak bahwa n adalah bilangan prima
def is_prime(n):
    print(n, "adalah bilangan prima")

# looping untuk input dari pengguna
while not x:
    print("gunakan 0 untuk stop")
    n = int(input("masukkan angka: "))  # input dari user
    if n == 0:  # stop loop jika user memasukkan 0
        x = True
    else:
        not_prime(n)  # cek apakah n adalah bilangan prima atau tidak?
