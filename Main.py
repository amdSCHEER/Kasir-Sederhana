print("--- PROGRAM KASIR ---")

harga = int(input("Harga barang: "))
jumlah = int(input("Jumlah beli: "))

total = harga * jumlah

# Mengedit bagian ini untuk potongan harga 
if total > 50000:
    print("Dapat potongan 5000 karena belanja di atas 50rb!")
    total = total - 5000

print("Total bayar:", total)

bayar = int(input("Uang cash: "))

if bayar >= total:
    kembalian = bayar - total
    print("Kembalian anda:", kembalian)
    print("Terima kasih sudah berbelanja!")
else:
    kurang = total - bayar
    print("Uang anda kurang sebesar:", kurang)
