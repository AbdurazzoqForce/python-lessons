# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:38:04 2024

@author: пк
"""

#Functions


#def salom_ber():
 #   """Salom beruvchi funksiya"""
  #  print("Assalomu alaykum !")
   #salom_ber()



def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")
#def salom_ber(ism):
 #   """Foydalanuchini ismini qabil qilib
  #  unga salom beruvchi funksiya"""
   # print(f"Assalomu alaykum hurmatli {ism.title()} !")
#salom_ber('hasan')



#def yosh_hisobla(ism, tugilgan_yil):
 #   """Foydalanuvchi yoshini hisoblaydigan dastur"""
  #  print(f"{ism.title()} {2024-tugilgan_yil} yoshda")
#yosh_hisobla('olim', 1997)



#def name_year(ism, tugilgan_yil):
 #   print(f"{ism.title()}, {2024-tugilgan_yil} ")
#name_year('ali', 1981)



#def kv_kub(son):
#    print(f" {son**2} ga teng")
#kv_kub(3)



#def juftmi(son):
 #   if son%2:
  #      print(f"{son} toq son")
   # else:
    #    print(f"{son} juft son")
#juftmi(3)
#juftmi(4)



#def solishtir(x,y):
 #   if x<y:
  #      print(f"{x}<{y}")
   # elif x>y:
    #    print(f"{x}>{y}")
    #else:
     #   print(f"{x}={y}")
#solishtir(18,4)
#solishtir(3,3)



#def daraja(x, y=2):
 #   print(f"{x} ning {y}-darajasi {x**y}  ga teng")
#daraja(3,3)



def bolinish_alomatlari(son):
    for n in range(2,11):
        if not n%son:
            print(f"{son} {n} ga qoldiqsiz bolinadi")
        
            
bolinish_alomatlari(2)




























