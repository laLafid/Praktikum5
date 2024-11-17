import fungsi as f
menu = {
    "1": f.lihat,"l" : f.lihat,
    "2": f.tambah,"t" : f.tambah,
    "3": f.ubah,"u" : f.ubah,
    "4": f.hapus,"h" : f.hapus,
    "5": f.cari,"c" : f.cari,
    "6": exit,"k" : exit
}
while True:
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