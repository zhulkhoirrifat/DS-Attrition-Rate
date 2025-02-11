# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

### Permasalahan Bisnis

Permasalahan bisnis yang diderita oleh perusahaan Jaya Jaya maju adalah tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%. Kondisi ini berpengaruh dengan stabilitas perusahaan. Untuk menyelesaikan masalah bisnis ini harus mengidentifikasi permasalahan faktor apa saja yang menyebabkan tingginya attrition rate. 

### Cakupan Proyek

- Cleaning Data
- Melakukan Exploratory Data Analysis (EDA) untuk mengidentifikasi faktor-faktor penyebab tingginya attrition rate.
- Membuat dashboard untuk visualisasi
- Membuat model machine learning untuk prediksi potensi karyawan yang ingin melakukan attrition.

### Persiapan

Sumber data: [Jaya Jaya Maju Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:

- Install library yang akan digunakan

```
pip install -r requirements.txt
```

- Buka file prediction.py dan ubah variabel new_data untuk prediksi

```
new_data = pd.DataFrame([
        [35, 5, 5000, 2, 10, 5, 3, 3, 'Male', 'Bachelor', 'Technical Degree', 'Single',
         'Travel_Rarely', 'Medium', 'High', 'Very High', 'No', 'Excellent', 'High', 'Good']
    ], columns=numerical_features + categorical_features)
```

- Jalankan prediction.py
```
python prediction.py
```

## Business Dashboard

![istiabudi73 - dashboard](https://github.com/user-attachments/assets/78a36da2-6d75-4a02-98aa-313652ba888e)

Dashboard ini dibuat untuk memantau tingkat attrition (tingkat keluar/mutasi karyawan) di perusahaan. Dengan data ini, perusahaan dapat memahami pola dan faktor yang berkontribusi terhadap keluarnya karyawan, serta mengambil langkah-langkah strategis untuk meningkatkan retensi karyawan. Dashboard dapat diakses melalui tautan ini. [Tableau Public - Attrition](https://public.tableau.com/app/profile/istiabudi121/viz/Attrition_17392325586410/Dashboard1)

## Conclusion

1. Tingkat Attrition

    - Total attrition (karyawan yang keluar) adalah 179 karyawan.
    - Saat ini terdapat 1.291 karyawan aktif.
    - Tingkat attrition lebih tinggi pada laki-laki (10,21%) dibanding perempuan (6,71%).

2. Attrition Berdasarkan Job Role

    - Sales Executive (39), Research Scientist (38), dan Laboratory Technician (49) memiliki angka attrition tertinggi.
    - Manufacturing Director dan Human Resources memiliki attrition terendah.

3. Attrition Berdasarkan Departemen

    - Departemen Research & Development (107) memiliki jumlah attrition tertinggi.
    - Departemen Sales (66) juga memiliki tingkat attrition yang cukup tinggi.
    - Departemen Human Resources memiliki attrition yang sangat rendah.

4. Attrition Berdasarkan Job Level

    - Job level 1 memiliki attrition tertinggi (108 karyawan).
    - Job level 2 dan 3 juga mengalami attrition tetapi tidak sebanyak level 1.
    - Job level 4 dan 5 memiliki attrition yang lebih rendah, menunjukkan bahwa karyawan dengan jabatan lebih tinggi cenderung bertahan lebih lama.
    
5. Attrition Berdasarkan Pendidikan

    - Karyawan dengan pendidikan Bachelor memiliki attrition tertinggi (76).
    - Attrition cukup merata pada jenjang pendidikan lainnya, tetapi lebih rendah pada tingkat Doctor.

6. Distribusi Attrition Berdasarkan Gaji Bulanan

    - Attrition lebih banyak terjadi pada karyawan dengan gaji antara 4K - 7K.
    - Semakin tinggi gaji, semakin rendah tingkat attrition, kecuali pada gaji 13K dan 19K yang masih memiliki sedikit attrition.

### Rekomendasi Action Items (Optional)

- Fokus pada Job Level 1 dan Departemen Research & Development karena memiliki tingkat attrition yang tinggi.
- Perhatikan kesejahteraan karyawan di rentang gaji 4K - 7K, mungkin ada ketidakpuasan terkait kompensasi.
- Job Role seperti Sales Executive, Research Scientist, dan Laboratory Technician perlu strategi retensi khusus untuk mengurangi turnover.
- Karyawan dengan pendidikan Bachelor memiliki tingkat attrition tertinggi, bisa jadi karena ekspektasi karir yang lebih tinggi.
- Tingkatkan engagement bagi karyawan laki-laki, karena mereka lebih cenderung mengalami attrition dibanding perempuan.