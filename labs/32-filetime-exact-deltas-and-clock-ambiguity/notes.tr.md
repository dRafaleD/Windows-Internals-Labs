# Gün 32 — FILETIME Tam Fark Hesabı ve Saat Belirsizliği

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](lab.py)

31. günde FILETIME high/low alanlarından tick oluşturduk. Bugün önce tam sayı farkını alıp saniyeyi Fraction ile ifade ediyoruz. Komşu tick'ler Python mikrosaniye gösterimi aynı olsa da 100 ns farklıdır. Belirsizlikler tick cinsindendir ve aralıkların örtüşmesi kesin sıra iddiasını engeller. On bir örnek tek tick, negatif fark, bir saniye, temas eden aralık ve geçersiz değer içerir. Her gözlemde beş tick belirsizlik varken 10 ve 11 tick farkını karşılaştır. Çözünürlük ile saat doğruluğunu ayır. Bu yalnızca hayalî aritmetik örnektir; gerçek Windows sentinel ve kaynak anlamları ayrı incelenmelidir.

## Çalıştır
```bash
python3 labs/32-filetime-exact-deltas-and-clock-ambiguity/lab.py
python3 test_all.py
```
