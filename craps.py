#Goldfarb Santiago y Ferramola Joaquin

import random

n = random.randint(1, 6)
n1 = random.randint(1, 6) #Hacemos variables para despues ponerlas en el "If"
s = n + n1
s1 = s  #Hago esta nueva variable para poder usarla en el "While" que necesite q el resultado de los dados sea el mismo (Linea 29)
print(n)
print(n1)
if s == 7 or s == 11:
    print("Ganaste")

elif  s  == 3 or s == 12:
    print("Perdiste")

else:
    bucle = 0
    while bucle == 0:
        if s == 7:
            print("Perdiste")
            break
        else:
         print("su puntaje es" ,s, "Siga tirando")
         n2 = random.randint(1, 6)
         n3 = random.randint(1, 6)
         s = n2 + n3
         print(n2)
         print(n3)
    while bucle == 0:
         if s1 == s and s1 != 7:
            print("Ganaste")
            break
         else:
            print("su puntaje es" ,s, "Siga tirando")
            n2 = random.randint(1, 6)
            n3 = random.randint(1, 6)
            s = n2 + n3
            print(n2)
            print(n3)