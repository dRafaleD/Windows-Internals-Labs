# Gün 30 — FILETIME Little-Endian Kayıt Çözümleme

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](lab.py)

29. günde tam dönüşüm ve alana özgü sentinel değerlerini inceledik. Şimdi hayalî sekiz baytlık alanı unsigned little-endian biçiminde çözüyoruz. Unix epoch 116444736000000000 FILETIME tick'tir; baytları 00 80 3e d5 de b1 9d 01. Mikrosaniye altındaki kalanı sakla ve sıfırın eksik anlamına geldiği hayalî alan sözleşmesini normal aritmetik sıfırdan ayır. Hex değeri elle çöz, bayt sırasını ters çevirip farkı incele ve eksik uzunlukta alan ekle. Dokuz alan senaryosu ve üç kontrol var. Gerçek NTFS ayrıştırıcı veya Windows API değildir; sentinel anlamı gerçek alana göre belirlenir.

## Çalıştır
```bash
python3 labs/30-filetime-little-endian-record-decoding/lab.py
python3 test_all.py
```
