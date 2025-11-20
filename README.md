# ⚡️ Python Hızlı Port Tarayıcı (Port Scanner)

### Proje Sahibi: Hüseyin Akın

Basit, hızlı ve **çok iş parçacıklı (Multi-threaded)** bir TCP port tarama aracıdır. Python'ın standart kütüphanelerini kullanarak yazılmıştır ve sunucular, modemler veya ağ cihazları üzerindeki açık portları tespit etmek için idealdir.

---

## ✨ Temel Özellikler

* **Ultra Hızlı Tarama:** `threading` kütüphanesi sayesinde portlar eş zamanlı (paralel) olarak taranır, bu da tarama süresini dramatik şekilde kısaltır.
* **Esnek Port Aralığı:** Tek bir port, küçük bir aralık (`1-100`) veya tüm port aralığı (`1-65535`) taranabilir.
* **Servis Tespiti:** Açık bulunan portların yanında, otomatik olarak hangi standart servise ait olduğu (örneğin, `http` veya `ssh`) bilgisi gösterilir.
* **Profesyonel Argüman Yönetimi:** Python `argparse` kütüphanesi ile komut satırı argümanları düzenli ve kolay kullanılır.

---

## 🛠️ Gereksinimler

Bu araç sadece standart Python kütüphanelerini kullandığı için ek bir kurulum gerektirmez.

* **Python:** 3.x sürümü

---

## 🚀 Kullanım Kılavuzu

Programı çalıştırmak için komut satırını (Terminal veya CMD) kullanın.

### 1. Varsayılan Tarama (1-100 Port)

Hedefi belirtmeniz yeterlidir. Varsayılan olarak 1'den 100'e kadar olan portları tarar.

```bash
python port_tarayici.py google.com
