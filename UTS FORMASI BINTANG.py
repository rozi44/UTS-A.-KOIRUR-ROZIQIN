# NOMOR 1
print("Nomor 1 :")
baris = 6
for i in range(baris):
    sisi = baris - i
    tengah = i * 2
    print("*" * sisi + " " * tengah + "*" * sisi)

print()

# NOMOR 2
print("nomor 2 :")
baris = 6
for i in range(1, baris, + 1):
    spasi = baris - i
    bintang = i * 2 - 1
    print(" " * spasi + "*" * bintang)

print()

# NOMOR 3
print("nomor 3 :")
for i in range(1, 4):
    print("*" * i)
for i in range(1, 4):
    print(" " * (3 - i) + "*" * i)

print()

# NOMOR 4
print("Nomor 4 :")
baris = 6
for i in range(1, baris, +1):
    kiri = "*" * i
    spasi = " " * (baris - i) * 2
    kanan = "*" * i
    print(kiri + spasi + kanan)
print("*" * (baris * 2+1))

print()

# NOMOR 5
print("nomor 5 :")
baris = 6
for i in range(baris, 0, -1):
    spasi = baris - i
    bintang = i * 2 - 1
    print(" " * spasi + "*" * bintang)

print()

# NOMOR 6
print("nomor 6 :")
for i in range(1, 4):
    print(" " * (3 - i) + "*" * i)
for i in range(1, 3):
    print("*" * i)
print()
print("*" * 3)

print()

print("nomor 7 :")
print(" "+"*" * 5)
print()
baris = 4
baris2 = 5
for i in range(baris, 0, -1):
    print(" " * (baris - i + 2) + "*" * i)
for i in range(2, baris2 + 1):
    print(" " * (baris2 - i + 1) + "*" * i)

print()

# NOMOR 8
print("nomor 8 :")
baris = 4
kolom = 10
print("0" + "*" * (kolom))
print()
for i in range(baris):
    print("0" + "*" * kolom)
print("0" * (kolom + 1))

print()

# NOMOR 9
print("nomor 9 :")
baris = 4
kolom = 10
for i in range(baris):
    print("*" * kolom)
    print("0")

print("0" * kolom)
print("0")

print()

# NOMOR 10
print("nomor 10 :")
baris1 = 5
baris2 = 6
print("*" * baris2)
print()
for i in range(baris1, 0, -1):
    print("*" * i)
for i in range(2, baris2):
    print("*" * i)

print()

# NOMOR 11
print("nomor 11 :")
baris = 5 
kolom = 10
print("0" * (kolom + 1))
for i in range(baris):
    print("0" + "*" * kolom)

print()

# NOMOR 12
print("nomor 12 :")
baris = 5
kolom = 10
print("0" * kolom)
print("0")
for i in range(baris):
    print("*" * kolom)
    print(0)

print()

# NOMOR 13
print("nomor 13 :")
baris = 6
for i in range(baris):
    print("0" * (i + 1) + "*" * (baris - i))

print()

# NOMOR 14
print("nomor 14 :")
baris = 6
for i in range(baris):
    print("*" * (i + 1) + "0" * (baris - i))

print()

# NOMOR 15
print("nomor 15 :")
baris = 6
for i in range(baris):
    print("0" * (baris - i) + "*" * (i + 1))

print()

# NOMOR 16
print("nomor 16 :")
baris = 6
for i in range(baris):
    print("0" * (baris - i) + "*" * (i + 1))

print()

# NOMOR 17
print("nomor 17 :")
baris = 6
for i in range(baris):
    print("0" * (baris - i) + "*" + "0" * i)

print()

# NOMOR 18
print("nomor 18 :")
baris = 6
for i in range(baris):
    print("0" * i + "*" + "0" * (baris - i))

print()

# NOMOR 19
print("nomor 19 :")
baris = 6
kolom = 7

for i in range(baris):
    if i == 0 or i == baris - 1:
        print("0" * kolom)
    else:
        print("0" + "*" * (kolom - 2) + "0")

print()

# NOMOR 20
print("nomor 20 :")
baris = 6
for i in range(baris):
    if i % 3 == 0:
        print("0" * 7)
    elif i % 3 == 1:
        print("*" * 7)
    else:
        print("=" * 7)
