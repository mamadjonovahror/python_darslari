# Buyerda men dasturlash asoslari ni hammasini yozib bormoqchiman bu yerda hamma organgan narsalarim mavjud
# 1-46 mavzuni hammalari bor . Buni men 31.10.2021 yil yozishni boshladim 
# mening ismim Mamadjonov Ahror dasturlashni shu yerdan organishni boshladim !
# Menga kerak bolgan narsalar mohirdev.uz sayiti Ustozim Anvar aka !
# Qani boshladik unda !!!!

#01 Dars print funksiyasi bilan tanishamiz  

print(' Hello Uzbekistan ! . Mening ismim Ahrorbek , men 2001 yilda \nAndijon viloyati Jalaquq tumanida tugilganman ! . ')

#02 Dars 

print(""" Men 16.09.2001 yilda Jalaquduq tumanida ,
tugilganman , va 7 yoshimda 3 - maktabga oqishga borganman. """)

print(" 1- Sentabirda 1 - B sinifiga qabul qilindim , unda kegin esa , \nfutbol sport turi bojicha , shug'ilanishni boshlanib ! ")

print(' Futbol sport turi , boyicha shug\'ilanishi boshladim !. ')

#03 Dars 


print(2+8*56)

print(' Bu raqamlar  esa shunchaki yozilda ! ')

print(" To'qizni kvadirati " , 9**2 , ' boladi ! .')

#04 Dars 

ism = (' Ahrorbek')

yosh = (21)

print(' Deme ,  meni ismim ', ism , ' , yoshim ' , yosh ,' da !')


print ( ' Kelilar endi sizlarga matematika fanidan , qande oq\'iganimni ko\'rsatib beraman ! . ')

radius = 25

pi = 3.14

aylanani_yuzi = pi * radius**2

print(" Radius " , radius , " ga teng aylanini yuzi : = " , aylanani_yuzi )

#05 Dars Matn bilan ishlash ( String ) unicode-table.com


print(' Sizlarga xozir zo\'r narsa ko\'rsataman 🔥 ! ')  # Bu yerda men smaylik qoydim uni unicode sayitidan oldim unicode-table.com

ism = (' Ahror ')
familiya = ( ' Mamadjonov ')

print(familiya + ' ' + ism ) # ' ' shu funksiya orqali boshlik boldi buyerda

ism = ' Ahror '
familiya = ' Mamadjonov '
ism_sharif = f"{familiya} {ism}" # f" uslubi buyerda
print(ism_sharif)

ism = ' Abdulaziz '
familiya = ' Sultonov '
print(f"Salom mening ismim {ism}.Familiyam {familiya} ! "  )


# Maxsus belgilar 


print( ' Hello , Andijon ! .')
print( ' Hello , \nAndijon ! .')
print( ' Hello , \tAndijon ! .')


# String Metodlar 

ism = " Xo'ja "
familiya = ' Qodirov '
ism_sharif= f" {familiya} {ism}"
print(ism_sharif.upper() )
print(ism_sharif.lower())
print(ism_sharif.title())
print(ism_sharif.capitalize())

ism = input (" ismingiz nima ? ") # Bu menga eng yoqan funksiya 


print(' Assolomu alaykum ! ' , ism )

ism = input( ' Ismingiz nima ? \n>>')
print(' Assolomu Alaylum ! ' , ism.title()) # Agar siz buyerda ismingizni bosh xarifini kichgina harifda kiritsez katta qilib beradi 

#06 Dars Sonlar bilan ishlash 

a = 5
b = 7.7
temp = 36.7

type(temp)   # Bu funksiya malumotni turini korsatib beradi 

aholi_soni = 7_256_123_632 #Agar malumot uzun bolsa biz buni 7_125_2568 shundey kiritseg boladi 

print( ' Aholi soni : = ' , aholi_soni )
   
#09 Dars




mehmonlar_1 = [ ' Ali ', '  Vali ' , '  Husan ', '  Hasan ', ' Olim' ]
print (' Salom ' , mehmonlar_1 [0])
 
for mehmon in mehmonlar_1 : # for 
    print (' Salom ' , mehmon)
    print( ' Hayr !' , mehmon)
    
mehmonlar = [ ' Qodirov ' ,' Dolimov ' , ' Mamadjonov ' ,' Shakirov ' ]
for oilalar in mehmonlar :
    print(f"Hurmatli {oilalar} , sizni 15 nayabr kuniga nahorga oshga 🍛 taklif qilamiz !\n")
    print('Hurmat bilan Davlatov lar oilasi .\n')
    
raqamlar = list(range(1,11))
for raq in raqamlar:
    print(f" {raq} ning kvadirati , {raq**2} ga teng ! ")



sonlar = list(range(11))

sonlarni_kvadirati = []

for son in sonlar:
          sonlarni_kvadirati.append(son**2)

print(sonlar)
print (sonlarni_kvadirati)

dostlar = []
print(" 5 eng yaqin dostingiz kim ? ")
for n in range (5):
    dostlar.append(input(f"{n+1}-do\'stigizni ismini kiriting : "))
print(dostlar)








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






