from tabulate import tabulate

def tabel(data, headers=None, title=""):
    if not data: 
        table = [["Tidak ada data"]]
        print(tabulate(
            table, 
            headers =["Tidak ada data"], 
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
    print(tabulate(
        table, 
        headers, 
        tablefmt="fancy_grid", 
        colalign=("center",)*7
        ))