


class harga_mobil:

    list_harga_mobil = {"avanza":[200_000_000,"toyota","minibus"],"innova":[250_000_000,"toyota","minibus"],
                        "veloz":[225_000_000,"toyota","minibus"],"agya":[180_000_000,"toyota","mini cooper"]}

    def __init__(self,nama):
        self.nama = nama
        
    def cek(self):
        print(f"\n{self.nama}\n")

    def harga(self):
        if self.nama in self.list_harga_mobil:
            print(f"Harga mobil {self.nama} adalah = ", self.list_harga_mobil[self.nama][0])
            print("merek mobil = ", self.list_harga_mobil[self.nama][1])
            print(f"type dari mobil {self.nama } adalah = ", self.list_harga_mobil[self.nama][2])
            
class checkout(harga_mobil):

    def __init__(self, nama):
        super().__init__(nama)

    def print_kwintasi(self):
        print("="*25,"JAYA MOTOR ABADI","="*25)
        nama = input("Nama Pembeli       = ")
        alamat = input("Alamat Pembeli     = ")
        jumlah = input("Jumlah Unit Dibeli = ")
        print("pajak kendaraan    = 10%")
        pajak = self.list_harga_mobil[self.nama][0] / 10
        print("="*30)
        print(f"Pembelian mobil {self.nama}")
        print(f"Atas Nama = {nama}")
        print(f"Alamat    = {alamat}")
        print(f"Dengan total harga beserta pajak 10% = {self.list_harga_mobil[self.nama][0] + pajak}")

for key in harga_mobil.list_harga_mobil:
    print(f"{key}  = {harga_mobil.list_harga_mobil[key]}")

mobil = input("masukkan nama mobil yang anda inginkan = ")
mobil1 = harga_mobil(mobil)
mobil1.cek()
mobil1.harga()
check1 = str(input("Apakah anda berminat untuk membeli (y/n) ? "))
if check1 == 'y':
    check2 = checkout(mobil)
    check2.print_kwintasi()
elif check1 == 'n':
    print("Apa anda masih bingung dengan jenis mobil apa yang cocok dengan anda?")
    print("jika iya, silahkan hubungi call center kami di 2000100")