'''print("O sene Bu sene")
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
    print("Sayı tektir.")''
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
    print("girilen sayıların toplamı:",toplam),'''
sayilar=[3,5,8,61]
sayilar.append(10)
sayilar.remove(8)
sayilar.insert(2,7)
sayilar.pop()   
sayilar.sort()
print(sayilar[0])
print(len(sayilar))
