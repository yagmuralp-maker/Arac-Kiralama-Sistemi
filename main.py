from tasitlar import Araba
from isletme import KiralamaSistemi

def main():
    sistem = KiralamaSistemi()
    
    # Örnek Araçlar
    sistem.arac_ekle(Araba("34 ABC 123", "Toyota", "Corolla", 2022, 1500))
    sistem.arac_ekle(Araba("06 XYZ 789", "Honda", "Civic", 2023, 1800))

    while True:
        print("\n--- ARAÇ KİRALAMA OTOMASYONU ---")
        print("1. Araçları Listele")
        print("2. Araç Kirala")
        print("3. Çıkış")
        
        secim = input("İşlem seçin (1-3): ")

        if secim == "1":
            sistem.araclari_goster()
        elif secim == "2":
            plaka = input("Plaka girin: ")
            gun = int(input("Gün sayısı: "))
            sistem.arac_kirala(plaka, gun)
        elif secim == "3":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()