# Gün 10 — Windows Servisleri, Zamanlanmış Görevler ve Başlangıç

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Amaç ve bağlam

Windows servisleri ve zamanlanmış görevler meşru arka plan çalışmaları için kullanılır. Yapılandırmaları, tetikleyicileri ve çalıştırma hesapları güvenlik incelemesinde önemlidir.

## Temel teknik kavramlar

1. Servis yapılandırması nasıl çalışabileceğini tanımlar; incelenen zaman aralığında kesin çalıştığını göstermez.

2. Zamanlanmış görevler zaman, olay veya kullanıcı eylemiyle tetiklenebilir. Tetikleyici, eylem, çalıştırma hesabı ve geçmiş birlikte incelenir.

3. Yeni başlangıç girdisi araştırma işaretidir; tek başına malware kanıtı değildir. Temel durum (baseline) ve yetkili yapılandırma verileriyle karşılaştır.

## Vaka çalışması

Sentetik zamanlanmış görevin eylemi geçici klasöre işaret ediyor. Çalıştırmadan yapılandırmayı incelemeye al.

## Güvenli çevrimdışı uygulama

Önce kodun beklenen sonucunu tahmin et. Python 3 ile çalıştır:

```bash
python lab.py
```

Bu dosya sentetik veriler kullanır, `assert` ifadeleriyle çıktıyı kontrol eder ve gerçek Windows ayarlarını değiştirmez.

## İsteğe bağlı Windows gözlemi (salt okunur)

Kendi Windows bilgisayarında PowerShell ile aşağıdaki **salt-okunur** komutu çalıştırabilirsin. Çıktıları ve olası erişim kısıtlarını not et.

```powershell
Get-Service | Select-Object -First 6 Name, Status, StartType; Get-ScheduledTask | Select-Object -First 6 TaskName, State
```

Bu komut laboratuvar simülasyonunun yerine geçmez. Bilgiler sistem sürümüne ve mevcut izinlere bağlıdır.

## Görevler

1. Sentetik önceki ve mevcut görev kayıtlarını karşılaştır.
2. Görev varlığı ile yürütülmesi farkını açıkla.
3. Gerekli log ve ek kanıtları yaz.

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
