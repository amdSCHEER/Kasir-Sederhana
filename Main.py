print("--- PROGRAM KASIR ---")

harga = int(input("Harga barang: "))
jumlah = int(input("Jumlah beli: "))

total = harga * jumlah
print("Total bayar:", total)

bayar = int(input("Uang cash: "))
kembalian = bayar - total

print("Kembalian anda:", kembalian)