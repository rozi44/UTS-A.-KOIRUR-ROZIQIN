# SOAL NOMOR 4
hasil = ""
for i in range(1,7):
    hasil += str(i) * i
print("Nomor 4  : " ,hasil)

# SOAL NOMOR 5
hasil = ""
for i in range(6, 0, -1):
    hasil += str(i) * i
print("Nomor 5  : " ,hasil)

# SOAL NOMOR 6
hasil = ""
for i in range(1, 7):
    for j in range(1, i + 1):
        hasil += str(j)
print("Nomor 6  : " ,hasil)

#SOAL NOMOR 7
hasil = ""
for i in range(6, 0, -1):
    for j in range(i, 0, -1):
        hasil += str(j)
print("Nomor 7  : ", hasil)

# NOMOR 8
hasil = ""
hasil += "1"*2
hasil += "2"
hasil += "3"*3
hasil += "".join(str(i) for i in range(1, 5))
hasil += "5"*5
hasil += "".join(str(i) for i in range(1, 7))
print("Nomor 8  : ", hasil)

# NOMOR 9
hasil = ""
hasil += "1"
hasil += "2"*2
hasil += "".join(str(i) for i in range(1, 4))
hasil += "4"*4
hasil += "".join(str(i) for i in range(1, 6))
hasil += "6"*6
print("Nomor 9  : ", hasil)

# NOMOR 10
hasil = ""
hasil += "".join(str(i) for i in range(6, 0, -1))
hasil += "5"*5
hasil += "".join(str(i) for i in range(4, 0, -1))
hasil += "3"*3
hasil += "2"
hasil += "1"*2
print("Nomor 10 : ", hasil)

# NOMOR 11
hasil = ""
hasil += "6"*6
hasil += "".join(str(i) for i in range(1, 6))
hasil += "4"*4
hasil += "".join(str(i) for i in range(1, 4))
hasil += "2"*2
hasil += "1"
print("Nomor 11 : ", hasil)

# NOMOR 12
hasil = ""
hasil += "1"
hasil += "2"*2
hasil += "".join(str(i) for i in range(1, 4))
hasil += "".join(str(i) for i in range(1, 4))
hasil += "5"*5
hasil += "6"*6
hasil += "".join(str(i) for i in range(1, 8))
hasil += "".join(str(i) for i in range(1, 9))
hasil += "9"*9
print("Nomor 12 : ", hasil)

# NOMOR 13
hasil = ""
hasil += "1"*2
hasil += "2"
hasil += "3"*3
hasil += "4"*4
hasil += "".join(str(i) for i in range(1, 6))
hasil += "".join(str(i) for i in range(1, 7))
hasil += "7"*7
hasil += "8"*8
hasil += "".join(str(i) for i in range(1, 10))
print("Nomor 13 : ", hasil)

# NOMOR 14
hasil=(
    "8"*8 + "7"*7 +
    "".join(str(i) for i in range(6, 0, -1))+
    "".join(str(i) for i in range(5, 0, -1))+
    "4"*4 + "3"*2 + "2" + "1"*2
)
print("Nomor 14 : ", hasil)

# NOMOR 15
hasil=(
    "".join(str(i) for i in range(8, 0, -1))+
    "".join(str(i) for i in range(7, 0, -1))+
    "6"*6 + "5"*5+
    "".join(str(i) for i in range(4, 0, -1))+
    "".join(str(i) for i in range(3, 0, -1))+
    "2"*2 + "1"
)
print("Nomor 15 : ", hasil)

# NOMOR 16
angka = 1
hasil = ""

for i in range(12):
    hasil += str(angka) + " "

    if i % 2 == 0:
        angka += 4
    else:
        angka -= 2
print("Nomor 16 : ", hasil.strip())

# NOMOR 17
angka = 2
hasil = ""

for i in range(10):
    hasil += str(angka) + " "

    if i % 2 == 0:
        angka += 10
    else:
        angka -= 5
print("Nomor 17 : ", hasil.strip())

# NOMOR 18
angka = 5
hasil = ""

for i in range(12):
    hasil += str(angka) + " "

    if i % 2 == 0:
        angka -= 3
    else:
        angka += 5
print("Nomor 18 : ", hasil.strip())

# NOMOR 19
angka = 3
hasil = ""

for i in range(10):
    hasil += str(angka) + " "

    if i % 2 == 0:
        angka *= 3
    else:
        angka -= 5
print("Nomor 19 : ", hasil.strip())

# NOMOR 20
angka = 1
hasil = ""

for i in range(13):
    hasil += str(angka) + " "

    angka += (i % 3) + 1
print("Nomor 20 : ", hasil.strip())

# NOMOR 21
angka = 1
hasil = ""

for i in range(10):
    hasil += str(angka) + " "

    angka *= 2
print("Nomor 21 : ", hasil.strip())

