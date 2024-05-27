# Inisialisasi data
data_nilai_siswa = []

# Fungsi untuk load data dari file
def load_data():
    try:
        with open('data_siswa.txt', 'r') as file:
            for line in file:
                values = line.strip().split('|')
                if len(values) == 6:
                    nama, nim, umur, kota_asal, alamat, nilai = values
                    nilai = None if nilai == 'None' else int(nilai)
                    data_nilai_siswa.append({
                        'Nama': nama,
                        'NIM': nim,
                        'Umur': umur,
                        'Kota Asal': kota_asal,
                        'Alamat': alamat,
                        'Nilai': nilai
                    })
                else:
                    print(f"Tidak valid: {line.strip()}")
    except FileNotFoundError:
        pass

# Save data ke file
def save_data():
    with open('data_siswa.txt', 'w') as file:
        for siswa in data_nilai_siswa:
            line = f"{siswa['Nama']}|{siswa['NIM']}|{siswa['Umur']}|{siswa['Kota Asal']}|{siswa['Alamat']}|{siswa['Nilai']}\n"
            file.write(line)

# Fungsi untuk melihat data nilai siswa keseluruhan
def view_data():
    if not data_nilai_siswa:
        print("Tidak ada data nilai siswa.")
    else:
        print(f"{'Nama':<20}{'NIM':<10}{'Umur':<5}{'Kota Asal':<15}{'Alamat':<30}{'Nilai':<10}")
        print("="*90)
        for siswa in data_nilai_siswa:
            nilai = siswa['Nilai'] if siswa['Nilai'] is not None else '-'
            print(f"{siswa['Nama']:<20}{siswa['NIM']:<10}{siswa['Umur']:<5}{siswa['Kota Asal']:<15}{siswa['Alamat']:<30}{nilai:<10}")
        print("="*90)

# Fungsi untuk melihat data nilai siswa berdasarkan kota
def filter_by_kota(kota):
    siswa_ditemukan = False
    for siswa in data_nilai_siswa:
        if siswa['Kota Asal'].lower() == kota.lower():
            if not siswa_ditemukan:
                print(f"{'Nama':<20}{'NIM':<10}{'Umur':<5}{'Kota Asal':<15}{'Alamat':<30}{'Nilai':<10}")
                print("="*90)
                siswa_ditemukan = True
            nilai = siswa['Nilai'] if siswa['Nilai'] is not None else '-'
            print(f"{siswa['Nama']:<20}{siswa['NIM']:<10}{siswa['Umur']:<5}{siswa['Kota Asal']:<15}{siswa['Alamat']:<30}{nilai:<10}")
    if not siswa_ditemukan:
        print(f"Tidak ada data siswa dari kota {kota}.")
    else:
        print("="*90)

# Fungsi untuk melihat data nilai siswa berdasarkan nilai
def filter_by_nilai(batas_bawah, batas_atas):
    siswa_ditemukan = False
    for siswa in data_nilai_siswa:
        if siswa['Nilai'] is not None and batas_bawah <= siswa['Nilai'] <= batas_atas:
            if not siswa_ditemukan:
                print(f"{'Nama':<20}{'NIM':<10}{'Umur':<5}{'Kota Asal':<15}{'Alamat':<30}{'Nilai':<10}")
                print("="*90)
                siswa_ditemukan = True
            print(f"{siswa['Nama']:<20}{siswa['NIM']:<10}{siswa['Umur']:<5}{siswa['Kota Asal']:<15}{siswa['Alamat']:<30}{siswa['Nilai']:<10}")
    if not siswa_ditemukan:
        print(f"Tidak ada data siswa dengan nilai di antara {batas_bawah} dan {batas_atas}.")
    else:
        print("="*90)

# Fungsi untuk melihat data siswa yang belum memiliki nilai
def filter_tanpa_nilai():
    siswa_ditemukan = False
    for siswa in data_nilai_siswa:
        if siswa['Nilai'] is None:
            if not siswa_ditemukan:
                print(f"{'Nama':<20}{'NIM':<10}{'Umur':<5}{'Kota Asal':<15}{'Alamat':<30}{'Nilai':<10}")
                print("="*90)
                siswa_ditemukan = True
            print(f"{siswa['Nama']:<20}{siswa['NIM']:<10}{siswa['Umur']:<5}{siswa['Kota Asal']:<15}{siswa['Alamat']:<30}{'-':<10}")
    if not siswa_ditemukan:
        print("Tidak ada siswa yang belum memiliki nilai.")
    else:
        print("="*90)


# Fungsi untuk menambah data nilai siswa
def input_data_siswa(nama, nim, umur, kota_asal, alamat):
    # Periksa apakah NIM sudah ada
    for siswa in data_nilai_siswa:
        if siswa['NIM'] == nim:
            print(f"Data dengan NIM {nim} sudah ada. Tidak dapat menambahkan data baru.")
            return

    # Jika NIM belum ada, tambahkan data baru
    siswa = {
        'Nama': nama,
        'NIM': nim,
        'Umur': umur,
        'Kota Asal': kota_asal,
        'Alamat': alamat,
        'Nilai': None
    }
    data_nilai_siswa.append(siswa)
    save_data()
    print(f"Data untuk {nama} berhasil ditambahkan.")

# Fungsi untuk menambah nilai siswa berdasarkan NIM
def input_nilai(nim, nilai):
    if not (0 <= nilai <= 100):
        print("Nilai harus antara 0 dan 100.")
        return
    for siswa in data_nilai_siswa:
        if siswa['NIM'] == nim:
            siswa['Nilai'] = nilai
            save_data()
            print(f"Nilai untuk NIM {nim} berhasil ditambahkan.")
            return
    print(f"Tidak ada data siswa dengan NIM {nim}.")


# Fungsi untuk menghapus data nilai siswa berdasarkan NIM
def delate_data_siswa(nim):
    global data_nilai_siswa
    siswa_ditemukan = False
    data_nilai_siswa_baru = []
    for siswa in data_nilai_siswa:
        if siswa['NIM'] == nim:
            siswa_ditemukan = True
        else:
            data_nilai_siswa_baru.append(siswa)

    if siswa_ditemukan:
        data_nilai_siswa = data_nilai_siswa_baru
        save_data()
        print(f"Data dengan NIM {nim} berhasil dihapus.")
    else:
        print(f"Tidak ada data siswa dengan NIM {nim}.")

# Fungsi untuk mengubah data nilai siswa berdasarkan NIM
def update_data_siswa(nim, nama=None, umur=None, kota_asal=None, alamat=None):
    for siswa in data_nilai_siswa:
        if siswa['NIM'] == nim:
            if nama:
                siswa['Nama'] = nama
            if umur:
                siswa['Umur'] = umur
            if kota_asal:
                siswa['Kota Asal'] = kota_asal
            if alamat:
                siswa['Alamat'] = alamat
            save_data()
            print(f"Data dengan NIM {nim} berhasil diubah.")
            return
    print(f"Data dengan NIM {nim} tidak ditemukan.")

# Fungsi untuk meminta konfirmasi dari pengguna
def konfirmasi_eksekusi(pesan):
    while True:
        konfirmasi = input(pesan + " (y/n): ").lower()
        if konfirmasi in ['y', 'n']:
            return konfirmasi == 'y'
        else:
            print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")


# Program utama
load_data()
while True:
    print("\nMenu Data Nilai Siswa")
    print("1. Report Data Siswa")
    print("2. Tambah Data Siswa")
    print("3. Input/Update Nilai Siswa")
    print("4. Hapus Data Siswa")
    print("5. Update Data Siswa")
    print("6. Keluar")

    pilihan = input("Pilih menu [1-6]: ")

    if pilihan == '1':
        while True:
            print("\nMenu Report Data Siswa")
            print("1. Full Data Siswa")
            print("2. Data Siswa Berdasarkan Kota")
            print("3. Data Siswa Berdasarkan Nilai")
            print("4. Kembali ke Menu Utama")

            sub_pilihan = input("Pilih menu [1-4]: ")

            if sub_pilihan == '1':
                view_data()
            elif sub_pilihan == '2':
                kota = input("Masukkan nama kota: ")
                filter_by_kota(kota)
            elif sub_pilihan == '3':
                while True:
                    print("\nData Berdasarkan Nilai")
                    print("1. Siswa Lulus (80-100)")
                    print("2. Siswa Remedial (0-79)")
                    print("3. Siswa Tanpa Nilai (-)")
                    print("4. Kembali ke Menu Report Data Siswa")

                    sub_sub_pilihan = input("Pilih menu [1-4]: ")

                    if sub_sub_pilihan == '1':
                        filter_by_nilai(80, 100)
                    elif sub_sub_pilihan == '2':
                        filter_by_nilai(0, 79)
                    elif sub_sub_pilihan == '3':
                        filter_tanpa_nilai()
                    elif sub_sub_pilihan == '4':
                        break
                    else:
                        print("Pilihan menu hanya 1-4.")
            elif sub_pilihan == '4':
                break
            else:
                print("Pilihan tidak valid.")
    elif pilihan == '2':
        nama = input("Nama: ")
        nim = input("NIM: ")
        umur = input("Umur: ")
        kota_asal = input("Kota Asal: ")
        alamat = input("Alamat: ")
        if konfirmasi_eksekusi("Apakah Anda yakin ingin menambahkan data ini?"):
            input_data_siswa(nama, nim, umur, kota_asal, alamat)
    elif pilihan == '3':
        nim = input("Masukkan NIM: ")
        try:
            nilai = int(input("Masukkan Nilai (0-100): "))
            if 0 <= nilai <= 100:
                if konfirmasi_eksekusi("Apakah Anda yakin ingin memasukkan nilai ini?"):
                    input_nilai(nim, nilai)
            else:
                print("Nilai harus antara 0 dan 100.")
        except ValueError:
            print("Nilai harus berupa angka antara 0 dan 100.")
    elif pilihan == '4':
        nim = input("Masukkan NIM siswa yang ingin dihapus: ")
        if konfirmasi_eksekusi("Apakah Anda yakin ingin menghapus data ini?"):
            delate_data_siswa(nim)
    elif pilihan == '5':
        nim = input("Masukkan NIM siswa yang ingin diubah: ")
        nama = input("Nama Baru (biarkan kosong jika tidak diubah): ") or None
        umur = input("Umur Baru (biarkan kosong jika tidak diubah): ") or None
        kota_asal = input("Kota Asal Baru (biarkan kosong jika tidak diubah): ") or None
        alamat = input("Alamat Baru (biarkan kosong jika tidak diubah): ") or None
        if konfirmasi_eksekusi("Apakah Anda yakin ingin mengubah data ini?"):
            update_data_siswa(nim, nama, umur, kota_asal, alamat)
    elif pilihan == '6':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
