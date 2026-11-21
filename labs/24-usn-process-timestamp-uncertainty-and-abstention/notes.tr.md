# Gün 24 — USN ve Süreç Zaman Belirsizliği ile Kanıt Değerlendirme

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 23. günden devam
Önceki gün USN yeniden adlandırma olayıyla süreç kaydını **yakın zamana** göre karşılaştırdık. Ancak zaman damgaları tam doğru olmayabilir.

**Timestamp uncertainty:** zaman bilgisinin hata payı. **Clock skew:** iki kaynağın saatlerinin farklı olması. **Interval overlap:** olayların olası zaman aralıklarının kesişmesi veya yeterince yaklaşması. **Abstention:** delil kesin değilse kesin sonuç vermemek.

Her kayıtta `zaman ± belirsizlik` bulunuyor. Dosya kimliği uyuşuyor ve aralıklar yeterince yakınsa **PAIR_WITH_POSSIBLE_CONTEXT** sonucu veriliyor. Birden fazla süreç adayı varsa **AMBIGUOUS_CONTEXT**, eksik USN toplaması varsa **UNCERTAIN_COLLECTION** sonucu öncelikli oluyor.

## Çalıştırma
```bash
python3 labs/24-usn-process-timestamp-uncertainty-and-abstention/lab.py
python3 test_all.py
```

## Sorular
İki zaman damgası neden tam eşit olmak zorunda değil? Saat kayması yanlış eşleşmeyi nasıl etkiler? Yakın süreç kaydı neden gerçek aktörün kesin ispatı değildir?

## Sınırlar
Gerçek Windows/NTFS kaydı yoktur. Reason bit değerleri ve `toy_epoch` hayalîdir.
