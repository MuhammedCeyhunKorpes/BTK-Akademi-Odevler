print("Üçgenin çeşidini algılama makinesi")
sayi1=float(input("1. Kenarın uzunluğunu giriniz: "))
sayi2=float(input("2. kenarın uzunluğunu giriniz: "))
sayi3=float(input("3. kenarın uzunluğunu giriniz: "))

"""
hepsi farkliysa cesitkenar
ikisi ayniysa ikizkenar
ucu de ayniysa eskenar

"""
if sayi1==sayi2==sayi3:
    print("Üçgen eşkenardır. ")
elif sayi1==sayi2:
    print("Üçgen ikizkenardır.")
elif sayi2==sayi3:
    print("Üçgen ikizkenardır. ")
elif sayi1==sayi3:
    print("Üçgen ikizkenardır. ")

else:
    print("Üçgen çeşitkenardır. ")
