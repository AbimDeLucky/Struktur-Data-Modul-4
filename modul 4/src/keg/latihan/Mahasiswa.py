mhs = {
    "1": {
        "nama": "Putri",
        "kelas": "3H",
        "matkul_praktikum": "Struktur Data",
        "nim": 2020000
    },
    "2": {
        "nama": "Agus",
        "kelas": "3A",
        "matkul_praktikum": "Matematika",
        "nim": 2020012
    },
    "3": {
        "nama": "Arro",
        "kelas": "3D",
        "matkul_praktikum": "Pemrograman",
        "nim": 2020017
    }
}

input_id = input("Masukan ID : ")
data = mhs.get(input_id)
if data:
    print("Data Mahasiswa : ")
    print("Nama : ", data["nama"])
    print("Kelas : ", data["kelas"])
    print("Mata Kuliah Praktikum : ", data["matkul_praktikum"])
    print("NIM : ", data["nim"])
else:
    print("ID tidak ditemukan")
