print(f"{'='*25} PROGRAM HITUNG GAJI KARYAWAN {'='*25}")

gaji = 300_000 # GAJI POKOK 
nama = input("Masukkan nama anda : ")
golongan = int(input("    Golongan Jabatan  : "))
pendidikan = input("    Pendidikan        : ")
jam = int(input("    Jumlah jam kerja  : "))

#TUNJGANAN JABATAN
if golongan == 1: # TERDAPAT 3 GOLONGAN JABATAN DENGAN BESARAN TUNJANGAN YANG BERBEDA
    TunjanganJabatan = (gaji*5)/100
elif golongan == 2:
    TunjanganJabatan = (gaji*10)/100
elif golongan == 3:
    TunjanganJabatan = (gaji*15)/100

#TUNJAGAN PENDIDIKAN 
# ADA SMA,D1,D3,DAN S1. SETIAP TINGKATAN MEMILIKI BESARAN YANG BERBEDA
if pendidikan.upper() == "SMA": # TERDAPAT 4 TINGKATANN TUNJAGANA PENDIDIKAN
    TunjangaPendidikan = (gaji*2,5)/100
elif pendidikan.upper() == "D1":
    TunjanganJabatan = (gaji*5)/100
elif pendidikan.upper() == "D3":
    TunjanganJabatan = (gaji*20)/100
else:
    TunjanganPendidikan = (gaji*30)/100

b = 8*22
#jam_lembur = jam - b 
# hari kerja dalam sebulan sekitar 22-23 bahkan bisa kurang
# sehingga kita hitung saja 22

if jam > b:
    jam_lembur = jam - b # jika total dari jam lebih besar dari b akan dilakukan perhitungan
else :
    jam_lembur = 0 # jika jam kerja sama dengan b atau kurang maka tidak ada uang tambahan

HonorLembur = jam_lembur * 3500
TotalGaji = gaji + TunjanganJabatan + TunjanganPendidikan + HonorLembur

print(f'\nkaryawan yang bernama = {nama}')
print("Honor yang diterima")
print(f"{' '*4}Tunjangan Jabatan{' '*2}   Rp  {TunjanganJabatan}")
print(f"{' '*4}Tunjangan Pendidikan{' '*2}Rp  {TunjanganPendidikan}")
print(f"{' '*4}Honor Lembur{' '*2}        Rp  {HonorLembur}")
print(f"{' '*4}Total Gaji{' '*2}               Rp  {TotalGaji}")
print("(Gaji pokok + tunjangan +lembur)")

