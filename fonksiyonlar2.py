import numpy as np

def toplam(A,B):

    return A+B

def Mçarpım(A,B):

    return A@B

def Eçarpım(A,B):

    return A*B

def Sileçarpım(A):

    s = int(input("Bir Sayı Giriniz: "))

    return s*A

def VSçarpım(A,B):

    return A@B

def transpoz(A):

    return A.T

def vektörnorm(A):
    i=0
    for d in A:
        i = i + d**2
    return i ** (1 / 2)

def birimMatris():  ##burda parametre yazmadık çünkü n yi dışardan almıyoruz

    n = int(input("Birim Matris İçin Boyut Giriniz: "))

    return np.eye(n)