# Gün 09 — Windows Olay Logları, Sağlayıcılar ve Event ID

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Amaç ve bağlam

Windows olay kayıtları farklı sağlayıcı ve kanallardan üretilir. Event ID ancak sağlayıcı, kanal, sürüm ve kayıt alanlarıyla birlikte anlam kazanır.

## Temel teknik kavramlar

1. 4624 (başarılı giriş) ve 4688 (süreç oluşturma) gibi Security olaylarının görünürlüğü audit politikası ve olay sürümüne bağlıdır.

2. Sistemler arası sıralama için zaman normalizasyonu, eksik kayıt, log devri ve toplama gecikmesi dikkate alınır.

3. Giriş olayı kimlik doğrulama sonucunu kaydeder; tek başına gerçek insan niyetini kanıtlamaz.

## Vaka çalışması

İki sentetik kayıtta Event ID aynı ancak provider farklı. Aynı olayı temsil ettiklerini varsayma.

## Güvenli çevrimdışı uygulama

Önce kodun beklenen sonucunu tahmin et. Python 3 ile çalıştır:

```bash
python lab.py
```

Bu dosya sentetik veriler kullanır, `assert` ifadeleriyle çıktıyı kontrol eder ve gerçek Windows ayarlarını değiştirmez.

## İsteğe bağlı Windows gözlemi (salt okunur)

Kendi Windows bilgisayarında PowerShell ile aşağıdaki **salt-okunur** komutu çalıştırabilirsin. Çıktıları ve olası erişim kısıtlarını not et.

```powershell
Get-WinEvent -ListLog * | Select-Object -First 8 LogName, RecordCount
```

Bu komut laboratuvar simülasyonunun yerine geçmez. Bilgiler sistem sürümüne ve mevcut izinlere bağlıdır.

## Görevler

1. Olayları yalnız Event ID değil (provider, event_id) ile grupla.
2. Eksik timestamp içeren negatif örnek ekle.
3. Gerçek 4688 çalışmasında audit politikasının rolünü açıkla.

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
