# E-Commerce Customer Churn Prediction

Project ini bertujuan untuk menghasilkan model machine learning klasifikasi yang dapat memprediksi customer churn. Label 0 : not churn, label 1 : churn

**Problem Statement**

Untuk menghindari terjadinya customer churn maka perusahaan perlu mengoptimalkan strategi retensi untuk mempertahankan pelanggan. Perusahaan juga perlu mengurangi risiko biaya retensi yang dikeluarkan yang kurang optimal akibat strategi retensi tidak tepat sasaran.

**Goals**

- Melakukan prediksi customer churn
- Strategi retensi tepat sasaran kepada pelanggan yang mungkin churn.
- Biaya retensi dialokasikann secara efisien

**Data**

Dataset yang digunakan terdiri dari 11 kolom dan 3270 baris

**Conclusion**

- Metrik yang digunakan adalah F2-score.
- Model yang paling baik dalam memprediksi customer churn adalah model **LGBMClassifier** dengan kombinasi hyperparameter terbaik hasil hyperparameter tuning. 
- Biaya retensi jika tidak ada prediksi dan tidak menggunakan machine learning:
654 x $20 = $13080
- Biaya jika menggunakan machine learning: $3960
- Perusahaan dapat menghemat 70% biaya yang dikeluarkan untuk rentensi pelanggan
