# Windows Internals Labs

[🇬🇧 English](README.md) · [🇹🇷 Türkçe](README.tr.md)

Windows'un iç yapısını sıfırdan tanımak için hazırlanan **14 günlük iki dilli uygulamalı eğitim serisi**. Süreç, thread, PE, sanal bellek, Registry, erişim kontrolü, Event Log ve ETW/Sysmon kavramlarıyla ilerler.

## Dersler

| Gün | Konu | Notlar | Pratik |
| --- | --- | --- | --- |
| 01 | Windows Süreçleri, PID ve Ebeveyn-Çocuk İlişkileri | [Türkçe](labs/01-processes-pids-and-parent-child-trees/notes.tr.md) · [English](labs/01-processes-pids-and-parent-child-trees/notes.md) | [lab.py](labs/01-processes-pids-and-parent-child-trees/lab.py) |
| 02 | Thread, Handle ve Nesne Yaşam Süresi | [Türkçe](labs/02-threads-handles-and-lifetime/notes.tr.md) · [English](labs/02-threads-handles-and-lifetime/notes.md) | [lab.py](labs/02-threads-handles-and-lifetime/lab.py) |
| 03 | PE Başlıkları, Makine Türleri ve Güvenli Ayrıştırma | [Türkçe](labs/03-pe-headers-and-machine-types/notes.tr.md) · [English](labs/03-pe-headers-and-machine-types/notes.md) | [lab.py](labs/03-pe-headers-and-machine-types/lab.py) |
| 04 | Sanal Bellek Bölgeleri, Sayfalar ve Korumalar | [Türkçe](labs/04-virtual-memory-regions-and-page-protection/notes.tr.md) · [English](labs/04-virtual-memory-regions-and-page-protection/notes.md) | [lab.py](labs/04-virtual-memory-regions-and-page-protection/lab.py) |
| 05 | DLL Yükleme, Arama Yolları ve Güven Sınırları | [Türkçe](labs/05-dll-loading-paths-and-search-boundaries/notes.tr.md) · [English](labs/05-dll-loading-paths-and-search-boundaries/notes.md) | [lab.py](labs/05-dll-loading-paths-and-search-boundaries/lab.py) |
| 06 | Registry Hive, Anahtar ve Değer Bağlamı | [Türkçe](labs/06-registry-hives-keys-and-value-context/notes.tr.md) · [English](labs/06-registry-hives-keys-and-value-context/notes.md) | [lab.py](labs/06-registry-hives-keys-and-value-context/lab.py) |
| 07 | NTFS Dosya Metadatası ve Zaman Damgası Belirsizliği | [Türkçe](labs/07-ntfs-file-metadata-and-time-uncertainty/notes.tr.md) · [English](labs/07-ntfs-file-metadata-and-time-uncertainty/notes.md) | [lab.py](labs/07-ntfs-file-metadata-and-time-uncertainty/lab.py) |
| 08 | Erişim Tokenları, SID ve DACL Değerlendirmesi | [Türkçe](labs/08-access-tokens-sids-and-dacl-models/notes.tr.md) · [English](labs/08-access-tokens-sids-and-dacl-models/notes.md) | [lab.py](labs/08-access-tokens-sids-and-dacl-models/lab.py) |
| 09 | Windows Olay Logları, Sağlayıcılar ve Event ID | [Türkçe](labs/09-windows-event-logs-and-provider-context/notes.tr.md) · [English](labs/09-windows-event-logs-and-provider-context/notes.md) | [lab.py](labs/09-windows-event-logs-and-provider-context/lab.py) |
| 10 | Windows Servisleri, Zamanlanmış Görevler ve Başlangıç | [Türkçe](labs/10-windows-services-and-scheduled-tasks/notes.tr.md) · [English](labs/10-windows-services-and-scheduled-tasks/notes.md) | [lab.py](labs/10-windows-services-and-scheduled-tasks/lab.py) |
| 11 | ETW, Sysmon ve Süreç Olayı Korelasyonu | [Türkçe](labs/11-etw-sysmon-and-process-event-correlation/notes.tr.md) · [English](labs/11-etw-sysmon-and-process-event-correlation/notes.md) | [lab.py](labs/11-etw-sysmon-and-process-event-correlation/lab.py) |
| 12 | Windows Internals Delil Yeniden Yapılandırma Bitirme Çalışması | [Türkçe](labs/12-windows-internals-evidence-capstone/notes.tr.md) · [English](labs/12-windows-internals-evidence-capstone/notes.md) | [lab.py](labs/12-windows-internals-evidence-capstone/lab.py) |
| 13 | Windows Handle Erişim Hakları ve Delil Bağlamı | [Türkçe](labs/13-windows-handle-access-rights-and-evidence/notes.tr.md) · [English](labs/13-windows-handle-access-rights-and-evidence/notes.md) | [lab.py](labs/13-windows-handle-access-rights-and-evidence/lab.py) |
| 14 | Windows Dosya Paylaşım Modları ve Handle Uyumluluğu | [Türkçe](labs/14-file-sharing-modes-and-handle-compatibility/notes.tr.md) · [English](labs/14-file-sharing-modes-and-handle-compatibility/notes.md) | [lab.py](labs/14-file-sharing-modes-and-handle-compatibility/lab.py) |

## Nasıl çalışılır?

1. Konuyu Türkçe veya İngilizce notlardan öğren.
2. Örnek kodu inceleyerek sonucu önceden tahmin et.
3. `python lab.py` çalıştır; `assert` denetimlerini gör. Tüm labları sınamak için kök dizinde `python test_all.py` çalıştır.
4. Yalnızca kendi Windows bilgisayarında verilen salt-okunur PowerShell komutunu dene (isteğe bağlı).
5. Bir yanlış pozitif ve bir eksik delil senaryosu yaz.

## Gereksinimler

- Python 3.10+ (standart kütüphane, çoğu lab platform bağımsız)
- İsteğe bağlı: Windows 10/11 + PowerShell 5.1 veya üzeri (salt okunur komutlar).
- Yönetici yetkisi gerektirmeyen örneklerle başla. Bazı Windows logları ve alanları erişim kısıtlı olabilir.

## Dizin yapısı

```text
Windows-Internals-Labs/
├── README.md
├── README.tr.md
├── resources.md
└── labs/
    ├── 01-processes-pids-and-parent-child-trees/
    │   ├── notes.md
    │   ├── notes.tr.md
    │   └── lab.py
    └── ... (toplam 13 gün, aynı düzen)
```

## Sınırlar ve güvenlik

Örnekler gerçek bellek okuması, DLL yüklemesi, Registry değişikliği veya log temizliği yapmaz. Python modelleri gerçek çekirdek davranışıyla birebir eş değildir. Kaynak sistemleri ve dosyaları yalnızca açık izinle inceleyin.

## Devam yolu

Temel 14 günün ardından WinDbg, PE loader ayrıntıları, bellek adli bilişimi, Win32 API ve kontrollü ETW deneylerine geçilebilir.

