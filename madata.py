import fungsi as f

menu = {
    "1": f.lihat,   "l" : f.lihat,
    "2": f.tambah,  "t" : f.tambah,
    "3": f.ubah,    "u" : f.ubah,
    "4": f.hapus,   "h" : f.hapus,
    "5": f.cari,    "c" : f.cari,
    "6": exit,      "k" : exit
}

reset = "\033[0m"
hijau = "\033[1;32m"
biru = "\033[1;34m"
merah = "\033[1;31m"
kuning = "\033[1;33m"
ungu = "\033[1;35m"
putih = "\033[1;37m"

while True:
    print(
        f"{putih}L{reset}ihat |", 
        f"{hijau}T{reset}ambah |", 
        f"{biru}U{reset}bah |", 
        f"{merah}H{reset}apus |", 
        f"{kuning}C{reset}ari |", 
        f"{ungu}K{reset}eluar"
    )
    pilihan = input("Masukkan pilihan: ").lower()
    if pilihan in menu:
        menu[pilihan]()
    else:
        print("Pilihan tidak ada.")