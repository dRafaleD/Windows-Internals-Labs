# Gün 08 — Erişim Tokenları, SID ve DACL Değerlendirmesi

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Amaç ve bağlam

Windows kimlik ve kaynak izinlerini SID, erişim token'ı ve erişim kontrol listeleri (ACL) ile modeller. Erişim kontrolü sırası ve kalıtım incelikli yorumlanmalıdır.

## Temel teknik kavramlar

1. Token, kullanıcı/grup kimliği ve ayrıcalık bilgileri içerir. Bir gruba üye olmak tüm işlemlerde otomatik tam yetki vermeyebilir.

2. DACL, ACE girişleri içerir; gerçek Windows erişim denetimi sıra, nesne türü, kalıtım ve token ayrıntılarına bağlıdır.

3. Bu labdaki açık-ret-öncelikli model eğitim amaçlıdır; Windows güvenlik çekirdeğinin tam uygulaması değildir.

## Vaka çalışması

Misafir kullanıcı Readers grubuna ait fakat ayrıca açık ret girdisiyle eşleşiyor. Basitleştirilmiş politikanın okumayı reddettiğini doğrula.

## Güvenli çevrimdışı uygulama

Önce kodun beklenen sonucunu tahmin et. Python 3 ile çalıştır:

```bash
python lab.py
```

Bu dosya sentetik veriler kullanır, `assert` ifadeleriyle çıktıyı kontrol eder ve gerçek Windows ayarlarını değiştirmez.

## İsteğe bağlı Windows gözlemi (salt okunur)

Kendi Windows bilgisayarında PowerShell ile aşağıdaki **salt-okunur** komutu çalıştırabilirsin. Çıktıları ve olası erişim kısıtlarını not et.

```powershell
Get-Acl $env:TEMP | Select-Object -ExpandProperty Access | Select-Object -First 8
```

Bu komut laboratuvar simülasyonunun yerine geçmez. Bilgiler sistem sürümüne ve mevcut izinlere bağlıdır.

## Görevler

1. Misafir ve normal okuyucuyu değerlendir.
2. Bir ACE değerini değiştirip etkin izni gözlemle.
3. Kalıtım ve ACE sıralamasının gerçek modeli neden karmaşıklaştırdığını açıkla.

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
