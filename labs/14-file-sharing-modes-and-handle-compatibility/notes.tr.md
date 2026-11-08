# Gün 14 — Windows Dosya Paylaşım Modları ve Handle Uyumluluğu

[English](notes.md) · [Türkçe](notes.tr.md) · [Çevrimdışı lab](lab.py)

## Amaç
13. günde handle için **erişim maskesi** konusunu gördük. Şimdi **istenen erişim (desired access)** ile **paylaşım modu (share mode)** arasındaki farkı öğreniyoruz. Bir programın dosyayı okuma hakkı olması, aynı dosyanın başka programlarca eş zamanlı açılabileceği anlamına gelmez.

## Windows'taki iki ayrı kontrol
`CreateFile` gibi API'lerde hem istenen erişim hem de `FILE_SHARE_READ`, `FILE_SHARE_WRITE`, `FILE_SHARE_DELETE` paylaşım bayrakları kullanılır. Bunlar **ACL/DACL yetkilendirmesinin yerini tutmaz**; yalnız eş zamanlı açma isteklerinin uyumluluğunu etkiler.

Basitleştirilmiş uyumluluk kuralı:
1. Yeni handle'ın istediği erişim, **mevcut handle'ın** izin verdiği paylaşım kapsamına uymalıdır.
2. Mevcut handle'ın istediği erişim de **yeni handle'ın** paylaşım bayraklarıyla uyumlu olmalıdır.

Gerçek Windows; daha ayrıntılı erişim hakları, dosya nesneleri, silinmeyi bekleyen durum ve API kuralları içerir. Bu program yalnız öğretici bir modeldir.

## Pratik
```bash
python lab.py
```
Sentetik ilk handle READ erişimiyle açılmış ve READ paylaşımı vermiştir. İkinci okuyucu kabul edilir; yazıcı paylaşım kısıtı yüzünden reddedilir. Yeni okuyucu kendi paylaşımını NONE yaparsa mevcut okuyucuyla uyumsuz olur. **Gerçek dosya açılmaz.**

## Görevler
1. Yalnız READ isteyen ama paylaşımı NONE olan yeni handle neden reddedilebilir?
2. Mevcut paylaşımı READ | WRITE yap ve sonuçları karşılaştır.
3. **Share mode uyumluluğu** ile **ACL/DACL yetkilendirmesini** ayır.
4. Gerçek bir “sharing violation” için hangi süreç, dosya yolu, zaman ve handle bilgileri gerekir?
5. Açık handle bulunmasının neden mutlaka dosya yazıldığı anlamına gelmediğini açıklayarak yanlış çıkarım örneği ver.

## Güvenlik
Yalnız uydurma handle'lar ve Python standart kütüphanesi kullanılır. Win32 API çağrısı, gerçek dosya değiştirme veya bellek okuma yoktur. Uyumluluk, işlemin yapıldığını kanıtlamaz.
