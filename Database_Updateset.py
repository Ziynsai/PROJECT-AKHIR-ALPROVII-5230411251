# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('Database_hewan_final.db')
cursor = conn.cursor()

# Data yang ingin diubah
id_hewan = 1 
jumlah_baru = 900

# Menjalankan query UPDATE
cursor.execute(f"UPDATE HEWAN SET jml_sekarang = {jumlah_baru} WHERE id_hewan = {id_hewan}")
conn.commit()

# Menampilkan pesan setelah update berhasil
if cursor.rowcount > 0:
    print(f"Data Hewan dengan ID {id_hewan} berhasil diupdate.")
else:
    print(f"Tidak ada data HEWAN dengan ID {id_hewan}.")
# Menutup koneksi
conn.close()
