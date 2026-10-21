"""
Program: Normalisasi Data Mahasiswa (tugas/normalisasi_data_mahasiswa.py)
Mata Kuliah: Algoritma dan Pemrograman - S1 Pendidikan Matematika Untirta
"""

def normalisasi_nama(nama):
    return " ".join(nama.strip().split()).title()

def buat_inisial(nama):
    nama_bersih = normalisasi_nama(nama)
    kata = nama_bersih.split()
    return "".join(k[0] for k in kata)

def normalisasi_kode(kode):
    kata = kode.strip().upper().split()
    return "-".join(kata)

def main():
    print("=" * 50)
    print("      TUGAS 10: NORMALISASI DATA MAHASISWA")
    print("=" * 50)
    
    nama_input = input("Masukkan Nama Lengkap : ")
    kode_input = input("Masukkan Kode Kelas   : ")
    
    nama_bersih = normalisasi_nama(nama_input)
    kode_bersih = normalisasi_kode(kode_input)
    inisial = buat_inisial(nama_input)
    jumlah_kata = len(nama_bersih.split())
    
    print("\n" + "=" * 50)
    print("                 HASIL NORMALISASI")
    print("=" * 50)
    print(f"Nama Bersih  : {nama_bersih}")
    print(f"Kode Kelas   : {kode_bersih}")
    print(f"Jumlah Kata  : {jumlah_kata}")
    print(f"Inisial      : {inisial}")
    print("=" * 50)

if __name__ == "__main__":
    main()