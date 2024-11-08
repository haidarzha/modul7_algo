print("Ordinal number")
x = False

def make_ordinal(n):
    if n == 0:
        return
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    print("(", n, ",", '"', suffix, '"', ")")

while not x:
    print("Ketik 0 untuk menghentikan program")
    n = int(input("Masukkan angka: "))
    if n == 0:
        x = True
    else:
        make_ordinal(n)
