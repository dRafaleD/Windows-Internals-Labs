# Gün 28 — Uygulama Günü: FILETIME Dönüşümü ve Zaman Damgası

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](lab.py)

FILETIME, 1601-01-01 UTC başlangıcından geçen 100 nanosaniyelik aralıkları temsil eder. Python datetime mikrosaniye çözünürlüğünde olduğu için 10'a bölümden kalanı ayrıca saklıyoruz.

| Tick girdisi | Beklenen |
|---|---|
| 0 | 1601-01-01 UTC (yalnızca aritmetik yorum) |
| 1 | Başlangıç + 100 ns, kalan 1 |
| 10 | Başlangıç + 1 mikrosaniye |
| 116444736000000000 | Unix epoch |
| Unix offset + 10000000 | Unix epoch + 1 saniye |
| Negatif sayı | INVALID_TICKS |
| En büyük unsigned 64 bit | Python için OUT_OF_RANGE |

**Alıştırmalar:** Bir saniyeyi ve bir milisaniyeyi tick'e çevir. 13 decode örneğini tahmin et. 00:00 UTC ile 03:00 +03:00 değerlerini karşılaştır. Mikrosaniye ve kalan bilgisinden tam tick sayısını yeniden oluştur. Zaman damgası hassasiyeti ile olay zamanının doğruluğunu ayır.

Beklenen özet: 13 decode cases + 5 encode checks passed. Gerçek NTFS veya Windows API kullanılmaz. Bazı Windows alanlarında sıfır ve diğer özel değerler farklı anlamlar taşıyabilir; bu örnek yalnızca aritmetik dönüşümdür.

## Çalıştır
```bash
python3 labs/28-filetime-conversion-and-timestamp-practice/lab.py
python3 test_all.py
```
