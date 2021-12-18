print("--İki basamaklı tam sayıların okunusunu bulma makinesi--")
onlar_basamagi =["","on","yirmi","otuz","kirk","elli","atmis","yetmis","seksen","doksan"]
birler_basamagi =[""," bir"," iki"," üç", " dört"," beş"," alti"," yedi","sekiz"," dokuz"]
girilen_sayi = int(input("Okunuşunu bulmak istediğiniz sayıyı girin: "))
x = girilen_sayi // 10 #girilen_sayi'nin onlar basamagini bulma(yani 10 ile bolumunden tam kisim)
y = girilen_sayi % 10 #girilen_sayi'nin birler basamagini bulma (yani 10 ile bolumunden kalan)
print(onlar_basamagi[x],birler_basamagi[y])
