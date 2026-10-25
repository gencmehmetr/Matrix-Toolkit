import numpy as np

def Mçarpım(A, B):

  satır_A, sütun_A = A.shape   ## A nın ölçülerini kendi değişkenlerimize atadık
  satır_B, sütun_B = B.shape
  sonuç = np.zeros((satır_A, sütun_B))   ## elemanları sıfır olan geçici bir matris oluşturduk sonra elemanları atamak için.

  for i in range(satır_A):
    for j in range(sütun_B):
      for k in range(sütun_A):
        sonuç[i][j] += A[i][k] * B[k][j]

  return sonuç