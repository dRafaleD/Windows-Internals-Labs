# Gün 22 — USN Toplama Eksikleri ve Rename Kanıtında Belirsizlik

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 21. günden devam
Önceki gün **USN bit flag** ve birden fazla eski ad adayını incelendik. Bugün **eksik toplanmış kayıtlar** durumunda ne yapılacağını öğreniyoruz.

**Collection gap:** delil toplama işleminin belirli bir aralıktaki kayıtları kapsamadığının bilinmesi. **Abstention:** yeterli veri olmadığında kesin eşleştirme yapmamak.

Örneklerde bir eski ad ve bir yeni ad kaydı aynı dosya kimliğine ait görünebilir. Ancak arada toplanamamış journal kayıtları varsa **UNCERTAIN_GAP** döneriz. Birden fazla eski ad adayı varsa **AMBIGUOUS**, hiç aday yoksa **INSUFFICIENT** döneriz.

**Önemli:** gerçek NTFS USN değerleri art arda giden basit kayıt sıra numaraları değildir. İki USN sayısının farkına bakıp tek başına kayıp kayıt var diyemeyiz. Buradaki eksik aralıklar **ayrıca belirtilmiş varsayımsal toplama eksiklikleridir**.

## Çalıştır
```bash
python3 labs/22-usn-collection-gaps-and-rename-evidence-abstention/lab.py
python3 test_all.py
```

## Sorular
Toplama eksikliği bir eşleşmeyi neden şüpheli hale getirir? USN değerinin atlaması neden doğrudan kayıt kaybı demek değildir? Rename için hangi ek delilleri ararsın?

## Sınırlar
Gerçek NTFS verisi veya Windows API kullanılmaz. Bit değerleri ve toy epoch gerçek Windows sabitleri değildir.
