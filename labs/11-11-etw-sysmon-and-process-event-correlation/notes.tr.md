# Gün 11 — ETW, Sysmon ve Süreç Olayı Korelasyonu

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Amaç ve bağlam

ETW ve Sysmon gibi kaynaklar süreç ve imaj etkinliği hakkında bağlam sağlar. Korelasyon yalnız süreç adına değil, kimliklere ve zaman penceresine dayanmalıdır.

## Temel teknik kavramlar

1. Sysmon Event ID 1 uygun yapılandırmada süreç oluşturmayı kaydedebilir; kayıt görünürlüğü kurulum ve toplama ayarına bağlıdır.

2. Process GUID, PID'ye göre bazı korelasyonlarda daha sağlam olabilir; yine de kaynağın şeması ve tanımlayıcının kökeni doğrulanır.

3. Sadece ad eşleşmesi zayıf kanıttır. Mümkünse provider, olay kimliği, oluşturma saati, dosya yolu ve ebeveyn bilgisi birlikte kullanılır.

## Vaka çalışması

İki farklı süreç aynı adı taşıyor ancak GUID'leri farklı. Etkinlikleri doğru süreçle eşleştir.

## Güvenli çevrimdışı uygulama

Önce kodun beklenen sonucunu tahmin et. Python 3 ile çalıştır:

```bash
python lab.py
```

Bu dosya sentetik veriler kullanır, `assert` ifadeleriyle çıktıyı kontrol eder ve gerçek Windows ayarlarını değiştirmez.

## İsteğe bağlı Windows gözlemi (salt okunur)

Kendi Windows bilgisayarında PowerShell ile aşağıdaki **salt-okunur** komutu çalıştırabilirsin. Çıktıları ve olası erişim kısıtlarını not et.

```powershell
Get-Service Sysmon64,Sysmon -ErrorAction SilentlyContinue | Select-Object Name, Status
```

Bu komut laboratuvar simülasyonunun yerine geçmez. Bilgiler sistem sürümüne ve mevcut izinlere bağlıdır.

## Görevler

1. Kayıtları sentetik Process GUID ile birleştir.
2. Sadece image adına göre eşleştirmenin neden belirsiz olduğunu göster.
3. Gerçek incelemede eksik telemetrinin etkisini tartış.

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
