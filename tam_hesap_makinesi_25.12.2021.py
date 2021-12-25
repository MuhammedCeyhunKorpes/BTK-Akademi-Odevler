print("Hesap Makinesi")
while True:
    print("""İşlem türleri ve numaraları:
    1-Toplama
    2-Çıkarma
    3-Çarpma
    4-Bölme
    """)
    toplama=1
    cikarma=2
    carpma=3
    bolme=4
    islem_turu=int(input("İşlem türünün numarasını giriniz: "))
    if islem_turu==1:
        toplama1=int(input("1. sayıyı girin: "))
        toplama2=int(input("2. sayıyı girin: "))
        print(toplama1+toplama2)
    elif islem_turu==2:
        cikarma1=int(input("1. sayıyı girin: "))
        cikarma2=int(input("2. sayıyı girin: "))
        print(cikarma1-cikarma2)
    elif islem_turu == 3:
        carpma1=int(input("1. sayıyı girin: "))
        carpma2=int(input("2. sayıyı girin: "))
        print(carpma1*carpma2)
    elif islem_turu == 4:
        try:
                bolme1 = int(input("1. sayıyı girin: "))
                bolme2 = int(input("2. sayıyı girin: "))
                print(bolme1 / bolme2)
        except ZeroDivisionError:
            print("Bir sayı 0 a bölünemez!")