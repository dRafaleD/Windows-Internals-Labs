# Gün 18 — File ID Yeniden Kullanımı ve Handle Kanıtı

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 17. günden devam
Hard link sayesinde iki yolun aynı dosyayı gösterebileceğini gördük. Ama eski nesne tamamen ortadan kalktıktan sonra **sayısal dosya kimliği başka nesne için yeniden kullanılabilir**. Bu nedenle farklı zamanlarda aynı file ID görülmesi, mutlaka aynı dosya olduğu anlamına gelmez.

Modelimizde 42 numaralı dosyanın `a.txt` ve `b.txt` adlı iki bağlantısı var. İki ad kaldırılsa bile açık **handle** nesneyi modelde yaşatıyor. Handle kapatılınca kimlik yeniden kullanılabiliyor; yeni nesne farklı bir **epoch (oyuncak nesil işareti)** alıyor.

Bu epoch, NTFS'in gerçek ve garanti edilen bir alanı **değildir**. Gerçek incelemede disk birimi, kayıt sırası, zaman, dosya sistemi ve USN gibi izler ayrıca değerlendirilmelidir.

## Çalıştır
~~~bash
python3 labs/18-file-id-reuse-generations-and-handle-evidence/lab.py
python3 test_all.py
~~~

## Sorular
Aynı file ID neden farklı zamanlarda farklı dosyaları temsil edebilir? Açık handle nesnenin ömrünü nasıl etkiler? Adli analizde tek başına dosya yolu neden yetersizdir?

## Sınırlar
Python içi simülasyondur; gerçek NTFS, dosya işlemi veya Windows API çağrısı kullanılmaz.
