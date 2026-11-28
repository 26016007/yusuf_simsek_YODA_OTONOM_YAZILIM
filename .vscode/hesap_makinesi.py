def topla(a,b):
    return a+b
def cıkarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    if b==0:
        return None
    return a/b
def main():
    
    gecmis = []                     
    while True:
        try:
            x = int(input("Yapmak istediğiniz işlemi seçiniz:\n1. Toplama\n2. Çıkarma\n3. Çarpma\n4. Bölme\n5. Geçmişi Görüntüle\n0. Çıkış\nSeçiminiz: "))               
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı giriniz.")
            continue

        if x == 1:
            a = sayi_al("Birinci sayıyı giriniz: ")
            b = sayi_al("İkinci sayıyı giriniz: ")
            sonuc = topla(a, b)     
            print("Sonuç:", guzel(sonuc))
            gecmis.append(f"{guzel(a)} + {guzel(b)} = {guzel(sonuc)}")  
        elif x == 2:
            a = sayi_al("Birinci sayıyı giriniz: ")
            b = sayi_al("İkinci sayıyı giriniz: ")
            sonuc = cıkarma(a, b)     
            print("Sonuç:", guzel(sonuc))
            gecmis.append(f"{guzel(a)} - {guzel(b)} = {guzel(sonuc)}")
        elif x == 3:
            a = sayi_al("Birinci sayıyı giriniz: ")
            b = sayi_al("İkinci sayıyı giriniz: ")
            sonuc = carpma(a, b)     
            print("Sonuç:", guzel(sonuc))
            gecmis.append(f"{guzel(a)} * {guzel(b)} = {guzel(sonuc)}")
        elif x == 4:
            a = sayi_al("Birinci sayıyı giriniz: ")
            b = sayi_al("İkinci sayıyı giriniz: ")
            sonuc = bolme(a, b)
            if sonuc is None:
                print("Hata: Bir sayıyı sıfıra bölemezsiniz.")
            else:     
                print("Sonuç:",guzel(sonuc))
                gecmis.append(f"{guzel(a)} / {guzel(b)} = {guzel(sonuc)}")
        elif x == 5:
            if not gecmis:
                print("Henüz işlem yapılmadı.")
            else:
                for i, kayit in enumerate(gecmis, 1):
                    print(f"{i}. {kayit}")          
        elif x == 0:
            break 
        elif x not in [0, 1, 2, 3, 4, 5]:
            print("Geçersiz seçim. Lütfen tekrar deneyiniz.")
def sayi_al(mesaj):
    while True:
        try:
            return float(input(mesaj))
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")  
def guzel(x):
    return int(x) if x == int(x) else x                   
main()
