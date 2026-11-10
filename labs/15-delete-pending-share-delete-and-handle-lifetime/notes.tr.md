# Gün 15 — Delete-Pending, FILE_SHARE_DELETE ve Handle Yaşam Süresi

[English](notes.md) · [Türkçe](notes.tr.md) · [Güvenli Python uygulaması](lab.py)

## Ne öğreneceğiz?
14. günde **istenen erişim hakkı (desired access)** ile **paylaşım modu (share mode)** arasındaki farkı incelemiştik. Şimdi Windows'ta bir dosya silinmek istendiğinde açık handle'ların neden önemli olduğunu ve **delete-pending** durumunun ne anlama geldiğini öğreniyoruz.

Önemli ayrım: Bir dosyayı açmak, o dosyayı silme hakkına sahip olmak veya silme işleminin tamamlandığı anlamına gelmez.

## Birbirinden farklı üç kontrol
1. **Erişim yetkisi:** Silme isteğini yapan süreç/kullanıcı gerekli haklara sahip mi? Gerçekte access token, erişim denetimleri ve DELETE hakkı gibi ayrıntılar vardır. Bizim örnekte `caller_authorized` yalnızca bunu temsil eden basit bir boole değerdir.
2. **Paylaşım uyumu:** Açık handle, `FILE_SHARE_DELETE` paylaşımını belirtmediyse yeni silmeyle ilişkili işlem engellenebilir. **FILE_SHARE_DELETE, silme yetkisi vermez**; başka handle/işlemlerle uyumluluğu ifade eder.
3. **Handle yaşam süresi:** Basitleştirilmiş geleneksel modelimizde silme isteği kabul edilince dosya `delete_pending` olur. Açık handle'lar kapanınca silme tamamlanır. Bu modelde pending durumundaki dosyaya yeni handle açılması reddedilir.

**Gerçekte Windows davranışı daha karmaşıktır.** Kullanılan API, dosya sistemi, disposition bayrakları ve POSIX tarzı silme seçenekleri sonucu değiştirebilir. Bu Python kodu çekirdeğin birebir kopyası değildir.

## Adım adım lab
Bu klasörde:
```bash
python lab.py
```
Kod hiçbir gerçek dosyaya dokunmaz; yalnızca hayalî handle nesneleriyle çalışır:
- `FILE_SHARE_DELETE` kullanmayan okuyucu varken silme isteği paylaşım nedeniyle reddedilir.
- Handle'lar DELETE paylaşımı verse bile **yetkisiz** silme isteği reddedilir.
- Yetkili istek kabul edilince `delete_pending` olur; bu modelde yeni açma isteği engellenir.
- İlk handle kapanınca silme bitmez, son handle kapatılınca model dosyayı `deleted` kabul eder.

`assert` satırları beklenen durumları test eder. Win32 çağrısı, dosya silme, Registry değişikliği ya da ağ erişimi yapılmaz.

## Pratik sorular
1. Neden `FILE_SHARE_DELETE` ile DELETE erişim hakkı aynı şey değildir?
2. Bir reddin paylaşım uyumsuzluğundan mı, erişim yetkisinden mi kaynaklandığını nasıl ayırırsın?
3. `delete-pending` gözlemi, dosya içeriğinin fiziksel olarak silindiğini neden kanıtlamaz?
4. DELETE paylaşımı vermeyen üçüncü handle ekle; sonucu çalıştırmadan tahmin et.
5. Gerçek bir olay incelemesinde process ID, handle, dosya yolu, erişim maskesi ve zaman damgası nasıl raporlanır?
6. Yalnızca bir handle açılışından dosyanın gerçekten yazıldığı sonucunu çıkarabilir misin?

## Kaynak ve sınırlar
[Microsoft CreateFileW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew) ve [File Sharing](https://learn.microsoft.com/en-us/windows/win32/fileio/file-sharing) belgeleri gerçek sistem davranışını incelerken temel kaynaklardır. Bu lab sadece **yetki, paylaşım ve yaşam süresi** kavramlarını öğretir; gerçek Windows üzerinde hiçbir değişiklik yapmaz.
