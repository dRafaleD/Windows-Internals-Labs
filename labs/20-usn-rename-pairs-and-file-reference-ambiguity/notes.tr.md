# Gün 20 — USN Rename Kayıtları ve Dosya Referansı Belirsizliği

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 19. günden devam
Önceki gün aynı sayısal file ID'nin farklı zamanlarda **başka nesneyi** gösterebileceğini öğrendik. Şimdi bu ayrımı **NTFS USN Journal'daki yeniden adlandırma olayları** üzerinde düşünelim.

**USN Journal:** NTFS'de dosya değişikliklerine ilişkin kayıt tutan mekanizma. **RENAME_OLD_NAME:** dosyanın eski adıyla ilgili neden bayrağı. **RENAME_NEW_NAME:** yeni adla ilgili neden bayrağı. **File reference:** dosya nesnesini tanımak için kullanılan kayıt bilgisi.

Hayalî iki kaydın aynı volume, file ID ve **oyuncak epoch** değerini taşıması; ayrıca USN sırasının artması beklenir. Farklı disk, yeniden kullanılmış kimlik, yanlış sıra ve eksik kayıt durumlarında eşleştirme reddedilir.

**Önemli:** gerçekte USN nedenleri tek bir metin değil, **bit flag** değerleri olabilir. `toy_epoch` gerçek NTFS alanı değildir. Kayıt çifti eşleşmesi **kimin** yeniden adlandırdığını ispatlamaz.

## Çalıştırma
~~~bash
python3 labs/20-usn-rename-pairs-and-file-reference-ambiguity/lab.py
python3 test_all.py
~~~

## Sorular
USN kayıtları neden yalnızca dosya adına göre eşleştirilmemeli? File ID yeniden kullanılırsa ne olur? Journal'dan bazı kayıtlar silinmiş veya kaybolmuşsa hangi belirsizlik doğar?

## Sınırlar
Gerçek Windows sistemine, NTFS diske veya USN Journal'a erişmez. Tamamen sentetik eğitim örneğidir.
