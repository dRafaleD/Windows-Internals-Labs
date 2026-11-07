# Gün 12 — Windows Internals Delil Yeniden Yapılandırma Bitirme Çalışması

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Amaç ve bağlam

Bağımsız sentetik süreç, dosya ve olay kayıtlarından Windows benzeri etkinlik dizisi oluştur. Doğrudan gözlem ile aktör atfını ve niyet yorumunu ayır.

## Temel teknik kavramlar

1. Kaynak ID, provider ve kararlı ilişkilendirme anahtarlarıyla UTC zaman çizelgesi kur. Özgün kayıtları koru.

2. Dosyanın bir süreç başladıktan sonra ortaya çıkması, dosyayı o sürecin oluşturduğunu tek başına kanıtlamaz. Bağımsız dosya işlemi kaydı gerekir.

3. Eksik log, zaman çözünürlüğü ve çelişkileri açıkça yaz. Delil yetersizse 'sonuçsuz' değerlendirme uygun olabilir.

## Vaka çalışması

Sentetik süreç oluşturuluyor ve bir dakika sonra dosya olayı görülüyor. Process GUID ile ilişkilendir; ancak süreci kimin başlattığı konusunda belirsizliği koru.

## Güvenli çevrimdışı uygulama

Önce kodun beklenen sonucunu tahmin et. Python 3 ile çalıştır:

```bash
python lab.py
```

Bu dosya sentetik veriler kullanır, `assert` ifadeleriyle çıktıyı kontrol eder ve gerçek Windows ayarlarını değiştirmez.

## İsteğe bağlı Windows gözlemi (salt okunur)

Kendi Windows bilgisayarında PowerShell ile aşağıdaki **salt-okunur** komutu çalıştırabilirsin. Çıktıları ve olası erişim kısıtlarını not et.

```powershell
Get-Date -Format o; Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, BuildNumber
```

Bu komut laboratuvar simülasyonunun yerine geçmez. Bilgiler sistem sürümüne ve mevcut izinlere bağlıdır.

## Görevler

1. Mini incelemeyi çalıştırıp kaynakları korunmuş zaman çizelgesini kontrol et.
2. Gözlem, hipotez, eksik kanıt ve güven düzeyini içeren kısa rapor yaz.
3. Aktör atfından önce hangi ek zararsız testlere ihtiyaç olduğunu belirt.

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
