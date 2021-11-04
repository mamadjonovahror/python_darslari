#11 Dars mavzu : if else funksiyalari bilan ishlash 

# Mualif Mamadjonov Ahror sana 01.11.2021

yosh = int((input(' Yoshingiz nechida ?' )))
if yosh <= 4:
    narx = 1000
elif yosh <= 12 :
    narx = 15000
elif yosh <= 18 :
    narx = 20000
else : narx = 25000

print(f" Sizga kirish , {narx} so\'m ")
    
     



narh = 15000
choy = True
salat = True

if choy and salat :
    narh = narh + 10000
elif choy or salat :
    narh = narh + 5000
    print (f" Jammi {narh} so'm " )
menu = [ 'manti', 'somsa' , 'shashlik' , 'qozon qabob' ]
ovqat = input( ' Nima ovqat yiysiz ? ')
if ovqat.lower()in menu:
    print ( ' Buyurtmangiz qabul qilindi ! .')
else:
    print (' Afsuski bizda bunaqa taom mavjud emas !.')
        
raqamlar =[ 25, 35, 45, 85, 25, 36, 74, -45, -465, 74 ]    