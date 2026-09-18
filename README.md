# 📷 IoT Camera Control Studio

Aplikasi kamera berbasis **Python, OpenCV, dan Tkinter** untuk menampilkan live preview kamera, mengatur parameter gambar secara software, serta mengambil foto single maupun burst capture.

## ✨ Fitur

* 🎥 Live camera preview secara real-time
* 🖼️ Pilihan resolusi:

  * `640x480`
  * `1280x720 (HD)`
  * `1920x1080 (FHD)`
* ☀️ Pengaturan **Exposure / Brightness** secara software
* 🔆 Pengaturan **ISO / Gain Multiplier** secara software
* 📸 Single capture menggunakan `Spacebar`
* 🔄 Burst capture dengan menahan `Spacebar`
* 💾 Foto otomatis disimpan ke folder `captured_images`
* ⌨️ `ESC` untuk keluar dari aplikasi
* 🔄 Reset parameter kamera ke kondisi normal

## 📁 Struktur Project

```text
project/
│
├── .venv/
│   └── Virtual environment Python
│
├── captured_images/
│   └── Folder penyimpanan hasil foto
│
├── camera.py
│   └── Program utama aplikasi kamera
│
└── README.md
    └── Dokumentasi project
```

## 🛠️ Teknologi

* **Python 3**
* **OpenCV** — akses kamera dan image processing
* **Tkinter** — graphical user interface
* **Pillow (PIL)** — menampilkan frame OpenCV pada Tkinter
* **NumPy** — pemrosesan array gambar

## 🚀 Instalasi

Pastikan **Python 3** sudah terinstall di komputer.

### 1. Clone repository

```bash
git clone https://github.com/atikamrlnd/IoT-Camera-Control.git
cd IoT-Camera-Control
```

### 2. Buat virtual environment

Jika `.venv` belum tersedia:

**Windows:**

```bash
python -m venv .venv
```

**Linux / macOS:**

```bash
python3 -m venv .venv
```

### 3. Aktifkan virtual environment

**Windows — Command Prompt:**

```bash
.venv\Scripts\activate
```

**Windows — PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

Setelah berhasil, biasanya terminal akan menampilkan:

```text
(.venv)
```

### 4. Install dependency

```bash
pip install opencv-python pillow numpy
```

> `tkinter` biasanya sudah tersedia bersama instalasi Python pada Windows. Pada beberapa distro Linux, Tkinter perlu di-install melalui package manager sistem.

## ▶️ Menjalankan Aplikasi

Pastikan virtual environment sudah aktif, kemudian jalankan:

```bash
python camera.py
```

Jika pada sistem menggunakan `python3`:

```bash
python3 camera.py
```

Jendela **IoT Camera Control Studio** akan terbuka dan kamera default komputer akan digunakan.

## 🎮 Kontrol Kamera

| Kontrol          | Fungsi                                       |
| ---------------- | -------------------------------------------- |
| `Spacebar` tekan | Mengambil satu foto                          |
| `Spacebar` tahan | Burst capture                                |
| `ESC`            | Keluar aplikasi                              |
| Resolution       | Mengubah resolusi kamera                     |
| Exposure         | Mengatur brightness/exposure secara software |
| ISO / Gain       | Mengatur penguatan brightness gambar         |
| Reset Parameter  | Mengembalikan parameter ke nilai normal      |

## 📸 Hasil Foto

Foto yang diambil akan otomatis disimpan pada:

```text
captured_images/
```

Format nama file:

```text
IMG_YYYYMMDD_HHMMSS_mmm.jpg
```

Contoh:

```text
IMG_20260918_081530_125.jpg
```

## ⚠️ Troubleshooting

### Kamera tidak ditemukan

Jika muncul pesan:

```text
Kamera tidak ditemukan atau gagal diakses!
```

pastikan:

1. Kamera terhubung dengan komputer.
2. Kamera tidak sedang digunakan aplikasi lain seperti Zoom, Google Meet, atau aplikasi kamera lainnya.
3. Permission kamera sudah diberikan kepada Python/aplikasi.
4. Coba tutup aplikasi lain yang sedang menggunakan kamera.
5. Pastikan kamera terdeteksi oleh sistem operasi.

### Tidak bisa mengaktifkan `.venv` di PowerShell

Jika PowerShell menolak menjalankan script, buka PowerShell sebagai user yang sesuai dan jalankan:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Kemudian aktifkan kembali:

```powershell
.venv\Scripts\Activate.ps1
```

## 📌 Catatan

Parameter **Exposure** dan **ISO / Gain** pada aplikasi ini diproses pada gambar setelah frame diperoleh dari kamera. Jadi pengaturan tersebut merupakan **software image processing**, bukan perubahan langsung terhadap shutter speed atau ISO hardware kamera.

Resolusi yang dipilih juga bergantung pada kemampuan kamera dan driver yang digunakan. Kamera dapat mengembalikan resolusi berbeda apabila resolusi yang diminta tidak didukung oleh hardware.

---

## 👨‍💻 Development

Project ini dibuat sebagai aplikasi sederhana untuk **camera control, image processing, dan GUI berbasis Python**.

```text
Python
   │
   ├── OpenCV ─────── Camera & Image Processing
   │
   ├── NumPy ──────── Image Matrix Processing
   │
   ├── Pillow ─────── Image Conversion
   │
   └── Tkinter ────── Graphical User Interface
```

**Main file:**

```text
camera.py
```

**Output directory:**

```text
captured_images/
```
