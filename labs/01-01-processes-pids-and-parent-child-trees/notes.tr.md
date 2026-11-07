# Gün 01 — Windows Süreçleri, PID ve Ebeveyn-Çocuk İlişkileri

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Amaç ve bağlam

Process (süreç), adres alanı, thread'ler ve işletim sisteminin yönettiği kaynaklarla çalışan bir yürütme birimidir. Süreç ağacı bağlam sağlar; ebeveyn ilişkisi tek başına kötücül davranış kanıtı değildir.

## Temel teknik kavramlar

1. PID, belirli anda süreci tanımlar; süreç sonlandıktan sonra aynı sayı yeniden kullanılabilir.

2. Ebeveyn süreç, veri toplama anından önce kapanmış olabilir. Eksik parent normal olabilir; zaman damgası ve ek tanımlayıcılar ilişkilendirmeyi güçlendirir.

3. Süreç ağacı kısmi görünüm sağlar. Komut satırı, dosya yolu, erişim token'ı ve imza bağımsız olarak doğrulanmalıdır.

## Vaka çalışması

Sentetik yardımcı sürecin ebeveyni kayıtta yok. Bunu zararlı olarak etiketlemeden eksik bağı raporla.

## Güvenli çevrimdışı uygulama

Önce kodun beklenen sonucunu tahmin et. Python 3 ile çalıştır:

```bash
python lab.py
```

Bu dosya sentetik veriler kullanır, `assert` ifadeleriyle çıktıyı kontrol eder ve gerçek Windows ayarlarını değiştirmez.

## İsteğe bağlı Windows gözlemi (salt okunur)

Kendi Windows bilgisayarında PowerShell ile aşağıdaki **salt-okunur** komutu çalıştırabilirsin. Çıktıları ve olası erişim kısıtlarını not et.

```powershell
Get-CimInstance Win32_Process | Select-Object -First 8 ProcessId, ParentProcessId, Name
```

Bu komut laboratuvar simülasyonunun yerine geçmez. Bilgiler sistem sürümüne ve mevcut izinlere bağlıdır.

## Görevler

1. Süreç ağacını çıkar ve ebeveyni eksik kaydı bul.
2. Bir ebeveyn değerini değiştirip sonucu açıkla.
3. PID tekrar kullanımı ve başlangıç saatinin rolünü tartış.

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
