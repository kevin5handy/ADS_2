# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut  telah berdiri sejak tahun 2000 dan telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

### Permasalahan Bisnis
1.  **Tingkat Dropout yang Cukup Tinggi** 
2.  **Diperlukannya Pemahaman Faktor Penyebab Dropout**
3.  **Dibutuhkan sistem untuk mengantisipasi siswa Dropout**

### Cakupan Proyek
1. Analisis daya yang tersedia: Data wrangling dan EDA.
2. Prapemrosesan data untuk membangun sistem ML: Scaling, Encoding, Oversampling, dan PCA
3. Membangun model klasifikasi multikelas untuk memprediksi status siswa: Decision Tree dan Random Forest
4. Hyperparameter tuning: Grid Search
5. Evaluasi Model: berbagai metrik klasifikasi
6. Pembuatan business dashboard: Metabase
6. Pembuatan prototipe sistem ML berbasis Streamlit.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
```bash
pip install -r requirements.txt
```
**Tools Utama:**
    * Metabase: Sebagai platform utama untuk pembuatan dashboard dan visualisasi data.
    * Docker: Digunakan untuk menjalankan Metabase.
    * Python, Jupyter Notebook/Google Colab, Pandas, NumPy, Matplotlib, Seaborn untuk analisis data awal.

## Business Dashboard
Proyek ini menyertakan file database Metabase (`metabase.db.mv.db`) yang berisi semua konfigurasi, pertanyaan, dan dashboard yang telah dibuat.

Link: http://localhost:3000/public/dashboard/7166abdc-7929-40bb-be4f-84e674080889

Untuk mengakses dashboard di atas, Anda harus memastikan bahwa aplikasi Metabase berjalan di komputer lokal Anda. Jika Anda menjalankan Metabase menggunakan Docker, maka Anda perlu menyalakan Docker dan memastikan kontainer Metabase aktif dan berjalan agar dasbor dapat diakses.

Kesimpulan Dashboard:
    1. 32.1% Siswa terdata melakukan dopout
    2. Dropout banyak terjadi pada siswa dengan usia rentang 15-37.5 tahun.
    3. Dropout banyak terjadi pada siswa dengan rentang Admission Grade dan previous qualification grade 100-160.
    4. 90.57% dari siswa dropout adalah siswa yang tidak mendapatkan beasiswa.
    5. 52.9% dari siswa dropout adalah siswa yang tidak mendapatkan displaced.

## Menjalankan Sistem Machine Learning
**Menjalankan Sistem Machine Learning**
1. Buka terminal atau command prompt, navigasi ke direktori utama proyek Anda (tempat file app.py berada).
2. Jalankan perintah berikut:
```bash
  streamlit run app.py
```
3. Link Streamlit
https://caoimhin.streamlit.app/

## Conclusion
1. Telah dibuat business dashboard dan prototipe sistem ML untuk  sekolah agar bisa mengetahui berbagai faktor yang mempengaruhi siswa untuk dropout.
2. Algoritma random forest dipilih pada sistem ML ini.
3. Terdapat beberapa faktor utama yang mempengaruhi siswa untuk Dropout.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- Pihak sekolah perlu untuk mengkaji berbagai faktor terlampir yang memengaruhi banyaknya siswa dropout serta mengkaji kembali berbagai program dan kebijakan yang telah dibuat sebelumnya. Kebijakan harus berorientasi kepada kebaikan siswa. Sebagai contoh, ushakan terbukanya berbagai beasiswa untuk siswa, karena diketahui lebih dari 90% dari siswa dropout adalah siswa yang tidak mendapatkan beasiswa.
- menerapkan dan meningkatkan sistem machine learning yang telah dibuat untuk mengantisipasi siswa Dropout.
