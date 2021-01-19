# ENG Léna
# Quick sort
import sys
import time

start_time = time.time()
listeDep = []
nbComp = 0
nbIteration = 0

def is_int(value):
  try:
    int(value)
    return True
  except:
    return False

def convert(str):
    liste = str.split(';')
    for i in liste:
        if is_int(i):
            listeDep.append(int(i))
        else:
            listeDep.append(float(i))

def quick(liste):
    global nbIteration
    global nbComp
    length = len(liste)
    if length <= 1:
        nbComp+=1
        return liste
    else:
        nbIteration+=1
        nbComp+=1
        pivot = liste.pop()
        gauche = []
        droite = []
        for i in liste:
            nbIteration+=1
            if i > pivot:
                nbComp+=1
                droite.append(i)
            else:
                nbComp+=1
                gauche.append(i)
        return quick(gauche) + [pivot] + quick(droite) # Recursive

convert(sys.argv[1])
res = quick(listeDep)

print("\nSérie : ", sys.argv[1])
print("Résultat : ", res)
print("Nb de comparaisons : ", nbComp)
print("Nb d'itérations : ", nbIteration)
print("Temps (sec) : ", (time.time() - start_time))