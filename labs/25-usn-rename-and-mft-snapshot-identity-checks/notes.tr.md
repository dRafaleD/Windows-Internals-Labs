# Gün 25 — USN Rename ve MFT Snapshot Kimlik Kontrolü

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 24. günden devam
Önceki gün USN ve süreç kayıtlarındaki **zaman belirsizliğini** değerlendirdik. Bugün dosya adı değişikliğine ilişkin kaydı, dosyanın **MFT snapshot** bilgileriyle karşılaştırıyoruz.

**MFT (Master File Table):** NTFS dosya kayıtları tablosu. **File reference sequence:** aynı sayısal dosya indeksinin farklı dönemlerde kullanılmasını ayırt etmeye yardım eden kimlik parçası. **Snapshot:** belirli anda gözlemlenen durum.

Modelde eski ve yeni dosya adının USN kayıtları eşleştirilir. Sonra iki hayalî MFT snapshot'ının volume, dosya indeksi, sequence, ad ve zamanı karşılaştırılır. Sequence farklıysa `FILE_REFERENCE_REUSE`, toplama eksikse `UNCERTAIN_COLLECTION`, tüm gözlemler tutarlıysa yalnızca `CONSISTENT_CANDIDATE` sonucu verilir.

**Dikkat:** snapshot gerçek dosya geçmişinin tamamını kanıtlamaz. Bu sonuç, eylemi yapan kişiyi veya süreci göstermez.

## Çalıştır
```bash
python3 labs/25-usn-rename-and-mft-snapshot-identity-checks/lab.py
python3 test_all.py
```

## Sorular
File reference sequence neden önemlidir? MFT snapshot neden tek başına rename olayının kanıtı değildir? USN Journal eksikse raporda neyi belirtmeliyiz?

## Sınırlar
Gerçek NTFS diski veya Windows API kullanılmaz; tüm kayıtlar sentetiktir.
