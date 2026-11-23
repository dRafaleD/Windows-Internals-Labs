# Gün 26 — MFT Çoklu Dosya Adları ve Rename Belirsizliği

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 25. günden devam
Önceki gün USN Rename kaydını MFT snapshot'ıyla karşılaştırdık. Bugün aynı dosyanın **birden fazla ada** sahip olabileceğini ele alıyoruz.

**Hard link:** aynı dosya içeriğine ve kaydına işaret edebilen başka bir ad/yol. **MFT snapshot:** dosya kaydının belirli andaki gözlemi. **Rename candidate:** kanıtlarla uyumlu olası ad değiştirme, kesin hüküm değil.

İlk örnekte `old.txt` isminin `new.txt` olarak değişmesi mantıklı görünüyor. Ancak sonraki snapshot'ta hem `old.txt` hem `new.txt` varsa `OLD_NAME_STILL_PRESENT` diyoruz. Başka adlar da varsa `MULTI_NAME_CONTEXT` sonucu veriyoruz. Dosya kimliği veya sequence uyuşmazlığı ayrıca raporlanıyor.

## Çalıştır
```bash
python3 labs/26-mft-multiple-names-and-rename-ambiguity/lab.py
python3 test_all.py
```

## Sorular
Bir dosyanın birden fazla adı olması neden önemlidir? Sonraki snapshot'ta eski ad hâlâ duruyorsa neden kesin rename dememeliyiz? Dosya indeksinin yeniden kullanılması nasıl yanlış eşleştirmeye neden olur?

## Sınırlar
Gerçek NTFS okumaz; USN flag'leri ve MFT verileri eğitim için uydurulmuştur.
