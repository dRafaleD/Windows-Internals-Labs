# Gün 02 — Thread, Handle ve Nesne Yaşam Süresi

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Amaç ve bağlam

Thread, bir süreç içinde komutları çalıştıran yürütme akışıdır. Handle, çekirdek tarafından yönetilen nesneye süreç bağlamında verilen referanstır. Handle sayısı küresel ve değişmez kimlik değildir.

## Temel teknik kavramlar

1. Bir süreçte adres alanını paylaşan birden fazla thread bulunabilir; her thread'in yürütme bağlamı ve yığını ayrıdır.

2. Handle kapatmak sürecin referansını bırakır; nesnenin yaşamı diğer referanslara ve işletim sistemi kurallarına bağlıdır.

3. Handle değerleri yeniden kullanılabilir. İncelemede süreç, nesne türü, erişim izinleri ve toplama zamanı kaydedilmelidir.

## Vaka çalışması

İki süreçte aynı sayısal handle değeri farklı sentetik nesnelere işaret ediyor. Bunları aynı nesne sanmadan ayır.

## Güvenli çevrimdışı uygulama

Önce kodun beklenen sonucunu tahmin et. Python 3 ile çalıştır:

```bash
python lab.py
```

Bu dosya sentetik veriler kullanır, `assert` ifadeleriyle çıktıyı kontrol eder ve gerçek Windows ayarlarını değiştirmez.

## İsteğe bağlı Windows gözlemi (salt okunur)

Kendi Windows bilgisayarında PowerShell ile aşağıdaki **salt-okunur** komutu çalıştırabilirsin. Çıktıları ve olası erişim kısıtlarını not et.

```powershell
Get-Process | Select-Object -First 8 Name, Id, Threads, HandleCount
```

Bu komut laboratuvar simülasyonunun yerine geçmez. Bilgiler sistem sürümüne ve mevcut izinlere bağlıdır.

## Görevler

1. (süreç, değer) çiftlerini kullanarak handle'ları ayır.
2. Aynı sayı ile kapat/aç işlemini simüle et.
3. Canlı handle listesinin neden eksik kalabileceğini anlat.

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
