# Gün 29 — FILETIME Tam Dönüşüm ve Özel Değerler

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](lab.py)

28. günde FILETIME dönüşümünde mikrosaniye altı kalanı koruduk. Bugün kayıpsız gidiş-dönüşü doğruluyoruz: UTC datetime ve 0–9 arası kalan ile tam sayı aritmetiği kullanarak orijinal tick sayısına dönüyoruz.

Sıfır bazı alanların tanımında eksik değer olabilir; aritmetik olarak ise 1601 başlangıcıdır. Hayalî zero_is_missing politikası bu ayrımı gösterir, genel Windows kuralı değildir.

**Alıştırma:** OFFSET+7 ve OFFSET-1 kalanını tahmin et, gidiş-dönüşü doğrula. Sıfırı iki politikayla karşılaştır. Sayısal hassasiyetin zaman doğruluğunu neden kanıtlamadığını açıkla. Dokuz dönüşüm ve dokuz sınır kontrolü vardır. Gerçek Windows API veya adli kayıt kullanılmaz.

## Çalıştır
```bash
python3 labs/29-filetime-exact-roundtrips-and-sentinel-values/lab.py
python3 test_all.py
```
