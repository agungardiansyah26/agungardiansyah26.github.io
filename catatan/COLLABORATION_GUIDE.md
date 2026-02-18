# Panduan Kolaborasi di GitHub

Jika Anda ingin orang lain (misalnya: **Jules Web**, teman, atau developer lain) ikut mengupdate website portofolio ini, Anda bisa melakukannya dengan fitur **Collaborators** di GitHub.

## Bagian 1: Mengundang Kolaborator

1.  Buka repository portofolio Anda di **GitHub.com**.
2.  Klik tab **Settings** (ikon roda gigi) di bagian atas.
3.  Di menu sebelah kiri, pilih **Collaborators**.
4.  Klik tombol hijau **Add people**.
5.  Masukkan username GitHub milik kolaborator (misal: username Jules Web).
6.  Pilih username tersebut dan klik **Add to this repository**.
7.  GitHub akan mengirim email undangan ke kolaborator tersebut. Mereka harus membuka email dan mengklik **Accept Invitation**.

## Bagian 2: Alur Kerja Kolaborasi

Setelah undangan diterima, kolaborator bisa ikut mengubah kode. Berikut alurnya:

### 1. Kolaborator Melakukan Update
Kolaborator akan:
*   Mendownload kode (`git clone`).
*   Mengedit file (tambah proyek, ubah warna, dll).
*   Mengirim perubahan kembali ke GitHub (`git push`).

### 2. Anda Mengambil Update (PENTING!)
Setiap kali kolaborator selesai melakukan update, kode di komputer Anda akan menjadi **"ketinggalan zaman"** (outdated) dibandingkan yang ada di GitHub.

Supaya komputer Anda punya update terbaru dari mereka, Anda **WAJIB** menjalankan perintah ini di terminal **sebelum** Anda mulai mengedit apa pun:

```bash
git pull
```

> **Ingat:** Rutinitas sebelum mulai kerja adalah `git pull` dulu.

## Ringkasan Perintah

| Aksi | Perintah Terminal |
| :--- | :--- |
| **Ambil update teman** | `git pull` |
| **Cek status file** | `git status` |
| **Simpan perubahan** | `git add .` lalu `git commit -m "Pesan"` |
| **Kirim ke GitHub** | `git push` |
