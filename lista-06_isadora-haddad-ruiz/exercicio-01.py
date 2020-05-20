# Utilize funções NumPy para:
import numpy as np
import math

s1 = np.array([168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
       242, 331, 251, 323, 106, 1055, 170])
len_s1 = (print('Quantidade de elementos (s1): ', len(s1)))

s2 = np.array([168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
       242, 331, 251, 180, 106, 1055, 200])
len_s2 = (print('Quantidade de elementos (s2): ', len(s2)))

print( )

def euclidiana(s1, s2):
    if len_s1 == len_s2:
        distancia = np.sqrt(np.sum((s1-s2)**2))

    return distancia

print('A distância euclidiana entre as séries é', '%.2f' %euclidiana(s1, s2))

print( )

def mean(s1, s2):
    if len_s1 == len_s2:
        a = s1, s2
        media = (np.mean(a, axis=0))
    return media

print('Série temporal com os valores médios:\n', mean(s1,s2))

print( )

def max(s1, s2):
    if len_s1 == len_s2:
        x = s1, s2
        maximo = np.amax(x, axis=0)
    return maximo

print('Série temporal com os valores máximos:\n', max(s1,s2))

print( )

def min(s1, s2):
    if len_s1 == len_s2:
        x = s1, s2
        minimo = np.amin(x, axis=0)
    return minimo

print('Série temporal com os valores mínimos:\n', min(s1,s2))

