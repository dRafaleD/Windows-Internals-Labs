# Gün 19 — File ID Yeniden Kullanımı ve Olayların İlişkilendirilmesi

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 18. günden devam
Sayısal file ID değerinin zaman içinde tekrar kullanılabileceğini öğrendik. Bu gün aynı kimlik veya dosya yolunu gördüğümüzde **iki ayrı nesneyi yanlışlıkla aynı dosya kabul etmemeyi** çalışıyoruz.

Hayalî kayıt alanları: disk birimi (`volume`), file ID, oyuncak nesil sayacı (`epoch`), yol, içerik hash'i ve gözlem zamanı.

- **SAME_TOY_OBJECT:** birim, ID ve oyuncak nesil aynı.
- **REUSED_NUMERIC_ID:** aynı birim ve ID, ama farklı nesil.
- **PATH_REUSED:** aynı dosya yolu başka nesneye geçmiş.
- **SAME_CONTENT_ONLY:** farklı nesneler aynı bayt içeriğine sahip.
- **NO_DIRECT_LINK:** doğrudan eşleşme yok.

**Epoch gerçek NTFS alanı değildir!** Gerçek Windows adli incelemesinde volume bilgisi, dosya referansı/sıra bilgisi, USN Journal, zaman damgaları ve delil kökeni ayrı doğrulanmalıdır.

## Çalıştırma
~~~bash
python3 labs/19-file-identity-reuse-and-event-correlation/lab.py
python3 test_all.py
~~~

## Sorular
Neden file ID'nin yanında volume gerekir? Aynı dosya adı başka bir nesneye nasıl geçer? Dosya kimliği veya hash eşleşmesi neden çalıştırmayı başlatan kişiyi kanıtlamaz?

## Sınırlar
Hiçbir gerçek dosya, NTFS tablosu veya Windows API'si incelenmez; sekiz hayalî senaryodur.
