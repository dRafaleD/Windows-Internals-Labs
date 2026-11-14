# Gün 17 — Hard Link, File ID ve Dosya Yolu Belirsizliği

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 16. günden devam
Yeniden adlandırma, dosya yolu ile dosya kimliğinin aynı şey olmadığını gösterdi. **Hard link (sabit bağlantı)** ise aynı dosya nesnesine **birden fazla dosya adı** verilmesine izin verir.

Hayalî modelde `first.txt` ve `second.txt` aynı 100 numaralı dosyayı gösterir. İlk ad kaldırılınca ikinci ad geçerli kalır. İki ad da kaldırıldığında açık **handle** nesneyi bu modelde hâlâ erişilebilir tutar. Eski yol daha sonra 101 numaralı yeni nesneye verilebilir.

## Çalıştır
```bash
python3 labs/17-hard-links-file-ids-and-path-ambiguity/lab.py
python3 test_all.py
```

## Sorular
İki yol neden aynı dosyayı gösterebilir? Adli analizde yalnızca yola güvenmek neden yanıltıcı? Açık handle ile dosya adı arasındaki ilişki nedir?

## Sınır
Bu gerçek NTFS veya Win32 davranışının tam modeli değildir; hiçbir dosyaya veya Windows API'sine erişmez.
