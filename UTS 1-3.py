# SOAL NOMOR 1
print("Nomor 1")
kata = input("masukkan kata : ")

balik = ""
for huruf  in kata:
    balik = huruf+balik
print(f"kata '{kata}' saat dibalik menjadi : ",balik)

print("")
print("------------------------")
print("")

# SOAL NOMOR 2
print("Nomor 2")
kalimat = input("Masukkan kalimat/kata : ")
huruf = input("Masukkan huruf yang ingin dicari : ")

kalimat = kalimat.lower()
huruf = huruf.lower()
jumlah = 0
for totalnya in kalimat:
    if totalnya == huruf:
        jumlah +=1

print(f"jumlah huruf '{huruf}' dalam kalimat/kata '{kalimat}' adalah : {jumlah}")

print("")
print("------------------------")
print("")

# SOAL NOMOR 3
print("Nomor 3")
kalimat = input("Masukkan kalimat/kata : ")
karakter = len(kalimat)
print(f"jumlah karakter dalam kalimat/kata '{kalimat}' adalah : {karakter}")
