import random
def sayiuret():
   return random.randint(1,100)
def sayitahminal():
   while True:
       try:
           tahmin = int(input("1 ile 100 arasında bir sayı tahmin ediniz: "))
           return tahmin
       except ValueError:
              print("Lütfen geçerli bir sayı giriniz.")
def oyna():
    hedef=sayiuret()
    for deneme in range (1,11):
        tahmin=sayitahminal()
        if tahmin<hedef:
            print("Daha büyük bir sayı tahmin ediniz.")
        elif tahmin>hedef:
            print("Daha küçük bir sayı tahmin ediniz.")
        else:
             print(f"Tebrikler! Doğru sayıyı buldunuz. {deneme}. denemede")
             return hedef
           
    print("Üzgünüm, doğru sayıyı bulamadınız. Doğru sayı:", hedef)

def main():
    while True:
        oyna()
        tekrar = input("Tekrar oynamak ister misiniz? (E/H): ")
        if tekrar.lower() != 'e':
            print("Oyun bitti. Teşekkürler!")
            break   
main()
