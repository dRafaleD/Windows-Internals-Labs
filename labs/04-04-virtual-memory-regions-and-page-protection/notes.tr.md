# Gün 04 — Sanal Bellek Bölgeleri, Sayfalar ve Korumalar

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Amaç ve bağlam

Süreçler sanal adreslerle çalışır. Bellek yöneticisi bölgeleri sayfalara ve koruma izinlerine eşler; sanal adres doğrudan fiziksel RAM adresi değildir.

## Temel teknik kavramlar

1. Windows'ta reserve ile commit farklı kavramlardır. Rezerve edilen alan otomatik olarak kullanılabilir commit edilmiş bellek değildir.

2. Okuma, yazma ve çalıştırma izinleri işlemleri kontrol eder; W^X savunma hedefidir ancak her sistemde mutlak kural değildir.

3. Bellek haritası anlık görüntüdür; geçmişteki tüm tahsisleri veya erişimleri göstermez.

## Vaka çalışması

Sentetik bellek sayfası hem yazma hem çalıştırma izni istiyor. Kesin malware demeden gözden geçirilmesi gerektiğini işaretle.

## Güvenli çevrimdışı uygulama

Önce kodun beklenen sonucunu tahmin et. Python 3 ile çalıştır:

```bash
python lab.py
```

Bu dosya sentetik veriler kullanır, `assert` ifadeleriyle çıktıyı kontrol eder ve gerçek Windows ayarlarını değiştirmez.

## İsteğe bağlı Windows gözlemi (salt okunur)

Kendi Windows bilgisayarında PowerShell ile aşağıdaki **salt-okunur** komutu çalıştırabilirsin. Çıktıları ve olası erişim kısıtlarını not et.

```powershell
Get-Process | Select-Object -First 8 Name, Id, VirtualMemorySize64, WorkingSet64
```

Bu komut laboratuvar simülasyonunun yerine geçmez. Bilgiler sistem sürümüne ve mevcut izinlere bağlıdır.

## Görevler

1. Yalnız rezerve ve commit edilmiş bölgeleri ayır.
2. W+X sayfaları bulup yanlış pozitif nedenlerini açıkla.
3. Bellek izni dışında gereken kanıtları öner.

## Bilgi kontrolü

1. Bu gözlem hangi kaynak tarafından üretiliyor?
2. Olayın oluştuğunu ne gösteriyor, neyi **kanıtlamıyor**?
3. Hangi negatif test veya karşı örnek çıkarımını zayıflatır?
4. Gerçek Windows sürümü, koruma ayarları veya toplama zamanı sonucu nasıl değiştirir?

## Güvenlik ve sınırlamalar

Bu bir tersine mühendislik ve savunma eğitimi çalışmasıdır. Gerçek dosya sistemi, Registry, servisler veya güvenlik ayarları değiştirilmez. `lab.py` kodu işletim sistemi mekanizmalarının **öğretici basitleştirmesidir**, Windows kernel veya adli bilişim aracının yerini tutmaz.

## Kaynaklar

- [Microsoft Windows documentation](https://learn.microsoft.com/en-us/windows/win32/)
- [Windows Internals resources](https://learn.microsoft.com/en-us/sysinternals/)
