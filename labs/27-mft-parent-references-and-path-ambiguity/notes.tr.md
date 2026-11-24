# Gün 27 — MFT Parent Referansları ve Yol Belirsizliği

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](lab.py)

26. günde aynı dosyanın birden fazla adı olabileceğini gördük. Bugün her isme üst dizin (parent) indeksi ve sequence değerini ekliyoruz. Aynı dosya adı farklı dizinde bulunabilir. Üst dizin aynıysa olası rename, farklıysa olası move olarak değerlendirilir. Parent sequence değişmişse belirsizlik raporlanır. Çoklu bağlantı ve eksik ad bilgisi de ayrı sonuç verir.

**Sorular:** Dosya adı neden tek başına yeterli değil? Parent referansı yeniden kullanılırsa ne olur? Snapshot neden gerçek olay sırasını kesin göstermez?

Gerçek NTFS veya Windows API kullanılmaz; tüm kayıtlar hayalîdir. Tam yol veya olay zaman çizelgesi oluşturulmaz.

## Çalıştır
```bash
python3 labs/27-mft-parent-references-and-path-ambiguity/lab.py
python3 test_all.py
```
