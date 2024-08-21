# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 20:01:31 2024

@author: пк
"""


#Moslashuvchan funktsiyalar


#def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
 #   avto={'kompaniya':kompaniya,
  #        'model':model,
   #       'rang':rang,
    #      'korobka':korobka,
     #     'yili':yili,
      #    'narhi':narhi}
     #return avto
 

#avto1=avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
#avto2=avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2019, 15000)
#avtolar=[avto1, avto2]
#print('onlayn bozordagi mavjud avtomoshinalar:')




#def summa(*sonlar):
 #   """Kiritilagan sonlar yigindisini hisoblaydigan funktsiy"""
  #  yigindi=0
   # for son in sonlar:
    #    yigindi += son
    #return yigindi
    
   
#print(summa(1,2))
#print(summa(1,2,3,4,5,))
#print(summa(4,5,6,7,))

    

#def avto_info(kompaniya, model, **malumotlar):
 #   """Avto haqidagi malumotlarni lugat shaklida qaytaruvchi funksiya"""
  #  malumotlar['kompaniya']=kompaniya
   # malumotlar['model']=model
   #return malumotlar


#avto1=avto_info('GM', 'Malibu', rang='Qora', yil= 2018)



#def multiply(*sonlar):
 #   kopaytma=1
  #  for son in sonlar:
   #     kopaytma *= son
    #return kopaytma

#print (multiply(4, 5, 6))


def table(ism, familiya, **malumotlar):
      malumotlar['ism']=ism
      malumotlar['familiya']=familiya
      return malumotlar

talaba=table('ali', 'valiyev', yil=2006)
print(talaba)















