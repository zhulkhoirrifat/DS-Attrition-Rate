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

Business dashboard yang ada dibuat untuk memonitor faktor faktor apa saja yang mempengaruhi attrition karyawan.

## Conclusion

Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- action item 1
- action item 2
