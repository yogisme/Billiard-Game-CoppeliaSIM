# Billiard-Game-CoppeliaSIM
Interactive billiard game simulation using Python &amp; CoppeliaSim with ZMQ API

1. PENDAHULUAN 
Proyek ini adalah simulasi permainan biliar sederhana menggunakan CoppeliaSim. 
Pengguna dapat mengontrol bola putih dengan memberikan gaya (force) atau torsi (torque) 
agar dapat memukul bola lain menuju lubang. Proyek ini dirancang untuk tujuan edukasi dalam 
memahami konsep fisika (dinamika benda kaku), kontrol input, serta interaksi antar objek di 
lingkungan simulasi.

3. PERSIAPAN SOFTWARE 
1) Instalasi Python & Library 
a. Pastikan Python 3.10+ sudah terpasang. 
b. Instal library untuk komunikasi dengan CoppeliaSim: 
pip install coppeliasim-zmqremoteapi-client 
2) Persiapan CoppeliaSim 
a. Buka aplikasi CoppeliaSim. 
b. Siapkan scene dengan bola-bola missal billiard_game.ttt di folder proyek 
• Sphere[6] = bola putih (cue ball). 
• Sphere[0] hingga Sphere[5] = bola berwarna. 
c. Pastikan semua bola punya dynamic properties diaktifkan (Rigid Body). 
                                                                                                                                       
3. MENYALIN PROGRAM 
Buat file Python, misalnya dengan nama billiard_multiplayer.py, lalu salin kode yang terlampir.

4. MENJALANKAN PERMAINAN 
1) Jalankan CoppeliaSim, load scene dengan bola-bola atau dapat mengakses link 
berikut untuk sce billiard https://zeentust.notion.site/sro-fall-2025. 
2) Jangan klik Start di CoppeliaSim, biarkan Python yang memulainya. 
3) Buka terminal di VS Code atau Command Prompt, lalu jalankan: 
python billiard_multiplayer.py 
4) Jika koneksi berhasil, akan muncul: 
5. ATURAN MAIN 
1) Saat program bertanya: 
Masukkan jumlah pemain, misalnya 2 untuk dua orang. 
2) Giliran akan dimulai dari Player 1, lalu bergantian sesuai jumlah pemain. 
3) Tiap pemain harus memasukkan nilai Force (Fx, Fy, Fz) dan Torque (Tx, Ty, Tz). 
Kalau ingin mendorong bola lurus ke arah sumbu X positif: 
• Fx = 10 
• Fy = 0 
• Fz = 0 
• Tx = 0 
• Ty = 0 
• Tz = 0 
Kalau ingin ke arah Y: 
• Fx = 0 
• Fy = 10 
• Fz = 0 
• Tx = 0 
• Ty = 0 
• Tz = 0 
4) Setelah input, bola putih akan bergerak selama 5 detik dan posisi terbaru semua bola 
akan ditampilkan di terminal. 
5) Program akan bertanya: 
• Masukkan y → lanjut ke pemain berikutnya. 
• Masukkan n → permainan selesai.

6. Menyelesaikan Permainan 
Setelah salah satu pemain mengetik n, program otomatis menghentikan simulasi: 
Bola kembali diam di posisi terakhir. CoppeliaSim siap digunakan lagi (bisa reset scene atau 
main ulang).

8. TIPS BERMAIN 
• Gunakan Fx, Fy untuk arah horizontal meja. 
• Gunakan Fz untuk memberi efek angkat bola (jarang dipakai di biliar normal). 
• Gunakan Torque (Tx, Ty, Tz) untuk memberi efek putaran (spin). 
• Semakin besar nilai gaya, semakin jauh bola akan bergerak.
