# ENG Léna
# Merge sort
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

def merge(listeA, listeB):
    res = []
    i, j = 0,0
    global nbIteration
    global nbComp
    while i < len(listeA) and j < len(listeB):
        nbIteration+=1
        if listeA[i] < listeB[j]:
            nbComp+=1
            res.append(listeA[i])
            i+=1
        else:
            res.append(listeB[j])
            j+=1
    if i == len(listeA): # Si tous les éléments de A sont dans res, il doit rester des éléments dans B
        nbComp+=1
        res.extend(listeB[j:]) # On les ajoute à res
    else : 
        res.extend(listeA[i:])
    return res

def tri_fusion(liste):
    global nbIteration
    global nbComp
    length = len(liste)
    if length <= 1:
        nbComp+=1
        return liste
    else:
        # Sépare la liste de manière récursive
        mid = int(length/2)
        nbIteration+=1
        gauche, droite = tri_fusion(liste[:mid]), tri_fusion(liste[mid:])
        return merge(gauche, droite)
    
convert(sys.argv[1])
res = tri_fusion(listeDep)

print("Série : ", sys.argv[1])
print("Résultat : ", res)
print("Nb de comparaisons : ", nbComp)
print("Nb d'itérations : ", nbIteration)
print("Temps (sec) : ", (time.time() - start_time))