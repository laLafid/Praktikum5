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
    
def tambah():
    NIM = int(input("Masukkan NIM (e.g. 123456789): "))
    if NIM in mahadata:
        print("NIM sudah ada di database. Silakan masukkan NIM lain.")
        return
    data = minta(NIM)
    mahadata[NIM] = data
    print("Data berhasil ditambahkan.")
    
def hapus():
    NIM = int(input("Masukkan NIM yang ingin dihapus: "))
    if NIM in mahadata:
        del mahadata[NIM]
        print("Data berhasil dihapus.")
    else:
        print("NIM tidak ditemukan.")
        
def ubah():
    NIM = int(input("Masukkan NIM yang ingin diubah: "))
    if NIM in mahadata:
        data = minta(NIM)
        mahadata[NIM] = data
        print("Data berhasil diubah.")
    else:
        print("NIM tidak ditemukan.")
        
def cari():
    NIM = int(input("Masukkan NIM yang ingin dicari: "))
    if NIM in mahadata:
        data = {NIM: mahadata[NIM]}
        tb.tabel(data, title=f"Data Mahasiswa dengan NIM {NIM}")
    else:
        print("NIM tidak ditemukan.")
        
def lihat():
    tb.tabel(mahadata, title="Data Mahasiswa")