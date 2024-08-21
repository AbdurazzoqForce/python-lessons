# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:41:17 2024

@author: пк
"""



#Funksiyalarga royxat uxatish



#def bahola(ismlar):
 #   baholar={}
  #  while ismlar:
   #     ism=ismlar.pop()
    #    baho=input(f"Talaba {ism.title()}ning bahosini kiriting:")
     #   baholar[ism]=int(baho)
    #return baholar
        

#talabalar=['ali', 'vali','hasan','husan']
#baholar=bahola(talabalar)
#print(baholar)



#def katta_harf(matnlar):
 #   for i in range(len(matnlar)):
  #      matnlar[i]=matnlar[i].title()
        
#ismlar=['ali', 'vali','hasan','husan']
#katta_harf(ismlar)
#print(ismlar)        




talabalar=['ali','vali','hasan','husan']

def bahola(ismlar):
    baholar={}
    for ism in ismlar:
        baho=input(f"Talaba {ism.title()}ning bahosini kiriting:")
        baholar[ism]=baho
    return baholar

baholar=bahola(talabalar)
print(baholar)
print(talabalar)

































































