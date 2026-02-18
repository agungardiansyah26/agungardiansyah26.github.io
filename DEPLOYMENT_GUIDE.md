# Panduan Upload Portofolio ke GitHub Pages

Panduan ini akan membantu Anda mengupload website portofolio yang sudah jadi ke **GitHub Pages** agar bisa diakses online oleh siapa saja.

## Langkah 1: Buat Repository di GitHub

1.  Buka browser dan login ke **[GitHub.com](https://github.com)**.
2.  Klik tombol **+** di pojok kanan atas, lalu pilih **New repository**.
3.  Isi kolom **Repository name** dengan format: `username-anda.github.io`
    *   *Contoh:* Jika username GitHub Anda adalah `agungdev`, maka nama repository-nya **WAJIB**: `agungdev.github.io`.
4.  Pilih opsi **Public**.
5.  Jangan centang "Add a README file", "Add .gitignore", atau "Choose a license". Biarkan kosong semua.
6.  Klik tombol hijau **Create repository**.

## Langkah 2: Hubungkan Kode Lokal ke GitHub

Sekarang, kembali ke folder proyek Anda di komputer.
Salin kode berikut dan jalankan di **Terminal** (bisa Command Prompt atau PowerShell) pada folder proyek Anda `f:\06_002\002A`:

```bash
git remote add origin https://github.com/USERNAME-ANDA/USERNAME-ANDA.github.io.git
git branch -M main
git push -u origin main
```

*(Ganti `USERNAME-ANDA` dengan username GitHub asli Anda)*

> **Catatan:** Jika muncul jendela login, silakan login dengan akun GitHub Anda.

## Langkah 3: Aktifkan GitHub Pages (Otomatis)

1.  Setelah perintah di atas sukses, kembali ke halaman repository Anda di GitHub.
2.  Refresh halaman tersebut. Anda akan melihat file-file kode Anda (`index.html`, `assets/`, dll) sudah masuk.
3.  Klik tab **Settings** (ikon roda gigi) di bagian atas.
4.  Di menu sebelah kiri, cari dan klik **Pages**.
5.  Pada bagian **Source**, pastikan sudah terpilih **Deploy from a branch**.
6.  Pada bagian **Branch**, pastikan terpilih **main** dan folder **/(root)**.
7.  Klik **Save** (biasanya sudah otomatis).

Tunggu sekitar 1-2 menit. Refresh halaman Settings > Pages tersebut.
Anda akan melihat kotak hijau bertuliskan:
**"Your site is live at https://username-anda.github.io/"**

Selamat! Portofolio Anda sudah online. 🚀

---

## Tips Tambahan: Cara Update Website

Jika di masa depan Anda mengedit kode (misal: menambah proyek baru), caranya sangat mudah:

1.  Edit kode di komputer seperti biasa.
2.  Buka terminal di folder proyek.
3.  Ketik 3 perintah sakti ini:
    ```bash
    git add .
    git commit -m "Update portofolio saya"
    git push
    ```
4.  Tunggu 1-2 menit, website online Anda akan otomatis terupdate.
