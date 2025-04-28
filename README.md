# Analisis Tren Keberlanjutan Dalam Industri Fashion

Sebuah model prediktif untuk memperkirakan apakah sebuah brand ramah lingkungan berdasarkan faktor-faktornya seperti bahan yang digunakan, jejak karbon, jenis sertifikasi, program daur ulang, dan atribut pendukung lainnya.

## Struktur File

```
├── app.py             # Endpoint API utama
├── model.pkl           # File model Machine Learning yang telah dilatih
├── scaler.pkl          # File scaler untuk normalisasi fitur input
├── requirements.txt    # Daftar dependency yang dibutuhkan
```

## Fitur API

- Prediksi status manufaktur ramah lingkungan
- Menerima input melalui metode POST
- Hasil prediksi: `Yes` atau `No`
