# Gün 23 — USN Rename ve Süreç Bağlamını Karşılaştırma

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 22. günden devam
Önceki gün USN Journal kayıtlarında **toplama eksikliklerini** inceledik. Bugün hayalî bir dosya adı değişikliğini, aynı zaman aralığında kaydedilmiş **süreç olaylarıyla** karşılaştırıyoruz.

**Corroboration:** farklı kanıtların birbirini desteklemesi. **Process GUID:** süreç örneğini ayırt etmeye yardımcı olan kimlik. **Evidence gap:** kayıt toplama eksikliği. **Candidate:** olası eşleşme, kesin hüküm değil.

Kod önce eski/yeni ad kaydını dosya kimliği ve USN sırası açısından kontrol eder. Arada eksik kayıt varsa `UNCERTAIN_COLLECTION` der. Ardından ±2 saniyede aynı dosyaya ilişkin süreç olayı arar. Tek uygun olay varsa `PAIR_WITH_CONTEXT`; birden fazla süreç uygunsa `AMBIGUOUS_PROCESS_CONTEXT` sonucu verir.

**Dikkat:** bir sürecin zamanca yakın görünmesi, o eylemi gerçekleştirdiğini veya hangi kişinin başlattığını kesin kanıtlamaz.

## Çalıştır
```bash
python3 labs/23-usn-process-context-and-evidence-corroboration/lab.py
python3 test_all.py
```

## Sorular
Eksik USN kaydı sonucu neden zayıflatır? Yakın zamanlı süreç neden kesin başlatıcı demek değildir? Farklı Process GUID'ler aynı olaya yakınsa ne yapmalı?

## Sınırlar
Gerçek NTFS/Windows kaydı kullanılmaz; reason bitleri ve toy epoch hayalîdir.
