# ENG Léna
# Bubble sort
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

def bulle(liste):
    tmp = liste
    i = 0
    used = False
    if len(liste) <= 1:
        return tmp
    else:
        global nbIteration
        global nbComp
        nbIteration+=1

        while i < len(tmp)-1:
            nbIteration+=1
            if tmp[i] > tmp[i+1]:
                nbComp+=1
                used = True
                tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
            i = i+1
        if used:
            return bulle(tmp)
        else:
            return tmp

convert(sys.argv[1])
res = bulle(listeDep)


print("Série : ", sys.argv[1])
print("Résultat : ", res)
print("Nb de comparaisons : ", nbComp)
print("Nb d'itérations : ", nbIteration)
print("Temps (sec) : ", (time.time() - start_time))