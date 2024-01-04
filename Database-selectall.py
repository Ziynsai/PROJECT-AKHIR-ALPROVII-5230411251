# Koneksi DB
import sqlite3
koneksi = sqlite3.connect('Database_hewan_final.db')
kursor = koneksi.cursor()

#Menampilkan Semua Data Dalam Database
kursor.execute("SELECT * FROM HEWAN")
baris_tebel = kursor.fetchall()
#BUAT TABEL PEGAWAI
print("SEMUA DATA HEWAN")
print("="*80)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("id_hewan","nama_hewan","jenis","asal","jml_sekarang","thn_ditemukan"))
print('-'*80)

for baris in baris_tebel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

print("-"*80)
koneksi.close()