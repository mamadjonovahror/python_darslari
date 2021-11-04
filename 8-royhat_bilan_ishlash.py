# 08 Dars Ro'yhat bilan ishlash sana 30.10.2021

#    Mualif Mamadjonov Ahror 

# Tartiblash

cars = [ 'volvo' , ' mersedez benz ', ' bmw' , ' audi' , ' tesla']

cars.sort()


sonlar = [ 25, 35 , 65, 199 , 45 , -15, 78 , -14 , 9.3 ]


sonlar.sort()   #Bu funksiya 0 ....10 oldidan orqaga tahlab beradi


sonlar.sort(reverse=True)   # Bu esa 10.....0 orqadan olnigda tahlab beradi


print(sonlar)

cars.reverse()   # Bu funksiys malumotlarni aylantirib qoyadi

len(cars)   # Bu funksiya royhatni uzunligini olchedi 
 
sonlar = list (range (0 , 10))    # Malum bir oralikdegi sonlarni qaytaradi 

list(range(0 , 11 ))

toq_sonlar = list(range(1 , 20 , 2))

shuft_sonlar = list(range(2 , 20 , 2))

max_qiymat = max( shuft_sonlar) # max MAksimal yuqori sonlarni chikarib beradi 



narxlar = [12000, 25000, 25680 ,63000 , 7500 , 45600,  ]

arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)

print(' Eng arzno mahsulot' , arzon , ' eng qimmat mahsulot' , qimmat ,' hammasi bolib' , jami  )

print(cars [0:3])

my_cars = cars

cars.remove('volvo')



#Amaliyot

raqamlar = [ 12 , 25 , 3265 , 487 , 1609 , -254 , 745 , 9654 , -1 ]

dostlarim = [ ' abdulaziz ' , ' zakariyo ' , " xo'ja " , ' emil ' , ' begzod ']

len(raqamlar) #matini uzunligini aniqledi

print(sorted(dostlarim))

sorted(raqamlar)     # bu tahlab beradi 

raqamlar.sort(reverse = True)    # Bu esa orqadan olndigda tahlab beradi

print(sorted(dostlarim))







             


