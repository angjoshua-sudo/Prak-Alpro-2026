gaji = int(input("Masukkan gaji yang diinginkan: "))
jam_kerja = int(input("Masukkan jumlah jam kerja perminggu: "))

pendapatan1 = gaji * jam_kerja * 5 #pendapatan sebelum kena pajak
pendapatan2 = pendapatan1 - pendapatan1 * 0.14 #pendapatan setelah kena pajak

pengeluaran1 = pendapatan2 * 0.1 #pengeluaran untuk beli pakaian dan aksesoris
pengeluaran2 = pendapatan2 * 0.01 #pengeluaran untuk beli alat tulis

sisa_uang = pendapatan2 - pengeluaran1 - pengeluaran2

pengeluaran3 = sisa_uang * 0.25 #pengeluaran untuk sedekah
sedekah1 = pengeluaran3 * 0.30 #sedekah anak yatim
sedekah2 = pengeluaran3 - sedekah1 #sedekah kaum dhuafa

print(f"1. Pendapatan sebelum pajak: Rp.{pendapatan1:,}")
print(f"2. Pendapatan setelah pajak: Rp.{pendapatan2:,.0f}")   
print(f"3. Pengeluaran untuk beli pakaian dan aksesoris: Rp.{pengeluaran1:,.0f}")
print(f"4. Pengeluaran untuk beli alat tulis: Rp.{pengeluaran2:,.0f}")
print(f"5. Pengeluaran untuk sedekah: Rp.{pengeluaran3:,.0f}")
print(f"6. Sedekah untuk anak yatim: Rp.{sedekah1:,.0f}")
print(f"7. Sedekah untuk kaum dhuafa: Rp.{sedekah2:,.0f}")
