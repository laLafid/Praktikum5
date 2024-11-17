import tabulate
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
def tabel(data, headers=None, title=""):
    # fungsi tabel mencetak table data
    if not data: 
        table = [["Tidak ada data"]]
        print(tabulate.tabulate(
            table, 
            headers=["Tidak ada data"], 
            tablefmt="fancy_grid", 
            colalign=("center",)
            ))
        return
    if headers is None:
        headers = ["No", "Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"]
    table = []
    for i, NIM in enumerate(data, start=1):
        row = [
            i, 
            data[NIM]["Nama"], 
            NIM, 
            data[NIM]["Nilai Tugas"], 
            data[NIM]["Nilai UTS"], 
            data[NIM]["Nilai UAS"], 
            data[NIM]["Nilai Akhir"]
            ]
        table.append(row)
    print(f"{title}")
    print(tabulate.tabulate(table, headers, tablefmt="fancy_grid", colalign=("center",)*7))
def minta(NIM):
    # fungsi minta input + nambahin ke dictionary
    Nama = input("Masukkan Nama: ")
    Tugas, UTS, UAS = map(nilai, 
    ["Masukkan Nilai Tugas: ", "Masukkan Nilai UTS: ", "Masukkan Nilai UAS: "])
    Akhir = (Tugas*0.3) + (UTS*0.35) + (UAS*0.35)
    return {
        "Nama": Nama,
        "NIM": NIM,
        "Nilai Tugas": Tugas,
        "Nilai UTS": UTS,
        "Nilai UAS": UAS,
        "Nilai Akhir": Akhir
    }
def tambah():
    # fungsi tambahkan data ke dictionary
    NIM = int(input("Masukkan NIM (e.g. 123456789): "))
    if NIM in r:
        print("NIM sudah ada di database. Silakan masukkan NIM lain.")
        return
    data = minta(NIM)
    r[NIM] = data
    print("Data berhasil ditambahkan.")
def hapus():
    # fungsi hapus data dari dictionary
    NIM = int(input("Masukkan NIM yang ingin dihapus: "))
    if NIM in r:
        del r[NIM]
        print("Data berhasil dihapus.")
    else:
        print("NIM tidak ditemukan.")
def ubah():
    # fungsi ubah data yang ada di dictionary
    NIM = int(input("Masukkan NIM yang ingin diubah: "))
    if NIM in r:
        data = minta(NIM)
        r[NIM] = data
        print("Data berhasil diubah.")
    else:
        print("NIM tidak ditemukan.")
def cari():
    # fungsi cari data dalam dictionary
    NIM = int(input("Masukkan NIM yang ingin dicari: "))
    if NIM in r:
        data = {NIM: r[NIM]}
        tabel(data, title=f"Data Mahasiswa dengan NIM {NIM}")
    else:
        print("NIM tidak ditemukan.")
def lihat():
    # fungsi ini sebenernya ga perlu
    # tapi karna pake dictionary menu isiannya langsung di cetak 
    # jadi pake ginian 
    tabel(r, title="Data Mahasiswa") # r, title= itu harus ada ya
r = {
    # Dictionary kosong 
    # nanti di isi dengan data dari user
}
menu = {
    # isinya menu yang bisa dipilih
    "1": lihat,"l" : lihat,
    "2": tambah,"t" : tambah,
    "3": ubah,"u" : ubah,
    "4": hapus,"h" : hapus,
    "5": cari,"c" : cari,
    "6": exit,"k" : exit
}
while True:
    # Menampilkan Menu 
    # Warnanya pake ANSI escape color code 
    print(
        "\033[1m L\033[0mihat", 
        "\033[1;32m T\033[0mambah", 
        "\033[1;34m U\033[0mbah", 
        "\033[1;31m H\033[0mapus", 
        "\033[1;33m C\033[0mari", 
        "\033[1;35m K\033[0meluar"
        )
    pilihan = input("Masukkan pilihan: ").lower()
    if pilihan in menu:
        menu[pilihan]()
    else:
        print("Pilihan tidak ada.")