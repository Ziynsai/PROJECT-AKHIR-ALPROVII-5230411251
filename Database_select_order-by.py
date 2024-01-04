# urutan berdasarkan alfabet
# Koneksi DB
import sqlite3
koneksi = sqlite3.connect('Database_hewan_final.db')
kursor = koneksi.cursor()

kursor.execute("SELECT * FROM HEWAN ORDER BY nama_hewan ASC ")
baris_tebel = kursor.fetchall()

print("DATA HEWAN DARI URUT ALFABET")
print("="*80)
print('-'*80)

for baris in baris_tebel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20} ".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

print("-"*80)
koneksi.close()

# URUTAN berdasarkan jumlah terbanyak
import sqlite3
koneksi = sqlite3.connect('Database_hewan_final.db')
kursor = koneksi.cursor()

kursor.execute("SELECT * FROM HEWAN ORDER BY jml_sekarang DESC ")
baris_tebel = kursor.fetchall()

print("DATA HEWAN DARI TERBANYAK")
print("="*80)
print('-'*80)

for baris in baris_tebel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20} ".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

print("-"*80)
koneksi.close()

# Urutan berdasarkan tahun terlama
import sqlite3
koneksi = sqlite3.connect('Database_hewan_final.db')
kursor = koneksi.cursor()

kursor.execute("SELECT * FROM HEWAN ORDER BY thn_ditemukanA ASC ")
baris_tebel = kursor.fetchall()

print("DATA HEWAN dari tahun terlama")
print("="*80)
print('-'*80)

for baris in baris_tebel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20} ".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

print("-"*80)
koneksi.close()