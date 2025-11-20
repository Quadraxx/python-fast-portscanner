import socket
import sys
import threading
import argparse
from datetime import datetime

# Tek bir portu tarayan eş zamanlı fonksiyon
def tarama_portu(hedef, port):
    """Belirtilen hedefin tek bir portunu tarar ve sonucu yazdırır."""
    try:
        # Soket oluştur (IPv4 ve TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Timeout süresini 0.1 saniyede tutarak hız sağlıyoruz
        s.settimeout(0.1) 
        
        # connect_ex, bağlantı başarılı olursa 0 (sıfır) döndürür
        sonuc = s.connect_ex((hedef, port))  
        
        if sonuc == 0:
            # Bağlantı başarılı = Port açık. Servis adını bulmaya çalışalım.
            try:
                # Servis adını al
                servis_adi = socket.getservbyport(port, 'tcp')
            except OSError:
                servis_adi = "Bilinmiyor"
            
            # Açık port ve servis adını ekrana yazdır
            print(f"Port {port:<5} -> AÇIK ({servis_adi})")
            
        s.close()
    except:
        # Hata durumunda (örneğin soket oluşturulamaması) sessizce geçeriz
        pass

# Argümanları Ayrıştırma Fonksiyonu
def argumanlari_al():
    """Komut satırı argümanlarını argparse ile işler."""
    # Programın nasıl kullanılacağını tanımlayan bir araç oluştur
    parser = argparse.ArgumentParser(
        description="Çok İş Parçacıklı Port Tarayıcı. Hız için eş zamanlı tarama yapar.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Hedef IP veya alan adı argümanı (zorunlu)
    parser.add_argument("hedef", help="Taranacak hedef IP adresi veya alan adı (Örn: google.com).")
    
    # Port aralığı argümanı (isteğe bağlı, varsayılan 1-100)
    parser.add_argument("-p", "--ports", default="1-100", 
                        help="Taranacak port aralığı (Örn: 1-100 veya 80-5000). Varsayılan: 1-100")
    
    args = parser.parse_args()
    return args

# Ana Tarama Başlatma Fonksiyonu
def tarama_baslat(hedef, port_araligi):
    """Çoklu iş parçacığı kullanarak tarama işlemini yönetir."""
    
    # Port aralığını ayrıştır
    try:
        if "-" in port_araligi:
            baslangic, bitis = map(int, port_araligi.split('-'))
        else:
            tek_port = int(port_araligi)
            baslangic, bitis = tek_port, tek_port
    except ValueError:
        print("\nHata: Geçersiz port aralığı formatı. Örnek: 1-100 veya 80.")
        sys.exit()

    print("-" * 50)
    print("Hedef taranıyor:", hedef)
    print(f"Port Aralığı: {baslangic} - {bitis}")
    print("Başlama zamanı:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-" * 50)
    
    threads = []
    
    # Çoklu İş Parçacığı ile tarama
    for port in range(baslangic, bitis + 1):
        # Her port için yeni bir thread oluştur ve başlat
        thread = threading.Thread(target=tarama_portu, args=(hedef, port))
        threads.append(thread)
        thread.start()
    
    # Tüm thread'lerin (port taramalarının) bitmesini bekle
    for thread in threads:
        thread.join()

# Ana Fonksiyon
if __name__ == "__main__":
    try:
        args = argumanlari_al()
        
        # Alan adını IP'ye çevir
        hedef_ip = socket.gethostbyname(args.hedef)
        
        tarama_baslat(hedef_ip, args.ports)
        
        print("-" * 50)
        print("Tarama tamamlandı.")

    except KeyboardInterrupt:
        print("\nTarama kullanıcı tarafından sonlandırıldı.")
        sys.exit()
    except socket.gaierror:
        print("\nHata: Hedef adı çözümlenemedi (IP/Domain hatası).")
        sys.exit()
    except Exception as e:
        print(f"\nBeklenmedik bir hata oluştu: {e}")
        sys.exit()