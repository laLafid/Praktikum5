import tabel as tb

mahadata = {}
def nilai(str):
    while True:
        try:
            poin = float(input(str))
            if poin < 0 or poin > 100:
                print(f"Nilai harus berkisar dari 0 hingga 100.")
            else:
                return poin
        except ValueError:
            print("Input harus berupa angka!!")       
def nim_adalah(str, harus_ada=False):
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
    tb.tabel(mahadata, title="Data Mahasiswa") 
def tambah():
    NIM = nim_adalah("Masukkan NIM (e.g. 123456789): ")
    mahadata[NIM] = minta(NIM)
    print("Data berhasil ditambahkan.")
def ubah():
    NIM = nim_adalah("Masukkan NIM yang ingin diubah: ", harus_ada=True)
    mahadata[NIM] = minta(NIM)
    print("Data berhasil diubah.")
def hapus():
    NIM = nim_adalah("Masukkan NIM yang ingin dihapus: ", harus_ada=True)
    del mahadata[NIM]
    print("Data berhasil dihapus.")
def cari():
    NIM = nim_adalah("Masukkan NIM yang ingin dicari: ", harus_ada=True)
    tb.tabel({NIM: mahadata[NIM]}, title=f"Data Mahasiswa dengan NIM {NIM}")