#Teoría 1
""" Primeras notas
"""

# Variables y operadores
num1 = 1
num2 = 2
num3 = num1 + num2
print(num3)

bool1 = True
bool2 = False
if (bool1):
    #!bool2
    bool2 = not bool2

bool1 = False

print(bool2)

# Formato de los strings
cancionMiBarba1 = "Mi {0} tiene tres {1}, tres {1} tiene mi {0}, si no tuviera tres {1}, ya no sería una {0}" .format("barba", "pelos")
print(cancionMiBarba1)

cancionMiBarba2 = "Mi {barba} tiene tres {pelos}, tres {pelos} tiene mi {barba}, si no tuviera tres {pelos}, ya no sería una {barba}" .format(barba="barba", pelos="pelos")
print(cancionMiBarba2)

#literales
barba = "barba"
pelos = "pelos"
cancionMiBarba3 = f"Mi {barba} tiene tres {pelos}, tres {pelos} tiene mi {barba}, si no tuviera tres {pelos}, ya no sería una {barba}"
print(cancionMiBarba3)

# Listas
lista1 = []
print(len(lista1)) #no hay length