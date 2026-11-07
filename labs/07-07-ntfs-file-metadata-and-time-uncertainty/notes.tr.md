# Gün 07 — NTFS Dosya Metadatası ve Zaman Damgası Belirsizliği

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Amaç ve bağlam

NTFS, dosya adından fazlasını tutan metadata yapıları içerir. Zaman damgaları zaman çizelgesinde yardımcıdır; ancak kopyalama, yedekleme, saat ayarı ve dosya sistemi davranışı yorumu zorlaştırır.

## Temel teknik kavramlar

1. Oluşturma, içerik değişimi, erişim ve metadata değişim zamanları farklı kavramlardır; her işletim sistemi ve API aynı alanı sunmaz.

2. Python'un stat alanları tüm NTFS kanıtlarını göstermez; MFT kaydı, USN günlüğü veya ADS gibi veriler ayrıca incelenir.

3. Orijinalleri koru, saat dilimlerini normalleştir ve toplama araçlarını kaydet. Tek anormal tarihten timestomping sonucu çıkarma.

## Vaka çalışması

Zararsız bir eğitim dosyası oluşturulup değiştirilir. Taşınabilir API'nin gerçekten gösterdiği alanları kaydet.

## Güvenli çevrimdışı uygulama

Önce kodun beklenen sonucunu tahmin et. Python 3 ile çalıştır:

```bash
python lab.py
```

Bu dosya sentetik veriler kullanır, `assert` ifadeleriyle çıktıyı kontrol eder ve gerçek Windows ayarlarını değiştirmez.

## İsteğe bağlı Windows gözlemi (salt okunur)

Kendi Windows bilgisayarında PowerShell ile aşağıdaki **salt-okunur** komutu çalıştırabilirsin. Çıktıları ve olası erişim kısıtlarını not et.

```powershell
Get-Item $env:TEMP | Select-Object FullName, CreationTimeUtc, LastWriteTimeUtc, LastAccessTimeUtc
```

Bu komut laboratuvar simülasyonunun yerine geçmez. Bilgiler sistem sürümüne ve mevcut izinlere bağlıdır.

## Görevler

1. Geçici dosyanın değişiklik öncesi/sonrası boyut ve mtime değerini incele.
2. st_ctime alanının Windows ile Unix'teki farkını anlat.
3. Bu örneğin toplamadığı NTFS artefaktlarını say.

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
