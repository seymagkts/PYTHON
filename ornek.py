# Fonksiyonlara kadar
# ******************** TEMEL ********************
# Oyuncu Kaydetme Programı
"""
print("Oyuncu kaydetme programı")

ad = input("Oyuncunun adı: ")
soyad = input("Oyuncunun soyadı: ")
takim = input("Oyuncunun takimi: ")

print("Bilgiler kaydediliyor...")

print("Oyuncunun adi: {} \nOyuncunun soyadı: {} \nOyuncunun takımı: {}".format(ad,soyad,takim))
print("Bilgiler kaydedildi.")"""

# Kok Bulma
import random

"""
a = int(input("Birinci sayıyı giriniz: "))
b = int(input("İkinci sayıyı giriniz: "))
c = int(input("Üçüncü sayıyı giriniz: "))

delta = (b**2) - (4*a*c)

kok1 = (-b - delta ** 0.5) / (2*a) # karekokunu almak için 1/2 üssü alınır yani 0.5
kok2 = (-b + delta ** 0.5) / (2*a)

print("Birinci kök: {} \nİkinci kök: {}".format(kok1,kok2))"""

# Format Metoduyla Carpma
"""
a = int(input("Sayi1 girin: "))
b = int(input("Sayi2 girin: "))
c = int(input("Sayi3 girin: "))

print("Çarpmanın sonucu: {}".format(a*b*c)) """

# Beden Kitle İndeksi
"""
boy = float(input("Boyunuzu giriniz (m): "))
kilo = int(input("Kilonuzu giriniz: "))

indeks = kilo / (boy*boy)

print("Beden kitle indeksiniz: ",indeks)"""

# Kilometre Yakıt Hesabı
"""
kilometre = int(input("Aracın kilometresi: "))
yakit = int(input("Aracın kilometrede yaktığı miktar: "))

print("Ödemeniz gereken tutar: ",kilometre*yakit)"""

# Alınan Bilgileri Alt Alta Yazdırma
"""
ad = input("Adınız: ")
soyad = input("Soyadınız: ")
numara = input("Numaranız: ")

print(ad,soyad,numara,sep="\n")"""

# Alınan Değerleri Birbirleriyle Değiştirme
"""
x = input("x: ")
y = input("y: ")
x,y = y,x

print("x:",x, "y:",y)"""

# Hipotenüs Bulma
"""
kenar1 = int(input("a kenarını girin: "))
kenar2 = int(input("b kenarını girin: "))

hipotenus = int(((kenar1 ** 2) + (kenar2 ** 2)) ** 0.5)

print("Hipotenüsün uzunluğu: ",hipotenus)"""

# ******************** KOŞUL DURUMLARI ********************
# Basit Hesap Makinesi
"""
print("İşlem 1: Toplama","İşlem 2: Çıkarma","İşlem 3: Çarpma","İşlem 4: Bölme",sep="\n")
print("**************************************************************")
a = int(input("Sayi girin: "))
b = int(input("Sayi girin: "))
print("**************************************************************")
islem =input("İşlem secin: ")

if (islem == "1"):
    print(a+b)
elif (islem == "2"):
    if (a>b):
        print(a-b)
    else:
        print(b-a)
elif (islem == "3"):
    print(a*b)
elif (islem == "4"):
    if (a > b):
        print(a // b)
    else:
        print(b // a)
else:
    print("Gecersiz islem.")"""

# Kullanıcı Girişi
"""
gecerli_kullanici_adi = "sgoktas"
gecerli_sifre = "12345"

kullanici_adi = input("Kullanici Adi: ")
sifre = input("Sifre: ")

if (gecerli_sifre == sifre and gecerli_kullanici_adi == kullanici_adi):
    print("Giris basarılı...")
elif (gecerli_sifre != sifre and gecerli_kullanici_adi == kullanici_adi):
    print("Sifre hatalı")
elif (gecerli_sifre == sifre and gecerli_kullanici_adi != kullanici_adi):
    print("Kullanıcı adı hatalı")
elif (gecerli_sifre != sifre and gecerli_kullanici_adi != kullanici_adi):
    print("Kullanıcı adı ve sifre hatalı") """

# Beden kitle indeksine göre vücut tipini yazdırma
"""
boy = float(input("Boyunuzu girin: "))
kilo = int(input("Kilonuzu girin: "))
indeks = kilo / (boy**2)
if (indeks <= 18.5):
    print("İndeksiniz: {} Zayıfsınız".format(indeks))
elif (indeks > 18.5 and indeks < 25):
    print("İndeksiniz: {} Normalsiniz".format(indeks))
elif (indeks >= 25 and indeks <= 30):
    print("İndeksiniz: {} Fazla kilolusunuz".format(indeks))
elif (indeks > 30):
    print("İndeksiniz: {} Obezsiniz".format(indeks))"""

# Girilen sayıların en büyüğünü bulma
"""
a = input("Sayi girin: ")
b = input("Sayi girin: ")
c = input("Sayi girin: ")

if (a>b and a>c):
    print("En büyük sayi",a)
elif (b>a and b>c):
    print("En büyük sayi",b)
elif (c>a and c>b):
    print("En büyük sayi",c)
elif (a==b==c):
    print("Sayılar eşit") """

# Harf notu hesaplama
"""
vize1 = int(input("Vize 1 notunuzu giriniz: "))
vize2 = int(input("Vize 2 notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))

toplam_not = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)
print("**************************************")
print("Not ortalamanız : ", toplam_not)
print("**************************************")
if (toplam_not >= 90):
    print("Harf Notunuz AA")
elif (toplam_not >= 85):
    print("Harf Notunuz BA")
elif (toplam_not >= 80):
    print("Harf Notunuz BB")
elif (toplam_not >= 75):
    print("Harf Notunuz CB")
elif (toplam_not >= 70):
    print("Harf Notunuz CC")
elif (toplam_not >= 65):
    print("Harf Notunuz DC")
elif (toplam_not >= 60):
    print("Harf Notunuz DD")
elif (toplam_not >= 55):
    print("Harf Notunuz FD")
elif (toplam_not < 55):
    print("Harf Notunuz FF") """

# Ucgen mi dikdörtgen mi yazdırma
"""
islemler = print("1. Dörtgen tipi bulma","2. Ücgen tipi bulma", sep="\n")
islem=(input("Bir işlem seçiniz: "))

if (islem=="1"):
    dortgenA = int(input("Bir kenar giriniz: "))
    dortgenB = int(input("Bir kenar giriniz: "))
    dortgenC = int(input("Bir kenar giriniz: "))
    dortgenD = int(input("Bir kenar giriniz: "))
    if (dortgenA==dortgenB and dortgenB==dortgenC and dortgenC==dortgenD):
        print("Bir karedir.")
    elif ((dortgenA==dortgenB) and (dortgenC==dortgenD)) or ((dortgenA==dortgenC and dortgenD==dortgenB)) or ((dortgenA==dortgenD and dortgenC==dortgenB)):
        print("Bir dikdörtgendir.")
    else:
        print("Normal bir dörtgendir")

elif (islem=="2"):
    ucgenA = int(input("Bir kenar giriniz: "))
    ucgenB = int(input("Bir kenar giriniz: "))
    ucgenC = int(input("Bir kenar giriniz: "))
    if (abs(ucgenA-ucgenC)<ucgenB and ucgenB<ucgenA+ucgenC) and (abs(ucgenB-ucgenC)<ucgenA and ucgenA<ucgenB+ucgenC) and (abs(ucgenB-ucgenA)<ucgenC and ucgenC<ucgenB+ucgenA):
        if (ucgenA==ucgenB==ucgenC):
            print("Eşkenar ücgendir")
        elif (ucgenA==ucgenB or ucgenA==ucgenC or ucgenC==ucgenB):
            print("İkizkenar ücgendir")
        else:
            print("Normal bir üçgendir")
    else:
        print("Ucgen oluşmaz")
else:
    print("Gecersiz islem") """

#  Bankamatik uygulaması
"""
bakiye=5000
print("Basit ATM Uygulaması","1. Para cekme","2. Para yatırma","3. Bakiye sorgulama","Çıkmak icin 'q'ya basın",sep="\n")
print("*************************************************************")
while (True):
    print("*************************************************************")
    islem = input("Bir islem seciniz: ")
    if (islem == "1"):
        cekilecek_tutar = int(input("Tutar giriniz: "))
        if (cekilecek_tutar > bakiye):
            print("Bakiye yetersiz...")
            continue
        bakiye -= cekilecek_tutar
        print("Kalan bakiyeniz: ", bakiye)
    elif (islem == "2"):
        yatirilacak_tutar = int(input("Tutar giriniz: "))
        bakiye += yatirilacak_tutar
        print("Yeni bakiyeniz: ", bakiye)
    elif (islem == "3"):
        print("Bakiyeniz: ",bakiye)
    elif (islem=="q"):
        print("Çıkış yapılıyor...")
        break
    else:
        print("Gecersiz islem...") """

# Girilen 3 basamaklı bir sayının basamaklarının küpleri toplamı sayının kendine eşit olup olmadığını bulan program
"""
sayi=int(input("3 basamaklı sayi giriniz: "))
toplam=0

for i in range(3):
    basamak = sayi % 10
    toplam += (basamak**3)
    sayi = sayi // 10
print(toplam)

if (toplam==sayi):
    print("Eşittir")
else:
    print("Eşit değildir")"""

# Klavyeden girilen 20 adet sayıdan çift sayıların toplamının tek sayıların toplamına oranını bulan program
"""
cift=0
tek=0
sayilar = []
for i in range(20):
    sayi = int(input("Sayi giriniz: "))
    sayilar.append(sayi)
print(sayilar)

for i in sayilar:
    if (i%2==0):
        cift += i
    else:
        tek += i
print(cift/tek) """

# Girilen sayının 5'in kuvveti olup olmadığını bulan program
"""
sayi=int(input("Bir sayi giriniz: "))
for i in range(sayi):
    if (sayi%5==0):
        sayi = sayi / 5
if (sayi==1):
    print("5'in kuvvetidir")
else:
    print("5'in kuvveti değildir")"""

# Girilen sayının mükemmel sayı olup olmadığını bulan program, mükemmel sayi = kendisini tam bölen sayıların toplamı kendisine eşittir
"""
sayi=int(input("Bir sayi giriniz: "))
toplam=0
for i in range(1,sayi):
    if (sayi % i == 0):
        toplam += i
if (toplam==sayi):
    print("{} bir mükemmel sayidir.".format(sayi))
else:
    print("{} bir mükemmel sayi değildir.".format(sayi))"""

# ******************** DÖNGÜLER ********************
# Faktoriyel bulma
"""
while (True):
    faktoriyel=1
    print("\n****************************")
    print("Cıkıs icin 'q'ya basınız...\n")
    sayi=input("Sayi giriniz: ")
    if (sayi=='q'):
        print("Program sonlanıyor...")
        break
    else:
        sayi=int(sayi)
    for i in range(1,sayi+1):
        faktoriyel *= i
    print("Faktoriyel: {}".format(faktoriyel)) """

# Fibonacci
"""
a=1
b=1
fibonacci=[a,b]
sayi=int(input("Sayi giriniz: "))
for i in range(sayi):
    a,b=b,a+b
    fibonacci.append(b)
print(fibonacci) """

# Mükemmel sayı algoritması
"""
sayi=int(input("Sayi giriniz: "))
toplam=0
for i in range(1,sayi):
    if(sayi % i ==0):
        toplam += i
if (sayi==toplam):
    print("Mükemmel sayıdır.")
else:
    print("Mükemmel sayi değildir.") """

# Armstrong sayi
"""
sayi = input("Sayi giriniz: ")
yedek = sayi
liste = []
toplam=0
for i in sayi:
    i = int(yedek) % 10
    yedek = int(yedek) // 10
    liste.append(i)
for x in liste:
    ix = x ** len(liste)
    toplam += ix
if (toplam==int(sayi)):
    print("{} bir armstrong sayidir.".format(sayi))
else:
    print("{} bir armstrong sayi değildir.".format(sayi))"""

# 1'den 10'a kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
"""
for i in range(1,11):
    for j in range(1,11):
        print(i,"x",j,"=", i*j)
    print("*********************") """

# her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin.
# Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
"""
print("*****************************")
print("Cıkmak icin 'q'ya basın...")
print("*****************************")
toplam=0
while (True):
    sayi = input("Bir sayi giriniz: ")
    if (sayi == 'q'):
        break
    toplam += int(sayi)
print("Girilen sayilarin toplamı: {}".format(toplam)) """

# 1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.
"""
liste = []
for i in range (1,101):
    if (not(i%3==0)):
        continue
    else:
        liste.append(i)
print(liste) """

# list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.
"""
liste=[*range(1,101)]
liste2=[i for i in liste if i % 2 == 0] 
print(liste2) """

# 5 elemanlı dizideki değerlerin toplamını bulan program
"""
dizi = [5,9,10,189,52]
toplam=0
for i in dizi:
    toplam += i
print("Dizi: ",dizi)
print("Dizinin elemanlarının toplamı: ",toplam)"""

# Girilen kelimeyi tersten yazdıran program
"""
kelime = input("Bir kelime giriniz: ")
ters = kelime[::-1]
print("Girilen kelimenin tersi: {}".format(ters)) """

# Bir dizide dizi elemanlarının sondan başa gelecek şekilde düzenlenmesini sağlayan program
"""
dizi = []
for i in range(5):
    sayi=input("Dizi elemanı giriniz: ")
    dizi.append(sayi)
ters = dizi[::-1]
print("Dizi: {}".format(dizi))
print("Dizinin tersi: {}".format(ters)) """

# Bir dizide dışarıdan girilen bir sayının, dizinin elemanlarından kaç tanesinden küçük olduğunu bulan program
"""
dizi = [8,95,10,53,-5,72,7,4,21,92,-85,-56,41]
sayi = input("Sayi giriniz: ")
yeni_dizi=[]
for i in dizi:
    if (int(sayi)<i):
        yeni_dizi.append(i)
print("{}, dizinin {} elemanından küçüktür.".format(sayi,len(yeni_dizi)))"""

# Ekrandan girilen bir sayı eğer 5-10 arasında ise girilen sayının karesini alıp gösteren, eğer 5'ten küçük ise faktöriyelini alan,
# 10'dan büyük ise sayıyı ikiye bölüp bir eksiğini yazan program
"""
sayi=int(input("Bir sayi giriniz: "))
faktoriyel=1
if (sayi<=5):
    while (sayi>1):
        faktoriyel *= sayi
        sayi-=1
    print(faktoriyel)
elif (sayi>5 and sayi<=10):
    print(sayi ** 2)
elif (sayi>10):
    print((sayi/2)-1) """

# 10 elemanlı bir sayı dizisinin ortalaması tam sayı ise bu sayıdan dizide kaç tane olduğunu veren program
"""
dizi=[]
yeni_dizi=[]
ortalama=0
toplam=0
for i in range(10):
    eleman = int(input("Eleman giriniz: "))
    dizi.append(eleman)
for i in dizi:
    toplam += i
ortalama =toplam/len(dizi)
print("********")
print("Dizi: {}".format(dizi))
print("********")
print("Dizinin toplamı: ",toplam)
print("Dizinin ortalaması: ",ortalama)
print("********")
if (toplam % 10 == 0):
    for i in dizi:
        if (i==ortalama):
            yeni_dizi.append(i)
    print("Dizide {}'dan {} tane vardır.".format(ortalama,len(yeni_dizi)))
else:
    print("Dizinin ortalaması tam sayı değildir.") """

# Girilen cümlede, girilen karakterden kaç tane olduğunu bulan program
"""
aranan = input("Bir cümle giriniz: ")
aranacak = input("Aranacak karakteri seçiniz: ")
total = []
for i in aranan:
    if (i==aranacak):
        total.append(i)
print("{} karakteri '{}' içinde {} tane var.".format(aranacak,aranan,len(total))) """
# Asal carpan bulma
"""
def asal_bulma():
    sayi = int(input("Bir sayi giriniz: "))
    dizi = []
    i=2
    while i < sayi:
        if sayi % i == 0:
            dizi.append(i)
        i += 1
    print("{} asal bölenleri: {}".format(sayi, dizi))
    if (len(dizi)==0):
        print("Bu sayı asaldır.") """
# Girilen sayının smith sayısı olup olmadığını bulan program
# Smith sayısı:  1 den büyük asal olmayan bir tam sayının rakamlarının toplamı, sayı, asal çarpanlarına ayrılarak yazıldığında bu yazılışta bulunan tüm asal çarpanların rakamlarının
# toplamına eşit oluyorsa bu tür sayılara denir
"""
sayi = int(input("Sayi giriniz: "))
yedek_sayi = str(sayi)
basamak = len(yedek_sayi)
asal_carpan = 0
carpan_toplam = 0
rakam_toplam = 0
# sayinin basamakları toplamı
for i in range(0,basamak):
    rakam_toplam += int(yedek_sayi[i])
# sayinin asal carpanları toplamı
for asal in range(2,sayi):
    if (sayi % asal == 0 ):
        sayi_basamak = str(asal)
        for bas in sayi_basamak:
            carpan_toplam += int(bas)

if (carpan_toplam==rakam_toplam):
    print("{} bir smith sayısıdır.".format(sayi))
else:
    print("{} bir smith sayısı değildir.".format(sayi))

print(rakam_toplam)
print(carpan_toplam) """

#*****************************************

"""
sayi = int(input("Sayi giriniz: ")) # sayi degiskeni elimizde - int

stringSayi=str(sayi)
basamak = len(stringSayi)

# basamakalari toplami:
elemanToplam=0
for i in range(0,basamak):
    elemanToplam += int(stringSayi[i])
print(elemanToplam)


tamBolenler=0
# asal carpanlari:
for x in range(2,sayi):
    if(sayi%x==0):
        sayiBasamak=str(x)
        for i in sayiBasamak:
            tamBolenler+=int(i)
print(tamBolenler)

if(elemanToplam==tamBolenler):
    print(sayi,"bir smith sayisidir.") """

# 1000'e kadar olan smith

"""
smithSayilari = []

def AsalCarpanlariBul(n):
    dizi = []
    n = int(n)
    tamBolenler = []
    for i in range(2, n):
        while n % i == 0:
            n = n / i
            tamBolenler.append(i)
    for i in tamBolenler:
        if (AsalMi(i)):
            dizi.append(i)
    return dizi


def AsalMi(n):
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
            break
        else:
            return True


def diziElemanlariniTopla(dizi):
    diziToplam = 0
    for i in dizi:
        gecici = str(i)
        for j in range(len(gecici)):
            diziToplam += int(gecici[j])
    return diziToplam


def sayiDegerleriniTopla(sayi):
    sayiDegerleriToplam = 0
    sayi = str(sayi)
    for i in range(len(sayi)):
        sayiDegerleriToplam += int(sayi[i])
    return sayiDegerleriToplam


for k in range(2, 1000):
    if diziElemanlariniTopla(AsalCarpanlariBul(k)) == sayiDegerleriniTopla(k):
        smithSayilari.append(k)

print(smithSayilari)"""

# EBOB / EKOK bulma
"""
islemler = print("1. EBOB - EKOK Bulma\n"
                 "Çıkış için q'ya basınız...")
while (True):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    islem=input("Bir islem seciniz: ")
    if (islem == "1"):
        ebob1 = int(input("Bir sayi giriniz: "))
        ebob2 = int(input("Bir sayi giriniz: "))
        ortak_bolen = []
        for i in range(1,ebob1):
            if (ebob1 % i == 0) and (ebob2 % i == 0):
                ortak_bolen.append(i)
        print("{} ve {} EBOB'u: {} ".format(ebob1,ebob2,max(ortak_bolen)))
        ortak_kat = (ebob1*ebob2)//int(max(ortak_bolen))
        print("{} ve {} EKOK'u: {}".format(ebob1,ebob2,ortak_kat))
    elif (islem == "q"):
        print("Program sonlanıyor...")
        break
    else:
        print("Geçersiz islem...") """

# Kayıt
"""
print("Hos Geldiniz...")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("KAYIT")
ad_kullanici = input("Adınızı giriniz: ")
soyad_kullanici = input("Soyadınızı giriniz: ")
tcKimlik_kullanici = int(input("TC kimlik numaranızı giriniz: "))
dogumTarihi_kullanici = input("Dogum tarihinizi giriniz: ")
eposta_kullanici = input("Epostanızı giriniz: ")
eposta2_kullanici = input("Epostanızı giriniz (tekrar): ")
sifre_kullanici = input("Sifrenizi giriniz: ")
sifre2_kullanici = input("Sifrenizi giriniz (tekrar): ")

while (True):
    if (sifre_kullanici == sifre2_kullanici) and (eposta_kullanici == eposta2_kullanici):
        kod = random.randint(1000,10000)
        print(kod)
        dogrulama = int(input("Kodu giriniz: "))
        if (kod == dogrulama):
           print("KAYİT BASARILI...")
           print("{} {}, Genc Ne Sever'e Hos Geldiniz....".format(ad_kullanici,soyad_kullanici))
           break
        else:
            print("KOD HATALI...")
    elif (sifre_kullanici == sifre2_kullanici) and (eposta_kullanici != eposta2_kullanici):
        print("E-POSTANIZ HATALI...")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        eposta_kullanici = input("Epostanızı giriniz: ")
        eposta2_kullanici = input("Epostanızı giriniz (tekrar): ")
        sifre_kullanici = input("Sifrenizi giriniz: ")
        sifre2_kullanici = input("Sifrenizi giriniz (tekrar): ")
    elif (sifre_kullanici != sifre2_kullanici) and (eposta_kullanici == eposta2_kullanici):
        print("SİFRENİZ HATALI...")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        eposta_kullanici = input("Epostanızı giriniz: ")
        eposta2_kullanici = input("Epostanızı giriniz (tekrar): ")
        sifre_kullanici = input("Sifrenizi giriniz: ")
        sifre2_kullanici = input("Sifrenizi giriniz (tekrar): ")
    elif (sifre_kullanici != sifre2_kullanici) and (eposta_kullanici != eposta2_kullanici):
        print("SİFRENİZ VE E-POSTANIZ HATALI...")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        eposta_kullanici = input("Epostanızı giriniz: ")
        eposta2_kullanici = input("Epostanızı giriniz (tekrar): ")
        sifre_kullanici = input("Sifrenizi giriniz: ")
        sifre2_kullanici = input("Sifrenizi giriniz (tekrar): ") """
