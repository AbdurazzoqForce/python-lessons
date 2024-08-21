# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 18:33:21 2024

@author: пк
"""

#Lugat bilan ishlash


#mahsulotlar = { # Do'kondagi mahsulotlar
 #   'olma':10000,
  #  'anor':20000,
   # 'uzum':40000,
    #'anjir':25000,
    #'shaftoli':30000
    #}

#print(mahsulotlar.keys())



#bozorlik=['anor', 'uzum', 'non', 'baliq']
#for mahsulot in mahsulotlar:
 #   if mahsulot in bozorlik:
  #      print(f" {mahsulot.title()} {mahsulotlar[mahsulot]} som")



#for buyum in bozorlik:
 #   if buyum not in mahsulotlar:
  #      print(f" Iltimos dokonizga {buyum} ham olib kelin.")



#python_words={
 #   'integer':'butun son',
  #  'float':'0 lik son',
   ## 'boolean':'Mantiqiy qiymat',
    #'for': 'bir amalni qayta qayta bajarish tskili'
    #'if':'shartlarni tekshirish operatori'}
#for key, value in sorted(python_words.items()):
 #   print(f"{key.title()} -{value} ")
 

#python_words = {
 #   'integer':'Butun son',
  #  'float': "O'nlik son",
   # 'boolean':"Mantiqiy qiymat",
    #'for':"Biror amalni qayta-qayta bajarish tsikli",
    #'if':'Shartlarni tekshirish operatori'}

#for key, value in sorted(python_words.items()):
 #   print(f"{key.title()} - {value}")

#davlatlar = {
 #   "o'zbekiston":'toshkent',
  #  'aqsh':'washington d.c.',
   # 'rossiya':'moskva',
   # 'tojikiston':'dushanbe',
    #"qirg'iziston":'bishkek',
    #'qozog\'iston':'nursulton',
    #'malayziya':'kuala-lumpur',
    #'singapur':'sungapur',
    #'italiya':'rim'}

#print('Dunyo davlatlari:')
#for davlat in sorted(davlatlar):
 #   print(davlat.upper())

#print('\nDavlatlarning poytaxtlari')
#for poytaxt in sorted(davlatlar.values()):
 #   print(poytaxt.title())
    
    
   #country=input('Qaysi davlat poytahtinin bilishni istaysiz:').lower()
    #capital==davlatlar.get(country)
    ##   print('kechirasiz bizda bu haqida malumot yoq')
    #else:
     #   print(f"{country.upper()}ning poytaxti {capital.title()} shahri")


#country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
#capital = davlatlar.get(country)
#if capital==None:
 #   print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
#else:
 #   print(f"{country.upper()}ning poytaxti {capital.title()} shahri")



menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }

print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")




















































