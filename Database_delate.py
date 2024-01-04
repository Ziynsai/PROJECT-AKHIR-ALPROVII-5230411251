import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('Database_hewan_final.db')
cursor = conn.cursor()

# Menjalankan query DELETE
jenis = Mamalia  # ID pegawai yang akan dihapus
cursor.execute(f"DELETE FROM HEWAN WHERE jenis = ?", (jenis,))
conn.commit()

# Menampilkan pesan setelah penghapusan berhasil
if cursor.rowcount > 0:
    print(f"Data Hewan dengan ID {jenis} berhasil dihapus.")
else:
    print(f"Tidak ada data HEWAN dengan ID {jenis}.")

# Menutup koneksi
conn.close()
