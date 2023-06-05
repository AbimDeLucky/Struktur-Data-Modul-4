import sys


class DataMahasiswa:

    def __init__(self):
        self.data_tabel = {}
        self.tabel_sesi_login = {}

    def tambah_data(self, nim_praktikan, nama_asisten):
        if nim_praktikan not in self.data_tabel:
            if "IF" in nim_praktikan:
                self.data_tabel[nim_praktikan] = nama_asisten
            else:
                print("Format NIM salah!")
        else:
            print("Data Sudah diinputkan!")
        return nim_praktikan not in self.data_tabel

    def tampil(self):
        print("Total data tersimpan :", len(self.data_tabel))
        for nim, asisten in self.data_tabel.items():
            print(f"NIM : {nim}\t\tNama Asisten : {asisten}")

    def list_nim_praktikan(self):
        print(list(self.data_tabel.keys()))

    def list_nama_asisten(self):
        print(list(self.data_tabel.values()))

    def total_email(self):
        return len(self.data_tabel)

    def hapus_data(self, nim_praktikan, nama_asisten):
        if nim_praktikan in self.data_tabel:
            del self.data_tabel[nim_praktikan]
        else:
            print("Data tidak ditemukan!")
        return True

    def edit_data(self, nim_praktikan, nama_asisten):
        if nim_praktikan in self.data_tabel:
            print(
                f"Data lama yang akan diedit nim : {nim_praktikan}\tnama asisten : {nama_asisten}")
            nama_baru = input("Silahkan Masukkan nama asisten yang update : ")
            self.data_tabel[nim_praktikan] = nama_baru
        else:
            print("data tidak ditemukan!")

    def search(self, nama_asisten):
        print(f"List NIM Dengan Asisten {nama_asisten} : ")
        for i, (key, value) in enumerate(self.data_tabel.items(), start=1):
            if value == nama_asisten:
                print(f"{i}. {key}")
        print()

    def login(self):
        self.tabel_sesi_login["admin@umm.ac.id"] = "admin"

    print("==LOGIN==")
    email = input("Silahkan Masukkan Email : ")
    if email in self.tabel_sesi_login:
        if "@umm.ac.id" in email:
            password = input("Masukkan Password : ")
            if password == self.tabel_sesi_login[email]:
                print("===Login Sukses===")
                while True:
                    pilihan = int(input("...Menu...\n1. Tambah Data\n2. Tampilkan Data\n3. Tampilkan list nim praktikan\n4. Tampilkan list nama asisten\n5. Total jumlah data\n6. Hapus data\n7. Edit data\n8. Cari data\n9. Logout\nSilahkan masukkan pilihan : "))
                    if pilihan == 1:
                        print("---Tambah Data Baru---")
                        nim = input("Masukkan NIM : ")
                        nama_a = input("Masukkan nama asisten : ")
                        self.tambah_data(nim, nama_a)
                    elif pilihan == 2:
                        self.tampil()
                    elif pilihan == 3:
                        self.list_nim_praktikan()
                    elif pilihan == 4:
                        self.list_nama_asisten()
                    elif pilihan == 5:
                        print(self.total_email())
                    elif pilihan == 6:
                        print("---Hapus Data---")
                        nim_hapus = input("Masukkan NIM : ")
                        nama_hapus = input("Masukkan nama asisten : ")
                        self.hapus_data(nim_hapus, nama_hapus)
                    elif pilihan == 7:
                        print("---Edit Data---")
                        nim_edit = input("Masukkan NIM : ")
                        nama_edit = input("Masukkan nama asisten lama : ")
                        self.edit_data(nim_edit, nama_edit)
                    elif pilihan == 8:
                        print("---Search data Asisten---")
                        nama_asisten = input("Masukkan nama asisten : ")
                        self.search(nama_asisten)
                    elif pilihan == 9:
                        self.logout()
            else:
                print("Gagal Login")
                self.login()
        else:
            print("Gagal Login, Email salah!")
            self.login()
    else:
        print("Gagal Login, Email salah!")
        self.login()


def logout(self):
    print("---LOGOUT---")
    sys.exit(0)


@staticmethod
def main():
    dm = DataMahasiswa()
    dm.login()


if __name__ == "__main__":
    DataMahasiswa.main(sys.argv)
