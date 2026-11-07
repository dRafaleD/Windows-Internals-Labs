# Gün 06 — Registry Hive, Anahtar ve Değer Bağlamı

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Amaç ve bağlam

Windows Registry yapılandırma verilerini hiyerarşik tutar. Anahtar konumu, değer tipi ve erişim bağlamı önemlidir; bir değerin varlığı tek başına kalıcılık veya kötü niyet kanıtı değildir.

## Temel teknik kavramlar

1. Yaygın kök hive'lar HKLM ve HKCU'dur; kullanıcıya ve makineye özel yapılandırmalar farklı kapsamdadır.

2. Run/RunOnce değerleri başlangıç incelemesinde önemlidir ancak meşru uygulamalar da bunları kullanır. Yol, imza, değişim zamanı ve yürütme ile ilişkilendir.

3. 32-bit ve 64-bit Windows'ta Registry görünümleri farklı olabilir; tüm yazılımların aynı konumda tutulduğunu varsayma.

## Vaka çalışması

Sentetik başlangıç anahtarında meşru güncelleyici ve bilinmeyen bir yol var. Kesin tehdit etiketi yerine inceleme adayı olarak işaretle.

## Güvenli çevrimdışı uygulama

Önce kodun beklenen sonucunu tahmin et. Python 3 ile çalıştır:

```bash
python lab.py
```

Bu dosya sentetik veriler kullanır, `assert` ifadeleriyle çıktıyı kontrol eder ve gerçek Windows ayarlarını değiştirmez.

## İsteğe bağlı Windows gözlemi (salt okunur)

Kendi Windows bilgisayarında PowerShell ile aşağıdaki **salt-okunur** komutu çalıştırabilirsin. Çıktıları ve olası erişim kısıtlarını not et.

```powershell
Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' -ErrorAction SilentlyContinue
```

Bu komut laboratuvar simülasyonunun yerine geçmez. Bilgiler sistem sürümüne ve mevcut izinlere bağlıdır.

## Görevler

1. Sentetik HKCU ve HKLM kayıtlarını karşılaştır.
2. Meşru başlangıç girdisi ekleyip sonucu yeniden değerlendir.
3. Gerçek yürütmeyi hangi kanıtın gösterebileceğini açıkla.

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
