# Gün 03 — PE Başlıkları, Makine Türleri ve Güvenli Ayrıştırma

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Amaç ve bağlam

Windows Portable Executable (PE) biçimi DOS başlığı, PE imzası ve COFF/optional header alanları içerir. Güvenilmeyen baytları okumadan önce ofsetler ve sınırlar kontrol edilmelidir.

## Temel teknik kavramlar

1. DOS 'MZ' imzası ofset 0'dadır. 0x3c adresindeki little-endian e_lfanew alanı tipik PE dosyasında PE imzasını gösterir.

2. PE imzası 'PE' ve iki NUL baytından oluşur. Ardından gelen COFF başlığında makine türü bilgisi vardır.

3. Tek imza, dosyanın geçerli, çalıştırılabilir veya zararsız olduğunu kanıtlamaz. Gerçek ayrıştırıcı tüm yapı ilişkilerini ve boyutları denetlemelidir.

## Vaka çalışması

Bir örnekte e_lfanew dosyanın dışına işaret ediyor. Çökmeden reddet.

## Güvenli çevrimdışı uygulama

Önce kodun beklenen sonucunu tahmin et. Python 3 ile çalıştır:

```bash
python lab.py
```

Bu dosya sentetik veriler kullanır, `assert` ifadeleriyle çıktıyı kontrol eder ve gerçek Windows ayarlarını değiştirmez.

## İsteğe bağlı Windows gözlemi (salt okunur)

Kendi Windows bilgisayarında PowerShell ile aşağıdaki **salt-okunur** komutu çalıştırabilirsin. Çıktıları ve olası erişim kısıtlarını not et.

```powershell
Get-Item $env:SystemRoot\System32\notepad.exe | Select-Object Name, Length, LastWriteTime
```

Bu komut laboratuvar simülasyonunun yerine geçmez. Bilgiler sistem sürümüne ve mevcut izinlere bağlıdır.

## Görevler

1. Geçerli ve kesilmiş sentetik tampon testlerini çalıştır.
2. Yanlış MZ imzası için negatif test ekle.
3. Bu örneğin hangi PE yapılarını atladığını listele.

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
