# Koneksi DB
import sqlite3
koneksi = sqlite3.connect('Database_hewan_final.db')
kursor = koneksi.cursor()

# where jenis = mamalia
kursor.execute("SELECT * FROM HEWAN WHERE jenis = 'Mamalia' AND Jml_sekarang <= '1000' ")
baris_tebel = kursor.fetchall()
#BUAT TABEL PEGAWAI
print("DATA HEWAN MAMALIA dan KURANG ATAU SAMA DENGAN 1000 EKOR")
print("="*80)
print('-'*80)

for baris in baris_tebel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20} ".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

print("-"*80)
koneksi.close()