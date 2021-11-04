# 10 Dars if-else shartlari va tarmoklanishi   sana 31.10.2021


# Mualif Mamadjonov Ahrorbek  



# TARMOQLANISH

avtolar = [ ' tesla' , ' bmw ' , ' audi' , ' volvo ' , ' nissan']
for avto in avtolar :     
    #print(avto.title())
    if avto == ' bmw ':
         print(avto.upper())
    else:
         print(avto.title())
    
ism = input( ' Ismingiz nima ? \n>> ')
if ism.lower() != 'ahad':
    print(f"Uzr , {ism.title()} biz Firibgarni kutyamiz !")
else :
    print("Salom Ahad !" )
    
javob = float(input(' 9*9 nechiga teng ? \n>>> '))
if javob != 81:
    print(" Javob xato ! ")
    
yosh = int(input( " Assolomu Alaykum , yoshingiz nechida ? "))
if yosh >= 18:
    print(' Xush kelibsiz 😊 !')
else:       
      print("Kirish mumkun emas 🚷 ! ")
     
login = input(' Yangi login tanlen ')
if len(login) <=5 :
 print(' Login 5 harifdan koproq bolishi shart ! ')
 
yil = int(input('Tugilgan yiligizni kiriting : '))
if 2021-yil<18:
    print(f" Yoshingiz {2021-yil} da ekan ! ")
    print(" Kirish mumkun emas !")
else:
    print(" Xush kelibsiz !")
    
yosh = int(input(' Yoshingiz nechida :'))
if yosh >65: print(' Siz COVID -19 riskda ekansiz !')
    
     
     
        