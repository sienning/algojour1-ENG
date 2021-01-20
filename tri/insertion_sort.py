# ENG Léna
# Insertion sort
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

def insertion(liste):
    tmp = liste
    length = len(tmp)
    res = [tmp[0]]
    t = 1
    global nbIteration
    global nbComp
    if length <= 1: return tmp
    else:
        while t < length:
            
            nbIteration+=1
            i = len(res)-1 # longueur de res -1
            x = res[len(res)-1] # Dernier élément de res
            y = tmp[t] # élément courant de tmp
            if x > y: # si dernier élément de res > élt courant de tmp
                nbComp+=1
                while i >= 0:
                    nbIteration+=1
                    if y > res[i]:
                        nbComp+=1
                        res.insert(i+1, y)
                        break
                    else:
                        if i == 0:
                            nbComp+=1
                            res.insert(0, y)
                    i = i-1
            else: # Si nb supérieur on le met à la fin
                nbComp+=1
                res.append(tmp[t])
            t=t+1
    
    return res


convert(sys.argv[1])
res = insertion(listeDep)

print("Série : ", sys.argv[1])
print("Résultat : ", res)
print("Nb de comparaisons : ", nbComp)
print("Nb d'itérations : ", nbIteration)
print("Temps (sec) : ", (time.time() - start_time))