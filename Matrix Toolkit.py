import numpy as np
from fonksiyonlar2 import *

while True:
    print("\n--Matrix Toolkit--")
    print("\nYapmak İstediğiniz İşlemi Seçiniz:")
    print("A- İki Matrisin Toplamı")
    print("B- İki Matrisin Eleman Bazlı Çarpımı")
    print("C- İki Matrisin Matris Çarpımı")
    print("D- Bir Matrisin Bir Skaler İle Çarpımı")
    print("E- İki Vektörün Skaler Çarpımı")
    print("F- Bir Matrisin Transpozu")
    print("G- Vektör Normu Hesaplama")
    print("H- Birim Matris Oluşturma")

    print("\nQ- ÇIKIŞ")

    cevap = input("\nCevap: ").lower()

    if cevap == "q":
        print("Kapatılıyor...")
        break

    elif cevap in ["d", "f"]:

        satir = int(input("Kaç satırlı bir matris olsun? "))
        sutun = int(input("Kaç sütunlu bir matris olsun? "))

        bos_liste = []
        for i in range(satir):

            satırsayıları = input(f"{i + 1}. satırdaki {sutun} elemanı aralarında boşluk bırakarak girin:")

            sayılar = [float(x) for x in satırsayıları.split()]
            bos_liste.append(sayılar)

        A = np.array(bos_liste)

        if cevap == "d":
            sonuç = Sileçarpım(A)
            print(sonuç)

        elif cevap == "f":
            sonuç = transpoz(A)
            print(sonuç)

    elif cevap == "h":

        sonuç = birimMatris()
        print(sonuç)


    elif cevap in ["a", "b", "c"]:

        while True:
            satır_a = int(input("1. Matrisin satır sayısı: "))
            sütun_a = int(input("1. Matrisin sütun sayısı: "))

            liste_a = []
            for i in range(satır_a):
                veri = input(f"1. Matrisin {i + 1}. satırındaki {sütun_a} elemanı boşluklu girin: ")
                sayılar = [float(x) for x in veri.split()]
                liste_a.append(sayılar)

            A = np.array(liste_a)

            satır_b = int(input("2. Matrisin satır sayısı: "))
            sütun_b = int(input("2. Matrisin sütun sayısı: "))

            liste_b = []
            for i in range(satır_b):
                veri = input(f"2. Matrisin {i + 1}. satırındaki {sütun_b} elemanı boşluklu girin: ")
                sayılar = [float(x) for x in veri.split()]
                liste_b.append(sayılar)

            B = np.array(liste_b)

            if cevap == "a":
                if A.shape != B.shape:
                    print("HATA: Toplama işlemi için boyutlar eşit olmalıdır!")
                    continue
                sonuç = toplam(A, B)
                print(sonuç)
                break

            elif cevap == "b":
                if A.shape != B.shape:
                    print("HATA: Eleman bazlı çarpım için boyutlar eşit olmalıdır!")
                    continue
                sonuç = Eçarpım(A, B)
                print(sonuç)
                break

            elif cevap == "c":
                if A.shape[1] != B.shape[0]:
                    print("HATA: 1. matrisin sütun sayısı 2. matrisin satır sayısına eşit olmalıdır!")
                    continue
                sonuç = Mçarpım(A, B)
                print(sonuç)
                break

    elif cevap == "e":
        while True:
            v1 = input("1. Vektörün elemanlarını aralarında boşluk bırakarak girin: ")
            A = np.array([float(x) for x in v1.split()])

            v2 = input("2. Vektörün elemanlarını aralarında boşluk bırakarak girin: ")
            B = np.array([float(x) for x in v2.split()])

            if A.shape != B.shape:
                print(f"HATA: Vektör eleman sayıları eşit olmalıdır!")
                continue
            else:
                sonuç = VSçarpım(A, B)
                print(sonuç)
            break

    elif cevap == "g":
        v1 = input("1. Vektörün elemanlarını aralarında boşluk bırakarak girin: ")
        A = np.array([float(x) for x in v1.split()])

        sonuç = vektörnorm(A)
        print(sonuç)

    elif cevap not in ["a", "b", "c", "d", "e", "f", "g", "q", "h"]:
        print("Geçersiz Seçenek!")
        continue

    devammı = input("\nAna Menüye Dönmek İster misiniz? (e/h): ").lower()
    if devammı == "e":
        continue

    print("Kapatılıyor...")
    break