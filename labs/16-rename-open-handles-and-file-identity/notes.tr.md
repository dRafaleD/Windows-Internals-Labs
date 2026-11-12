# Gün 16 — Yeniden Adlandırma, Açık Handle ve Dosya Kimliği

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 15. günden devam
15. günde bir dosyanın silinme isteği sırasında açık handle'ların ne yaptığını öğrendik. Bugün, **dosyanın yolu değişse bile daha önce açılmış handle'ın aynı dosya nesnesine işaret edebileceğini** inceliyoruz.

**Handle:** bir sürecin dosya veya başka bir kaynak için tuttuğu açık referans.
**File identity:** dosyanın yalnızca adından ibaret olmayan nesne kimliği.
**Share mode:** farklı açma işlemlerinin beraber bulunabilmesi için izin verilen kullanım türleri.
**FILE_SHARE_DELETE:** açık handle varken silme/yeniden adlandırma türündeki başka işlemlere izin verebilen paylaşım bayrağı. Bu bayrak **işlem yapma yetkisi vermez**.

## Hayalî model
`old.txt` isimli nesnenin file ID değeri 101. Başka dosyanın kimliği 102.
- Açık handle DELETE paylaşımına izin vermiyorsa yeniden adlandırma reddedilir.
- İzinli paylaşım olsa da işlemi başlatan kişi yetkisizse reddedilir.
- Yeni isim başka bir nesnede kullanılıyorsa reddedilir.
- İzinli yeniden adlandırmadan sonra `old.txt` yolu yok olur, `new.txt` yolu aynı dosya kimliğini gösterir.
- Eski handle halen 101 kimlikli dosya nesnesine bağlıdır.

Bu, gerçek Windows çekirdeğinin birebir davranışı **değildir**; salt bellek içi öğretici bir soyutlamadır.

## Çalıştırma
~~~bash
python3 labs/16-rename-open-handles-and-file-identity/lab.py
python3 test_all.py
~~~

## Sorular
1. Dosya adı değişse bile açık handle neden geçerli kalabilir?
2. Paylaşım izni neden işlem yapma yetkisi anlamına gelmez?
3. Adli incelemede dosya yolu ile file ID neden ayrı kayıt edilmeli?
4. Hedef yol zaten varsa hangi ek Windows seçenekleri önem kazanır?
5. Hard link ve reparse point bu modeli neden karmaşıklaştırır?

## Güvenlik
Gerçek dosya, Registry, servis veya Windows API çağrısı kullanılmaz. Her şey Python nesneleriyle simüle edilir.
