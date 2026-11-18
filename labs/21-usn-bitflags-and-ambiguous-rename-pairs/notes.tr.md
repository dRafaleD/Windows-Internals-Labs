# Gün 21 — USN Bit Flag'leri ve Belirsiz Rename Eşleşmeleri

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 20. günden devam
Önceki gün eski dosya adı ve yeni dosya adı kayıtlarını eşleştirdik. Şimdi iki yeni sorun var: USN nedenleri **birden çok bit flag** taşıyabilir ve yeni ad için **birden çok eski ad adayı** bulunabilir.

**Bitmask:** birkaç işareti tek sayıda tutma biçimi. `OLD_NAME | CLOSE` iki neden bitinin birlikte bulunduğu hayalî kayıttır. **Pair candidate:** olası kayıt çifti, henüz kesinleşmiş olay değil. **Ambiguous:** birden fazla olası aday olduğu için eşleşmenin belirsiz kalması.

Kod aynı volume/file ID/oyuncak epoch bilgisini ve USN sırasını kontrol ediyor.
- Bir aday: `PAIR_CANDIDATE`
- Birden çok aday: `AMBIGUOUS`
- Yeterli veri yok: `INSUFFICIENT`

**Not:** bit değerleri ve `toy_epoch` gerçek NTFS sabitleri değildir. Gerçek USN Journal için Windows kayıt biçimine ve gerçek reason flag değerlerine bakılmalıdır.

## Çalıştır
~~~bash
python3 labs/21-usn-bitflags-and-ambiguous-rename-pairs/lab.py
python3 test_all.py
~~~

## Sorular
Reason değerine doğrudan eşitlik yerine bit kontrolü neden yapılır? İki aday olduğunda neden birini rastgele seçmemeliyiz? Eksik journal kayıtları sonucu nasıl etkiler?

## Sınırlar
Gerçek Windows sistemi, dosya, NTFS birimi veya USN Journal okunmaz; tamamen yerel Python simülasyonudur.
