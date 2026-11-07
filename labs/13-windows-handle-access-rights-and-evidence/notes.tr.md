# Gün 13 — Windows Handle Erişim Hakları ve Delil Bağlamı

[English](notes.md) · [Türkçe](notes.tr.md) · [Uygulama](lab.py)

## Öğrenme amacı

Zararsız yerel veriyle **Windows Handle Erişim Hakları ve Delil Bağlamı** konusunun güven sınırlarını ve kanıt değerlendirmesini öğren.

## Temel kavramlar

1. Windows handle değerleri sürece özgü referanslardır; izin maskesi nesne üzerindeki yetkili işlemleri anlamaya yardım eder.

2. İstenen ve verilen yetkiler farklı olabilir. Maske, nesne türüne özgü haklar ve uygun Windows API ile yorumlanmalıdır.

3. Süreçte handle bulunması tüm izinlerin kullanıldığı anlamına gelmez. Bu örnek gerçek process handle'larını okumaz.

## Güvenli pratik

Önce kaynak kodunu oku ve sonucu tahmin et:

```bash
python lab.py
```

Çıktı sentetiktir; gerçek sisteme komut gönderilmez.

## Görevler

1. Girdi verisini ve güvenilmeyen alanları belirle.
2. Bir negatif ya da sınır örneği ekleyip test et.
3. Gözlem ve yorum farkını açıkla.
4. Gerçek ortamda hangi doğrulamaların gerektiğini yaz.

## Kontrol soruları

- Tek gösterge yeterli mi?
- Yanlış pozitif veya eksik kayıt nasıl oluşabilir?
- Sonucu tekrar üretmek için hangi girdileri saklamalısın?

## Güvenlik ve sınırlamalar

Bu çalışma gerçek malware, bulut hesabı, sistem müdahalesi veya dış ağ gerektirmez. Modelin basitliği gerçek platformla birebir eşitlik iddiası taşımaz.
