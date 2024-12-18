import tabel as tb # pangil fungsi dari file tabel

mahadata = {} # Dictionary kosong
# nantinya akan di isi dengan data dari user

def nilai(str):
# fungsi untuk memastikan input adalah angka
# dan mengulangi permintaan jika input bukan angka
# juga membatasi nilai input yang diinputkan.
    while True:
        try:
            poin = float(input(str))
            if poin < 0 or poin > 100:
                print(f"Nilai harus berkisar dari 0 hingga 100.")
            else:
                return poin
        except ValueError:
            print("Input harus berupa angka!!")    
               
def nim_adalah(str, harus_ada=True):
# fungsi ini akan meminta input NIM dari user
# melihat apakah NIM tersebut ada di database atau tidak
# dan mengulangi permintaan jika input bukanlah angka
# karna NIM adalah Nomor Induk Mahasiswa
    while True:
        try:
            NIM = int(input(str))
            if harus_ada and NIM not in mahadata:
                print("NIM tidak ditemukan!")
            elif not harus_ada and NIM in mahadata:
                print("NIM sudah ada di database. Masukkan NIM lain!")
            else:
                return NIM
        except ValueError:
            print("Input harus berupa angka!!")    
            
def minta(NIM):
# fungsi minta input
    nama = input("Masukkan Nama: ")
    tugas, uts, uas = map(nilai, [
        "Masukkan Nilai Tugas: ", 
        "Masukkan Nilai UTS: ", 
        "Masukkan Nilai UAS: "
        ])
    akhir = (tugas*0.3) + (uts*0.35) + (uas*0.35)
    return {
        "Nama": nama,
        "NIM": NIM,
        "Nilai Tugas": tugas,
        "Nilai UTS": uts,
        "Nilai UAS": uas,
        "Nilai Akhir": akhir
    }
    
def lihat():
# fungsi untuk menampilkan data yang ada di dictionary
    tb.tabel(mahadata, title="Data Mahasiswa") 
    
def tambah():
# fungsi yang akan menambahkan data yang sudah diterima fungsi minta
# ke dalam dictionary
    NIM = nim_adalah("Masukkan NIM (e.g. 123456789): ", harus_ada=False)
    mahadata[NIM] = minta(NIM)
    print("Data berhasil ditambahkan.")
    
def ubah():
# fungsi akan mencari data dengan NIM yang sesuai
# kemudian meminta input data baru
# input tersebut akan menggantikan data yang sudah ada
    NIM = nim_adalah("Masukkan NIM yang ingin diubah: ")
    mahadata[NIM] = minta(NIM)
    print("Data berhasil diubah.")
    
def hapus():
# fungsi ini gunanya untuk hapus data dari dictionary
    NIM = nim_adalah("Masukkan NIM yang ingin dihapus: ")
    del mahadata[NIM]
    print("Data berhasil dihapus.")
    
def cari():
# akan mencari dengan NIM
# data dengan NIM tersebut akan ditamplikan kepada user
    NIM = nim_adalah("Masukkan NIM yang ingin dicari: ")
    tb.tabel({NIM: mahadata[NIM]}, title=f"Data Mahasiswa dengan NIM {NIM}")