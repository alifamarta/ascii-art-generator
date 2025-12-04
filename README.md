# ASCII Art Generator

ASCII Art Generator ini merupakan Program yang mengubah gambar menjadi teks ASCII. Dengan membaca file gambar dari path yang dimasukkan, proram akan mengubah tiap piksel ke dalam karakter ASCII. Hasil dari program yang telah dijalankan akan ditampilkan ke dalam konsol dan juga disimpan ke `ascii_image.txt`. Program ini menggunakan library `Pillow` (module `PIL`).

## Cara Menjalankan (Windows PowerShell)

1. Buat virtual environment lalu aktifkan:

```powershell
python -m venv env
.\env\Scripts\Activate
```

Jika PowerShell menolak menjalankan skrip aktivasi karena kebijakan eksekusi, jalankan :

```powershell
& .\env\Scripts\Activate.ps1
```

2. Install dependency:

```powershell
pip install -r requirements.txt
```

3. Jalankan program:

```powershell
python .\ascii-gen.py
```

### Note:
- Jika muncul error pada import `PIL`, pastikan `Pillow` telah terpasang.

