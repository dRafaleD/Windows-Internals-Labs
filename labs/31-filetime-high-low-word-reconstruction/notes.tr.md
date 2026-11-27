# Gün 31 — FILETIME High/Low Word Birleştirme

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](lab.py)

30. günde FILETIME baytlarını little-endian çözdük. Bugün 64 bit değeri iki unsigned 32 bit parçadan oluşturuyoruz. High word 32 bit sola kaydırılır ve low word ile birleştirilir. Örnek: low=0xffffffff, high=0 için 4294967295; low=0, high=1 için 4294967296. Yedi dönüşüm ve yedi geçersiz girdi senaryosu sınırları inceler. Unix epoch için iki parçayı hesaplayıp little-endian baytlarını karşılaştır. Parçaların yer değiştirmesi değeri değiştirir. Bu aritmetik örnektir; gerçek Windows API veya disk erişimi yoktur.

## Çalıştır
```bash
python3 labs/31-filetime-high-low-word-reconstruction/lab.py
python3 test_all.py
```
