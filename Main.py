print("--- PROGRAM KASIR ---")

harga = int(input("Harga barang: "))
jumlah = int(input("Jumlah beli: "))

total = harga * jumlah
print("Total bayar:", total)

bayar = int(input("Uang cash: "))

# Mengedit bagian ini agar bisa cek uang kurang
if bayar >= total:
    kembalian = bayar - total
    print("Kembalian anda:", kembalian)
else:
    kurang = total - bayar
    print("Uang anda kurang sebesar:", kurang)
