# NOMOR 22
n = (int(input("Nomor 21 Masukkan angka : ")))
angka = [str(i) for i in range(n, 0, -1)]
hasil = 1
for i in range(1, n+1):
    hasil *= i
print(f"{n}! = {' x '.join(angka)} = {hasil}")

# NOMOR 23
maksimal = (int(input("Nomor 22 Masukkan angka maksimal : ")))

a, b = 0, 1
print("Deret Fibonacci : ")

while a <= maksimal:
    print(a, end=" ")
    a, b = b, a+b
print()

# NOMOR 24
n_awal = int(input("Nomor 24 Masukkan angka awal: "))
n_akhir = int(input("Nomor 24 Masukkan angka akhir: "))

print(f"Bilangan yang habis dibagi 3 dari bilangan {n_awal} hingga {n_akhir} adalah:")

for i in range(n_awal, n_akhir + 1):
    if i % 3 == 0:
        print(i, end=" ")
print()

# NOMOR 25
n_awal = int(input("Nomor 25 Masukkan angka awal: "))
n_akhir = int(input("Nomor 25 Masukkan angka akhir: "))

print(f"Bilangan yang habis dibagi 4 dari bilangan {n_awal} hingga {n_akhir} adalah:")

for i in range(n_awal, n_akhir + 1):
    if i % 4 == 0:
        print(i, end=" ")
print()

# NOMOR 26
n_awal = int(input("Nomor 26 masukkan angka awal: "))
n_akhir = int(input("Nomor 26 masukkan angka akhir: "))

total = 0

for i in range(n_awal, n_akhir + 1):
    total += i   # sama seperti total = total + i

print(f"Total bilangan bulat dari {n_awal} hingga {n_akhir} adalah {total}")

# NOMOR 27
n_awal = int(input("Nomor 27 masukkan angka awal: "))
n_akhir = int(input("Nomor 27 asukkan angka akhir: "))

total = 0

for i in range(n_awal, n_akhir + 1):
    if i % 2 == 0:
        total += i

print(f"Total bilangan genap dari {n_awal} hingga {n_akhir} adalah {total}")

# NOMOR 28
n_awal = int(input("Nomor 28 masukkan angka awal: "))
n_akhir = int(input("Nomor 28 asukkan angka akhir: "))

total = 0

for i in range(n_awal, n_akhir + 1):
    if i % 2 != 0:
        total += i

print(f"Total bilangan ganjil dari {n_awal} hingga {n_akhir} adalah {total}")

# NOMOR 29
n_awal = int(input("Nomor 29 masukkan angka awal: "))
n_akhir = int(input("Nomor 29 masukkan angka akhir: "))

print(f"Bilangan prima dari {n_awal} hingga {n_akhir} adalah:")

for num in range(n_awal, n_akhir + 1):
    if num > 1:  # bilangan prima mulai dari 2
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

# NOMOR 30
n_awal = int(input("Nomor 30 masukkan angka awal: "))
n_akhir = int(input("Nomor 30 masukkan angka akhir: "))

total = 0

for num in range(n_awal, n_akhir + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            total += num

print(f"Jumlah total bilangan prima dari {n_awal} hingga {n_akhir} adalah {total}")
