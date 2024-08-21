# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:22:23 2024

@author: пк
"""

#Dictionary



#en_uz={'apple': 'olma', 'apricot': 'orik', 'banana': 'banan'}
#print(en_uz)


#mevalar={'olma':10000, 'tarvuz':8000, 'qovun':7000}
#print(f"Olma narhi {mevalar['olma']} som")


#talaba_0={'ism':'Murot Olimov', 'yosh':18, 't_yil':2006}
#print(f"{talaba_0['ism].title()}, {talaba_0['t_yil']}-yilda tugilgan, {talaba_0['yosh']} yoshda")
#talaba_0['kurs']=3
#talaba_0['fakultet']='informatika'
#talaba_0['ism']='Abdulloh'
#print(talaba_0)         


#talaba_1={}
#talaba_1['ism']='qobil rosulov'
#talaba_1['yosh']=19
#talaba_1['kurs']=2
#print(talaba_1)
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']} kursda   ")


#talaba_0={'ism':'Murot Olimov', 'yosh':18, 't_yil':2006}
#del talaba_0['yosh']
#print(talaba_0)


#telefonlar = {
 #   'ali':'iphone x',
  #  'vali':'galaxy s9',
   # 'olim':'mi 10 pro',
    #'orif':'nokia 3310'
    #}

#phone = telefonlar.get('hasan','Bunday ism mavjud emas')
#print(phone)


#otam={'ism ': 'Davlatbek', 't_yil': 1979, 't_shahri':'Andijon',}
#print(f"Otamning ismi {otam['ism']}, {otam['t_uil']} uilda , {otam['t_shahri']}  shahrida tugilgan  ")

#otam = {'ismi':'mavlutdin', 'tyil':1954,'viloyat':'samarqand'}
#tyil = otam['tyil']
#vil = otam['viloyat']
#print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")

#taom={'davron':'lagmon', 'dovud':'shorva', 'onam':'monti', 'dadam':'mastava'}
#taomlar = {
 #   'ali':'osh',
  #  'vali':'shashlik',
   # 'hasan':"lag'mon",
    #'husan':"mastava",
    #'olim':"somsa"
    #}

#taom = taomlar['ali']
#print(f"Alining sevimli taomi {taom}")
  

python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
# print(python_izohli_lugati['tuple'])

kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))






















