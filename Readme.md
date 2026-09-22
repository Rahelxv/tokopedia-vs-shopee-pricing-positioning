# Analisis Komparatif Positioning Harga Produk Elektronik: Tokopedia vs Shopee

Analisis komparatif harga produk kategori **Elektronik** pada dua marketplace terbesar di Indonesia menggunakan uji **Mann-Whitney U**, untuk membuktikan signifikansi perbedaan harga serta merumuskan rekomendasi bisnis bagi penjual, pelanggan, dan pihak marketplace.

> **Status:** Selesai — 22 September 2026
> **Analis:** Rahel ([@Rahelxv](https://github.com/Rahelxv))

---

## 1. Latar Belakang

Tokopedia dan Shopee merupakan dua platform e-commerce dengan pangsa akses terbesar di Indonesia, menopang pasar transaksi digital yang tumbuh dari Rp205,5 triliun (2019) menjadi Rp487,01 triliun (2024) (Bank Indonesia, 2025). Meskipun sama-sama beroperasi di kategori Elektronik, kedua platform menunjukkan pola harga yang tampak sangat berbeda pada pengamatan awal.

Memahami apakah perbedaan ini nyata secara statistik — dan apa yang mendasarinya — penting baik bagi pelanggan (memilih platform sesuai kebutuhan) maupun bagi penjual (menempatkan produk di platform yang tepat).

## 2. Tugas Bisnis (Business Task)

> Membuktikan signifikansi perbedaan harga produk elektronik antara Tokopedia dan Shopee, memahami faktor yang mendasarinya, serta merumuskan rekomendasi aksi bagi seluruh pihak terkait.

**Pertanyaan yang dijawab:**
- Secara statistik, apakah ada perbedaan signifikan pada harga yang ditawarkan kedua marketplace?
- Apa alasan yang mendasari terjadinya (atau tidak terjadinya) perbedaan tersebut?
- Apa rekomendasi bagi penjual, pelanggan, hingga marketplace itu sendiri?

**Indikator keberhasilan:**
1. Berhasil menunjukkan ada/tidaknya perbedaan harga dan kategori barang
2. Berhasil memahami alasan di balik fenomena tersebut
3. Berhasil merumuskan rekomendasi *actionable* bagi penjual, pelanggan, dan marketplace

## 3. Metodologi

Proyek ini menggunakan kerangka kerja **uji hipotesis non-parametrik**, dengan tahapan berikut:

| Tahap Analisis | Deskripsi |
| --- | --- |
| **Data Cleaning** | Standarisasi format harga, penanganan kolom kategori & jumlah terjual |
| **Statistik Deskriptif** | Mean, median, standard deviation, skewness, kurtosis, IQR per platform |
| **Uji Normalitas** | Shapiro-Wilk test untuk menentukan pendekatan uji yang sesuai |
| **Uji Mann-Whitney U** | Uji non-parametrik untuk membandingkan median dua kelompok independen |
| **Effect Size** | Rank-Biserial Correlation & Common Language Effect Size (CLES) |
| **Analisis Komposisi Produk** | Perbandingan kategori, estimasi nilai penjualan, dan pola algoritma tampilan |
| **Rekomendasi Aksi** | Disusun berjenjang untuk penjual, pelanggan, dan marketplace |

## 4. Data

| Data | Sumber | Cakupan | Keterangan |
| --- | --- | --- | --- |
| Harga produk Tokopedia | Halaman kategori Elektronik, Tokopedia | 69 baris × 3 kolom | Scraping otomatis (Scrapy + Playwright), guest mode |
| Harga produk Shopee | Halaman kategori Elektronik, Shopee | 60 baris × 3 kolom | Pengambilan manual, guest mode/incognito |

Kedua pengambilan data dilakukan tanpa akun (guest mode), memakai kondisi private/incognito atau cookies bersih, dan IP netral untuk meminimalkan bias personalisasi algoritma rekomendasi.

## 5. Ringkasan Temuan Utama

- **Uji normalitas (Shapiro-Wilk)** menunjukkan harga di kedua platform tidak berdistribusi normal (Tokopedia W = 0,3994; Shopee W = 0,4716; p < 0,001 untuk keduanya) — mengarahkan analisis ke uji non-parametrik.
- **Uji Mann-Whitney U** (U = 4.138, p < 0,001) membuktikan perbedaan median harga yang signifikan secara statistik, dengan effect size sangat besar (rank-biserial r ≈ -0,999; CLES ≈ 0,9995) — **99,95% kemungkinan** harga elektronik acak di Tokopedia lebih tinggi dari Shopee.
- **Median harga:** Tokopedia Rp2.381.000 vs Shopee Rp2.500 — selisih sekitar 950x, mencerminkan komposisi katalog yang berbeda kelas: Shopee didominasi elektronik kecil (lampu LED, saklar, stop kontak), Tokopedia didominasi elektronik rumah tangga besar (kulkas, mesin cuci, TV).
- **Pola algoritma rekomendasi** berbeda: Shopee memprioritaskan *low but frequent buy product* (populer, harga rendah), sedangkan Tokopedia memprioritaskan barang bernilai fungsi tinggi.
- **Estimasi pendapatan:** meskipun volume penjualan Tokopedia bervariasi lebar (1–10.000+ unit), mayoritas produknya menghasilkan estimasi nilai di atas Rp500 juta; Shopee terkonsentrasi di Rp10–50 juta akibat filter kurasi produk populer.
- **Validasi eksternal:** temuan ini konsisten dengan penelitian independen lain (Siregar, 2022; Yuni dkk., 2021) yang juga menemukan keunggulan Shopee pada dimensi harga & promosi.
- **Alasan mendasar** ditelusuri dari tiga sisi: strategi pemasaran (*shoppertainment* vs *trust*), model bisnis produk (*cross border import* vs UMKM lokal), dan branding (*Brand Awareness* Shopee vs *Brand Loyalty* Tokopedia).
- **Rekomendasi** disusun terpisah untuk penjual (memilih platform sesuai segmen produk), pelanggan (memilih sesuai prioritas harga vs kualitas), dan marketplace (Shopee perlu mengurangi ketergantungan pada *promotion addiction*; Tokopedia perlu menjaga rasio investasi kualitas-vs-ekspansi).

Detail lengkap perhitungan statistik, visualisasi distribusi, dan rekomendasi per pihak ada di dokumentasi proses dan laporan akhir.

## 6. Struktur Repository

```
.
├── code/      # Notebook: data cleaning, uji statistik, dan analisis komparatif
├── data/      # Data hasil scraping/pengambilan manual (Tokopedia & Shopee)
├── reports/   # Laporan akhir & dokumentasi proses analisis (PDF)
└── scrapy/    # Project Scrapy + Playwright untuk pengambilan data Tokopedia
```

| Folder | Isi |
| --- | --- |
| `code/` | `Data Cleaning Processing.ipynb` (pembersihan data), `Shopee-Tokopedia.ipynb` (statistik deskriptif & uji normalitas), `Analisis.ipynb` (uji Mann-Whitney U & effect size) |
| `data/` | Dataset harga produk elektronik Tokopedia dan Shopee |
| `reports/` | *Laporan Akhir - Analisis Komparatif Harga Produk Elektronik Shopee vs Tokopedia*, *Proses Teknis - Analisis Komparatif Positioning Harga Produk Elektronik* |
| `scrapy/` | Project Scrapy `market_places` dengan `scrapy_playwright` sebagai download handler |

## 7. Tools & Tech Stack

| Kategori | Tools |
| --- | --- |
| Pengambilan Data | Python, Scrapy, Scrapy-Playwright (Tokopedia); pengambilan manual (Shopee) |
| Pengolahan & Analisis Data | Pandas, SciPy (uji Shapiro-Wilk, Mann-Whitney U) |
| Visualisasi | Matplotlib, Seaborn |
| Presentasi | Microsoft PowerPoint |
| Version Control | GitHub |

## 8. Batasan & Catatan Metodologis

- Sample (69 baris Tokopedia, 60 baris Shopee) diambil dari halaman kategori Elektronik yang tampil saat pengambilan data — bukan mewakili seluruh populasi produk elektronik di kedua platform, melainkan mencerminkan produk yang ditampilkan pada halaman kategori yang diakses.
- Pengambilan data Shopee dilakukan secara manual (bukan otomatis seperti Tokopedia), sehingga ukuran sampel dan cakupan halaman yang terjangkau relatif lebih terbatas.
- Kolom jumlah terjual tidak dapat dibandingkan secara *apples-to-apples* antar platform — Shopee menampilkan produk hasil filter "populer" (nilai seragam tinggi), sedangkan Tokopedia menampilkan variasi penjualan yang lebih alami.
- Asal-usul produk (lokal vs impor) tidak diverifikasi langsung per item; klaim terkait *cross border* dan komposisi UMKM merujuk pada temuan penelitian eksternal, bukan hasil verifikasi pada data sampel ini.
- Kesimpulan dan rekomendasi berlaku spesifik untuk kategori **Elektronik** pada saat data diambil, dan tidak digeneralisasi ke seluruh kategori produk di kedua marketplace.

## 9. Author

**Rahel** — Data Analyst (portfolio project)
GitHub: [@Rahelxv](https://github.com/Rahelxv)

---

*Project ini dibuat sebagai bagian dari portofolio data analyst.*
