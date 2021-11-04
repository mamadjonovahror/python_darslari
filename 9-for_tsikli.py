# 09 dars for tsikli bilan tanishamiz sana 37.10.2021
#Mualif Mamadjonov Ahrorbek 

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





