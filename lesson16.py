# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:08:45 2024

@author: пк
"""

#while va royhatlar


#print("Yaqin dostlaringizni royhatini tuzamiz.")
#ismlar=[]
#n=1
#while True:
 #   savol=f"{n}-dostlaringizni ismini kiriting:"
  #  ism=input(savol)
   # ismlar.append(ism)
    #takrorlash=input("Yana ism qoshasizmi? (ha/yoq)")
    #n+=1
    #if takrorlash!="ha":
     #   break
    #print("Dostlaringiz royhati:")
    #for ism in ismlar:
     #   print(ism.title())
    

#print("Do'stlaringiz yoshini saqlaymiz.")
#dostlar = {}
#ishora = True
#while ishora:
 #   ism = input("Do'stingiz ismini kiriting: ")
  #  yosh = input(f"{ism.title()}ning yoshini kiriting: ")
   # dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
   # javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
   # if javob == "yo'q":
    #    ishora = False

#for ism, yosh in dostlar.items():
 #   print(f"{ism.title()} {yosh} yoshda")


#cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
#while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
 #   cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
#print(cars)


#cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
#while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
 #   cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
#print(cars)


#talabalar = ['hasan', 'husan', 'olim', 'botir']
#baholangan_talabalar = {}
#while talabalar:
 #   talaba = talabalar.pop()
  #  baho = input(f"{talaba.title()}ning bahosini kiriting: ")
   # print(f"{talaba.title()} baholandi")
    #baholangan_talabalar[talaba] = baho


#savat=[]
#while True:
 #   mahsulot=input("Savatga mahsulot qoshining:")
  #  savat.append(mahsulot)
   # javob=input("Yana amhsulot qoshasizmi (ha/yoq)")
    #if javob !='ha':
    # break

 
#mahsulotlar={}
#while True:
 #   mahsulot=input(f"Mahsulot nomini kiriting:")
  #  narh=input(f"{mahsulot.title()} ning narhini kiriting:")
   # mahsulotlar[mahsulot]=narh
   # javob=input("Yana mahsulot qoshasizmi (ha/yoq)")
    #if javob !='ha':
     #   break


buyurutmalar=['olma', 'anjir', 'uzmum', 'qovun']
mahsulotlar={'olma':2000, 
             'shaftoli':3000, 
             'tarvuz':35000,
             'uzum':4000}
while buyurutmalar:
    buyurutma=buyurutmalar.pop()
    if buyurutma in mahsulotlar.keys():
        narh=mahsulotlar[buyurutma]
        print(f"{buyurutma.title()} - {narh} som")
    else:
        print(f"Bizda {buyurutma} yoq")















