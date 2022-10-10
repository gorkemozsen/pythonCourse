## integer (int)
fps = 30
x = 7

## +, -, *, /, **

hiz = int(fps**x)




## float (ondalıklı sayı)
## +,-,/,**,//
point = 1.5

hiz = fps//x

##print(float(fps))


## string (Metin)

message = 'Oyuna hoşgeldiniz '

username = "Görkem"

## str fonksiyonu farklı tipleri stringe dönüştürür.

##print(str(987))



##last_message = "Hoşgeldiniz " "Görkem"

##print(f"{message} {username}. Bugün Nasılsın?")

##print("{1} {0}. Bugün Nasılsın?".format(message, username))


## boolean
start = False,True


##pass_at_database = "12345"
##
##password = input("Give me your password: ")
##
##print(pass_at_database == password)


## liste, sözlük, kümeler, tuple(demet)

## inputun çıktısı string olur. Tipi değiştirilebilir.

##name = input("Give me Your name: ")
##
##age = int(input("How old are you! "))
##kilo = input(" How much is your weight!  ")
##
##kilo = int(kilo)
##
##bilimsel_deger = age*kilo
##
##print(f"Sayın {name} Bilimsel Değeriniz {bilimsel_deger}")


##password = input("Give me your password: ")
##
##tip = type(password)
##
##print(f"Bu şifrenin tipi: {tip}")

"""
Kullanıcıdann adını, sınıfını ve 3 tane sınavını alarak ortalamasını hesapla.

"""

print("-"*30)
print("ORTALAMA HESAPLAMA ARACI ")

username = input("Adınız: ")

sinif = input("Sınıfınız: ")

not_1 = int(input(" Birinci Sınav Notu:  "))
not_2 = int(input(" İkinci Sınav Notu:  "))
not_3 = int(input(" Üçüncü Sınav Notu:  "))

SINAV_SAYISI = 3

ortalama = (not_1 + not_2 + not_3) // SINAV_SAYISI

print(f" Sayın {username} ortalamanız {ortalama} ")

