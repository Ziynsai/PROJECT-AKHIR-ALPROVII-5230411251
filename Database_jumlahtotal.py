import sqlite3
koneksi = sqlite3.connect('Database_hewan_final.db')
kursor = koneksi.cursor()

kursor.execute("select SUM(JML_SEKARANG) FROM HEWAN")
total_hewan_langka = kursor.fetchone()[0]

print(f"Jumlah total populasi hewan saat ini ada : {total_hewan_langka}")
kursor.close()