package keg.modul4;

import java.util.HashMap;
import java.util.Scanner;

public class DataPraktikan {

    HashMap<String, String> dataTabel = new HashMap<>();
    HashMap<String, String> tabelSesiLogin = new HashMap<>();
    Scanner input = new Scanner(System.in);

    public boolean tambahData(String nimPraktikan, String namaAsisten) {

        if (!dataTabel.containsKey(nimPraktikan)) {
            if (nimPraktikan.contains("IF")) {
                dataTabel.put(nimPraktikan, namaAsisten);
            } else {
                System.out.println("Format NIM salah!");
            }
        } else {
            System.out.println("Data Sudah diinputkan!");
        }
        return !dataTabel.containsKey(nimPraktikan);
    }

    public void tampil() {
        System.out.println("Total data tersimpan : " + dataTabel.size());
        String[] nim = dataTabel.keySet().toArray(new String[0]);
        String[] asisten = dataTabel.values().toArray(new String[0]);

        for (int i = 0; i < dataTabel.size(); i++) {
            System.out.println("NIM : " + nim[i] + "\t\t" + "Nama Asisten : " + asisten[i]);
        }
    }

    public void listNimPraktikan() {
        System.out.println(dataTabel.keySet());
    }

    public void listNamaAsisten() {
        System.out.println(dataTabel.values());
    }

    public int totalEmail() {
        return dataTabel.size();
    }

    public boolean hapusData(String nimPraktikan, String namaAsisten) {
        if (dataTabel.containsKey(nimPraktikan)) {
            dataTabel.remove(nimPraktikan, namaAsisten);
        } else {
            System.out.println("Data tidak ditemukan!");
        }
        return true;
    }

    public void editData(String nimPraktikan, String namaAsisten) {
        for (String nim : dataTabel.keySet()) {
            if (nim.equals(nimPraktikan)) {
                System.out.println(
                        "Data lama yang akan diedit nim : " + nimPraktikan + "\tnama asisten : " + namaAsisten);
                System.out.print("Silahkan Masukkan nama asisten yang update : ");
                String namaBaru = input.next();
                dataTabel.replace(nimPraktikan, namaBaru);
            } else {
                System.out.println("data tidak ditemukan!");
            }
        }
    }

    public void search(String namaAsisten) {
        int i = 1;
        System.out.println("List NIM Dengan Asisten " + namaAsisten + " : ");
        for (String key : dataTabel.keySet()) {
            if (dataTabel.get(key).equals(namaAsisten)) {
                System.out.println(i + ". " + key);
                i++;
            }
        }
        System.out.println();
    }

    public void login() {

        tabelSesiLogin.put("admin@umm.ac.id", "admin");

        System.out.println("==LOGIN==");
        System.out.print("Silahkan Masukkan Email : ");
        String email = input.next();
        if (tabelSesiLogin.containsKey(email)) {
            if (email.contains("@umm.ac.id")) {
                System.out.print("Masukkan Password : ");
                String password = input.next();
                if (tabelSesiLogin.containsValue(password)) {
                    System.out.println("===Login Sukses===");
                    while (true) {
                        System.out.println(
                                "...Menu...\n1. Tambah Data\n2. Tampilkan Data\n3. Tampilkan list nim praktikan\n4. Tampilkan list nama asisten\n5. Total jumlah data\n6. Hapus data\n7. Edit data\n8. Cari data\n9. Logout\nSilahkan masukkan pilihan : ");
                        int pilih = input.nextInt();
                        switch (pilih) {
                            case 1:
                                System.out.println("===Tambah Data Baru===");
                                System.out.print("Masukkan NIM : ");
                                String nim = input.next();
                                System.out.print("Masukkan nama asisten : ");
                                String namaA = input.next();
                                tambahData(nim, namaA);
                                break;
                            case 2:
                                tampil();
                            case 3:
                                listNimPraktikan();
                            case 4:
                                listNamaAsisten();
                            case 5:
                                System.out.println(totalEmail());
                                break;
                            case 6:
                                System.out.println("===Hapus Data===");
                                System.out.print("Masukkan NIM : ");
                                String nimHapus = input.next();
                                System.out.print("Masukkan nama asisten : ");
                                String namaHapus = input.next();
                                hapusData(nimHapus, namaHapus);
                                break;
                            case 7:
                                System.out.println("===Edit Data===");
                                System.out.print("Masukkan NIM : ");
                                String nimEdit = input.next();
                                System.out.print("Masukkan nama asisten lama : ");
                                String namaEdit = input.next();
                                editData(nimEdit, namaEdit);
                                break;
                            case 8:
                                System.out.println("===Search data Asisten===");
                                System.out.print("Masukkan nama asisten : ");
                                String namaAsisten = input.next();
                                search(namaAsisten);
                                break;
                            case 9:
                                logout();
                        }

                    }

                } else {
                    System.out.println("Gagal Login");
                    login();
                }
            }
        } else {
            System.out.println("Gagal Login, Email salah!");
            login();
        }
    }

    public void logout() {
        System.out.println("=== LOGOUT ===");
        System.exit(0);
    }

    public static void main(String[] args) {

        DataPraktikan dm = new DataPraktikan();

        dm.login();

    }
}
