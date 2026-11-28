print("O sene Bu sene")
İsim= "yusuf şimşek" 
yaş= 18
boy= 1.67
ogrenci_mi= True

print(isim,type(isim))
print(yaş,type(yaş))
print(boy,type(boy))
print(ogrenci_mi,type(ogrenci_mi))
print(5+int(boy))
isim = input("Adın: ")
yas = int(input("Yaşın: "))
boy = float(input("Boyun: "))
print(f"Merhaba {isim}, {yas} yaşındasın ve boyun {boy:.2f} m.")
a=int(input("Bir sayı giriniz: "))
b=int(input("Bir sayı daha giriniz: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print(a==b)
print(a>10 or b>10)
print(a>20 or b==5)
print(not(a>b))
sayi=int(input("Bir sayı giriniz: "))
if sayi>0:
    print("Sayı pozitiftir.")
elif sayi<0:
    print("Sayı negatiftir.")
else:
    print("Sayı sıfırdır.")
if sayi%2==0:
    print("Sayı çifttir.")
else:
    print("Sayı tektir.")

for i in range(1,11):
    print(i)
toplam=0
for i in range(1,101):
    toplam=toplam+i
print(toplam)
while True:
    sayi=int(input("Bir sayı giriniz: "))
    if sayi==0:
        break
    toplam= toplam+sayi
    print("girilen sayıların toplamı:",toplam),
sayilar=[43,5,8,61]
sayilar.append(10)
sayilar.remove(8)
print(sayilar)
sayilar.insert(2,7)
print(sayilar)
sayilar.pop()   
print(sayilar)
sayilar.sort()
print(sayilar)
print(len(sayilar))
koordinat=(10,20,15)
print(koordinat[2])
meyveler={"hamsi","palamut","hamsi"}
print(meyveler)
ogrenci={"isim":"yusuf","yaş":18,"boy":1.67}
print(ogrenci["isim"])
ogrenci["boy"]=1.68
print(ogrenci.keys())
print(ogrenci.values())
metin= "       Yusuf Şimşek ytü kontrol ve otomasyon mühendisliğinde okuyan bir öğrencidir.  "
print(metin.strip())
print(metin.lower())
print(metin.upper())
print(metin.replace("Şimşek","ŞİMŞEK"))
print(metin.split())
print(len(metin))

def topla(x,y):
    return x+y
print(topla(60,1))
def çarpma(a,b):
    return a*b
print(çarpma(5,6))
a=input("bir sayı giriniz: ")
b=input("bir sayı daha giriniz: ")
print(topla(int(a),int(b)))
def selamla(isim="misafir"):
    return"merhaba "+isim
print(selamla(" yusuf"))
print(selamla())
with open("yusmek.txt","r", encoding="utf-8") as dosya:
    print(dosya.read())
with open("yusmek.txt","a", encoding="utf-8") as dosya:
    dosya.write("\nYusuf Şimşek")
with open("yusmek.txt","w", encoding="utf-8") as dosya:
    dosya.write("Yusuf Şimşek")
import random
print(random.randint(1,100))
print(random.choice(["elma","armut","muz"]))
from datetime import datetime
simdi=datetime.now()
print(simdi.year,simdi.month,simdi.day)
print(simdi.strftime("%d/%m/%Y %H:%M:%S"))
import json
veriler={"isim":"yusuf","yas":18,"notlar":[90,85,95]}
metin=json.dumps(veriler)
print(metin)
geri=json.loads(metin)
print(geri["isim"])
class ogrenci:
    def __init__(self,isim,yas,):
        self.isim=isim
        self.yas=yas
    def tanıt(self):
        return f"merhaba ben {self.isim} ve {self.yas} yaşındayım."
o=ogrenci("yusuf",18)
print(o.tanıt())
print(o.isim)