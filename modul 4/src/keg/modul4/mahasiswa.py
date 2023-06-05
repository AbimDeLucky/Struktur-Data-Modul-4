import getpass
import sys


class DataMahasiswa:
    def __init__(self):
        self.tabelData = {}
        self.tabelLogin = {}

    def tambah_data(self, nim_praktikan, nama_asisten):
        if nim_praktikan not in self.tabelData:
            if "IF" in nim_praktikan:
                self.tabelData[nim_praktikan] = nama_asisten
            else:
                print("Format NIM salah!")
        else:
            print("Data sudah diinputkan!")
        return nim_praktikan not in self.tabelData

    def tampil(self):
        print("Total data tersimpan :", len(self.tabelData))
        for nim, asisten in self.tabelData.items():
            print("NIM :", nim, "\t\t", "Nama Asisten :", asisten)

    def list_nim_praktikan(self):
        print(set(self.tabelData.keys()))

    def list_nama_asisten(self):
        print(set(self.tabelData.values()))

    def total_email(self):
        return len(self.tabelData)

    def hapus_data(self, nim_praktikan, nama_asisten):
        if nim_praktikan in self.tabelData:
            del self.tabelData[nim_praktikan]
        else:
            print("Data tidak ditemukan!")
        return True

    def edit_data(self, nim_praktikan, nama_asisten):
        if nim_praktikan in self.tabelData:
            print("Data lama yang akan diedit nim :",
                  nim_praktikan, "\tnama asisten :", nama_asisten)
            nama_baru = input("Silahkan masukkan nama asisten yang update : ")
            self.tabelData[nim_praktikan] = nama_baru
        else:
            print("Data tidak ditemukan!")

    def search(self, nama_asisten):
        print("List NIM dengan Asisten", nama_asisten, ":")
        for nim, asisten in self.tabelData.items():
            if asisten == nama_asisten:
                print(nim)
        print()

    def login(self):
        self.tabelLogin["admin@umm.ac.id"] = "admin"
        print("==LOGIN==")
        email = input("Silahkan masukkan email : ")
        if email in self.tabelLogin:
            if "@umm.ac.id" in email:
                password = getpass.getpass("Masukkan password : ")
                if password == self.tabelLogin[email]:
                    print("=== Login Sukses ===")
                    self.menu()
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
        print("=== LOGOUT ===")
        exit()

    def menu(self):
        while True:
            pilihan = int(input("\n:::..    MENU    ..:::\n1. Tambah Data\n2. Tampilkan Data\n3. Tampilkan list nim praktikan\n4. Tampilkan list nama asisten\n5. Total jumlah data\n6. Hapus data\n7. Edit data\n8. Cari data\n9. Logout\nSilahkan masukkan pilihan : "))
            if pilihan == 1:
                print("=== Tambah Data Baru ===")
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
                print("=== Hapus Data ===")
                nim_hapus = input("Masukkan NIM : ")
                nama_hapus = input("Masukkan nama asisten : ")
                self.hapus_data(nim_hapus, nama_hapus)
            elif pilihan == 7:
                print("=== Edit Data ===")
                nim_edit = input("Masukkan NIM : ")
                nama_edit = input("Masukkan nama asisten lama : ")
                self.edit_data(nim_edit, nama_edit)
            elif pilihan == 8:
                print("=== Search data Asisten ===")
                nama_asisten = input("Masukkan nama asisten : ")
                self.search(nama_asisten)
            elif pilihan == 9:
                self.logout()
            else:
                print("Pilihan tidak valid. Silahkan coba lagi.")

    @staticmethod
    def main(args):
        dm = DataMahasiswa()
        dm.login()


if __name__ == "__main__":
    DataMahasiswa.main(sys.argv)
