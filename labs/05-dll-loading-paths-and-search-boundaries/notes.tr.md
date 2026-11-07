# Gün 05 — DLL Yükleme, Arama Yolları ve Güven Sınırları

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Amaç ve bağlam

Programlar DLL kütüphanelerini dinamik yükleyebilir. Belirsiz, göreli veya yalnız ad içeren DLL başvuruları, arama bağlamı ve dosya sistemi izinlerini kritik hâle getirebilir.

## Temel teknik kavramlar

1. Windows DLL arama kuralları kullanılan API, loader ayarı, paket tipi ve sistem korumalarına bağlıdır; tek bir evrensel sıra varsayılmaz.

2. Uygun olduğunda tam yol ve güvenilir uygulama konumları kullan; kütüphane imzası ve güncelleme süreçlerini ayrıca denetle.

3. Yolda DLL bulunması yüklenip çalıştırıldığını kanıtlamaz. Modül yükleme delili gerekir.

## Vaka çalışması

Sentetik uygulama göreli 'example.dll' adını kullanıyor. Simülasyon, isteğin izin verilen mutlak yol içerip içermediğini inceliyor.

## Güvenli çevrimdışı uygulama

Önce kodun beklenen sonucunu tahmin et. Python 3 ile çalıştır:

```bash
python lab.py
```

Bu dosya sentetik veriler kullanır, `assert` ifadeleriyle çıktıyı kontrol eder ve gerçek Windows ayarlarını değiştirmez.

## İsteğe bağlı Windows gözlemi (salt okunur)

Kendi Windows bilgisayarında PowerShell ile aşağıdaki **salt-okunur** komutu çalıştırabilirsin. Çıktıları ve olası erişim kısıtlarını not et.

```powershell
Get-Process -Id $PID | Select-Object Name, Id, Path
```

Bu komut laboratuvar simülasyonunun yerine geçmez. Bilgiler sistem sürümüne ve mevcut izinlere bağlıdır.

## Görevler

1. Mutlak ve göreli DLL adlarını karşılaştır.
2. Dosyanın varlığıyla modülün yüklenmesinin farkını anlat.
3. Gerçek Windows incelemesinde gerekli kaynakları ve telemetriyi yaz.

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
