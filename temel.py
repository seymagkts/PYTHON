# Print ve format yazimi
"""
#birinciSayi=5
#ikinciSayi=4
#carpimMi=birinciSayi*ikinciSayi
#print(carpimMi)
#print("{} * {} = {} ".format(5,4,5*7))
#print("{}*{}={}".format(birinciSayi,ikinciSayi,carpimMi))
#"eyvallah="alikperim"
#print(eyvallah)
#print("18","19","25", sep=".") # seperate parametresi = değerlerin arasındaki boşluğa istenilen karakteri koyar. tek karakter koyar. """

# Veri tipleri ve değişken tanımlama
"""
from asyncio.windows_events import NULL # import tanımlama
a = 67 # int
b = 31.31 # float
c = "Alikkem" # string
d = '!' # char
booelanMiBu=True # bool true veya false
sayi=NULL # null (int türünde) ctrl ile null'a tıklanıldıgından kaynak kodlarından tipi değiştirilir. 
dizi1 = ["lalala",4,4.23,True,'?',NULL,(1,2,3),["g","h",6],{"kelam":4}] # array-dinamik liste içerisine her türden veri tipi alır
dizi2=list(("lalala",3,4,5)) # ikinci array tanımlama yolu 
f=(2,3,"p") # tuples demetler
sozluk1={"Tekerlek":"Araba","Kağıt":"defter",5:7,"dizi":list((1,2,3))} # sozluk key:value
sozluk2= dict(isim="alikper",soyisim="islam") # ikinci sozluk tanımlama yolu
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(booelanMiBu))
print(type(sayi))
print(type(dizi1))
print(type(dizi2))
print(type(f))
print(type(sozluk1))
print(type(sozluk2))
"""

# Matematik operatorleri
"""
print(6+8)
print(6-8)
print(5*4)
print(5/2)
print(5//2) # tam sayı operatoru
print(5%2) # mod operatoru
print(2**2) # üs alma operatoru
"""
# ileri seviye matematiksel operatorleri için math kütüphanesi import edilmelidir.

# inputtan alınan değerler stringtir
# listelerin metodları: .append(), .pop(), .sort()
# demet(tuple)ların listlerden farkı değiştirilemez olmasıdır. sadece 2 metodu vardır. tuple.count() ve tuple.index().
# sozluklerin metodları: .keys(), .values(), .items()

# dizi ve stringlerde indeks işlemleri
"""
k = "PythonıSeviyorum"
d = [2,3,4,5,6,8,9,22,1,78789]
print(k[-1]) # sonuncu elemanı yazdırır
print(k[len(k)-1]) # sonuncu elemanı yazdırır
print(d[::3]) # dizideki değerleri baştan üçer üçer atlayarak yazdırır
print(d[2::2]) # dizideki değerleri 2. indeksekten başlayarak ikişer ikişer atlayarak yazdırır
print(k[:len(k):2]) # stringteki değerleri baştan ikişer ikişer atlayarak yazdırır
print(k[:4]) # baştan 4. indekse kadar (4. indeks dahil değil) yazdırır
"""

# ----------------------------------------#
# input alma - örnek 1
""" 
vize=float(input("Vize notunuzu giriniz: "))
final=float(input("Final notunuzu giriniz: "))
ortalama=(vize*0.4)+(final*0.6)
print("Ortalamanız: ", ortalama)
 """
# input alma - örnek 2
""" fiyat=float(input("Ürün fiyatını giriniz: "))
kdv=float(input("KDV oranını giriniz: "))
kdv_Fiyat=fiyat+(fiyat*(kdv/100))
print("Tutar: ", kdv_Fiyat) """

# ----------------------------------------#
# karşılaştırma operatorleri
""" # > büyüktür.
# < küçüktür.
# >= büyük eşittir.
# <= küçük eşittir.
# == eşit eşittir.
# != eşit değildir.
# mantıksal operatorler
# && yerine and kullanılır.
# || yerine or kullanılır. 
# ! yerine not kullanılır."""

# if-elif-else koşullu durumları örnek 1
""" vize=float(input("Vize notunuzu giriniz: "))
final=float(input("Final notunuzu giriniz: "))
ortalama=(vize*0.4)+(final*0.6)
print("Ortalamanız: ", ortalama)

if ortalama<=100 and ortalama>=85:
    print("Harf notunuz A")
elif ortalama<85 and ortalama>=65:
    print("Harf notunuz B")
elif ortalama<65 and ortalama>=50:
    print("Harf notunuz C")
elif ortalama>100 or ortalama<0:
    print("bele bişe olamaz")
else:
    print("Başarısız not") """

# if-elif-else koşullu durumları örnek 2
""" fiyat=int(input("Sepet tutarını giriniz: "))
urun_sayisi=int(input("Sepetteki ürün sayısını giriniz: "))
minFiyat=350
minUrun=10
kalanUrun=minUrun-urun_sayisi
kalanFiyat=minFiyat-fiyat

if fiyat>=minFiyat:
    if urun_sayisi>=minUrun:
        print("Yeni tutar: ", fiyat-(fiyat*0.10))
    else: 
        print("İndirim için sepetinize en az {} adet daha ürün ekleyin.".format(kalanUrun))
else: 
     print("İndirim için sepetiniz en az {} TL tutarında ürün ekleyin.".format(kalanFiyat)) """

# ----------------------------------------#
# while ornek 1
""" i=0
while i < 20:
        print("{} tur koştunuz".format(i))
        i+=2

print("\t**********************************************")
"""
# while ornek 2
"""
sayi=int(input("sayi girin: "))
fak=1

while sayi > 1:
    fak*=sayi
    sayi-=1
print(fak) """

# while ile break-continue kullanımı örnek
""" i=0
while i<10:
    if i==3 or i==5: 
        i+=1   
        continue
    if i==9:
         break
    print("i:", i)
    i+=1
     """
# ----------------------------------------#
# diğer dillerde foreach olan yapının python'da for i in dizi olarak dizi elemanlarının yazdırılması
# foreach
""" dizi1=[3.25,7.58,"hamid"]
for i in dizi1:
    print(i)
for i in dizi1[2]:
    print(i) """
# for dongusu -> for i in range(başlangıc sayısı, bitiş sayısı, artırma-azaltma)
# artan şeklinde for döngüsü
""" for i in range(0,50,5):
    print(i) """
# azalan şeklinde for döngüsü
""" for i in range(101,0,-2):
    print(i) """

# for örnek 1
""" sayi=100
for i in range(0,sayi,2):
    print(i) """

# for ile sıcaklık analizi
""" X=""
for i in range(-5,45,4):
    if i>=-5 and i<=0:
        x="donma"
        print("Hava sıcaklığı: {}\nHava durumu {}\n--------------------".format(i,x))
    elif i>0 and i<=18:
        x="ılıman"
        print("Hava sıcaklığı: {}\nHava durumu {}\n--------------------".format(i,x))
    elif i>18 and i<=30:
        x="cok sıcak"
        print("Hava sıcaklığı: {}\nHava durumu {}\n--------------------".format(i,x))
    elif i>30 and i<=45:
        x="UIV"
        print("Hava sıcaklığı: {}\nHava durumu {}\n--------------------".format(i,x))
 """

# for ile roket irtifa hesabına göre kurtarma sistemi
""" birinciKurtarma=False
ikinciKurtarma=False
for i in range(0,3001,100):
    if i==3000:
        birinciKurtarma=True
        print(i,"İrtifada birinci kurtarma aktifleşti.")
        for i in range(3000,0,-100):
            if i>=400 and i<=600:
                ikinciKurtarma=True
                print(i,"İritifada ikinci kurtarma aktifleşti.")
                break """
# fonksiyonlar - void geriye bir şey döndürmeyen fonksiyon
# parametresiz ve geriye dondurmeyen fonksiyon
""" def ode():
    print("Ödeme başarılı")
     """
# parametreli ve geriye dondurmeyen fonksiyon
""" def parkEt(araba):
    print(araba,"park edildi") """

# default parametreli ve geriye dondurmeyen fonksiyon
# fonksiyon cagırıldıgında herhangi bir deger girilmese de default olarak Gıcımını yazdırır. hatayı önler
""" def ogrenci(isim = "Gıcımını", adet = 0):
    print("{} adlı kisi {} adet mail attı".format(isim,adet)) """

# parametreli ve geriye döndüren fonksiyon
""" def kareDondur(sayi):
    return sayi**2
 """
# fonksiyonların çağırılması
""" ode() 
parkEt("GTR")
ogrenci(adet=8) # default parametre calısır
ogrenci("Alikper",6) # default parametre olmasına ragmen atanan değer calısır

a = kareDondur(6)
print(a) # return içeren fonksiyon yazdırma 

print(kareDondur(5)) # return içeren fonksiyon yazdırma 2
 """
# fonksiyonlar ornek 1 - fonksiyon içinde başka bir fonksiyon çağırma
""" import math 
def hesapla(sayi1,sayi2):
    sonuc= (math.cos(sayi1)) + (math.pow(2,sayi2))
    return sonuc
def fonksiyonCagir():
    return hesapla(90,5)+10 # fonksiyon içinde fonksiyon çağırma
print(fonksiyonCagir()) """

# fonksiyonlar ornek 2 - recursive (özyinelemeli) fonksiyon - fonksiyonun kendi içinde kendini çağırması
""" def sat(fiyat,kdv):
    kdvli_fiyat= fiyat+((fiyat*kdv)/100)
    if kdvli_fiyat>500:
        kdvli_fiyat=sat(fiyat,kdv-5)
    return kdvli_fiyat  
print(sat(600,18)) """

# String - list fonksiyonları
""" .startswith("") -> string/liste bununla baslıyor mu?
.endswith("") -> string/liste bununla bitiyor mu?
.replace("","") -> ilk parametreyi ikinci ile değistir
.append("") -> listenin sonuna ekleme yapar
.pop() -> listenin içine indeks verilmezse listenin son elemanını cıkarır, verilirse o indeksteki elemanı cıkarır.
 """
