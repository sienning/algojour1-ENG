# ENG Léna
# Selection sort
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

def selection(liste):
    global nbComp
    global nbIteration
    tmp = liste
    length = len(liste)
    res = []
    while len(res) < length:
        nbIteration+= 1
        nbComp+=1
        minim = min(tmp)
        res.append(minim)
        tmp.remove(minim)
    return res


convert(sys.argv[1])
res = selection(listeDep)

print("Série : ", sys.argv[1])
print("Résultat : ", res)
print("Nb de comparaisons : ", nbComp)
print("Nb d'itérations : ", nbIteration)
print("Temps (sec) : ", (time.time() - start_time))