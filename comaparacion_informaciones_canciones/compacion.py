# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 23:11:52 2022
@author: USUARIO
"""
import math
residente = list(open("residente.txt",encoding="utf8"))
balvin = list(open("morado.txt",encoding="utf8"))
type(residente)
#print(residente)
str_residente = "".join(residente)
str_balvin = "".join(balvin)
palabras_r = list(set(str_residente.split()))
palabras_b = list(set(str_balvin.split()))
d_r = {}
h_r = []
for i in palabras_r:
    veces = 0
    for j in range(len(str_residente.split() )):
        if i == str_residente.split()[j]:
            veces += 1
    d_r[i] = veces/len(str_residente.split())
    h_r.append(veces/len(str_residente.split()))
d_b = {}
h_b = []
for i in palabras_b:
    veces = 0
    for j in range(len(str_balvin.split() )):
        if i == str_balvin.split()[j]:
            veces += 1
    d_b[i] = veces/len(str_balvin.split())
    h_b.append(veces/len(str_balvin.split()))
H_r=-sum(list(map(lambda x: x*math.log2(x),h_r)))
H_b=-sum(list(map(lambda x: x*math.log2(x),h_b)))
delta_H = H_r - H_b
print("El contenido de información de Shannon (ci) en bits en la canción de This is Not America de residente es de ",H_r," mientras que el ci de morado de J Balbin es ",H_b)
print("Por cual se puede afrimar que This is Not America tiene ",delta_H, "mas bits de información que morado")
