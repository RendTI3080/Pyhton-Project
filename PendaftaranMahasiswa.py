print("\nSilahkan pilih prodi yang sesuai dengan minat anda : ")
jurusan = {"Sistem Informasi":[2_400_000,"SI"],"Sistem Informasi Akuntasi":[2_000_000,"SIA"]}

a = 1
for i in jurusan: # perulangan untuk menampilkan jurusan yang ada
    print(f"\nJurusan ke -{a}")
    print(f"Kode jurusan = {jurusan[i][1]}")
    print(f"Nama prodi   = {i}")
    print(f"Harga        = {jurusan[i][1]}")
    a += 1

nis = input("\nMasukkan NIS anda = ")
nama = input("Masukkan nama lengkap anda = ")
prodi = input("Masukkan prodi pilihan anda = ")

if prodi.title() in jurusan: # merupakan keluaran dari proses pendafataran
    print(f"\n{'='*25} KARTU PENDAFTARAN {'='*25}")
    print(f"Nomor NIS anda    = {nis}")
    print(f"Nama anda         = {nama}")  
    print(f"prodi anda        = {prodi.title()}")
    print(f"Total biaya pendidikan anda adalah = {jurusan[prodi.title()][0]}")
else:
    print("maaf prodi yang anda pilih tidak ada") # jika jurusan yang dipilih tidak ada maka sistem 
                                                  # akan mengeluarkan perintah ini