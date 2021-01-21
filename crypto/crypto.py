import sys
import math

msg = ""
key = ""
nCol = 0
nLin = 0

def start(m, k, encrypt):
    global msg
    global key

    if len(m) <= 0 or len(k) <= 0 or encrypt > 1 or encrypt < 0:
        print("python3 crypto.py <String : message> <String : key> <Integer : encrypt>")
    elif encrypt == 0:
        msg = m
        key = k
        matriceCle = make_key_matrix(k)
        matriceMsg = make_msg_matrix(m)
        print("matrice clé :", matriceCle)
        print("\nmatrice message :", matriceMsg, "\n")
        calc_matrix_res(matriceCle, matriceMsg)


def make_key_matrix(k): # On crée la matrice clé
    length = len(k)
    global nCol
    carre = int(math.sqrt(length))
    matriceCle = []
    ligne = []
    l = 0
    # On compte le nombre de colonne de la matrice clé qui doit être une matrice carrée
    while int(math.pow(carre, 2)) < length: carre+=1 
    nCol = carre
    nCarre = int(math.pow(carre, 2))
    for c in range(nCarre+1): # On itère le nombre de case dans la matrice carrée + 1
        if l > carre-1: # Si la ligne est terminée
            matriceCle.append(ligne) # On l'ajoute à la matrice clé
            ligne = [] # On vide la ligne
            l = 0 # On reprend l'itération de la ligne à 0
        if c < length: ligne.append(ord(k[c])) # Si la chaîne de caractères du message n'est pas terminée, on ajoute le code ascii dans la ligne
        else: ligne.append(0) # Sinon non ajoute un 0
        l+=1
    return matriceCle

def make_msg_matrix(m): # On crée la matrice clé
    length = len(m)
    global nCol # NB de colonnes imposé par la matrice clé
    global nLin # NB de ligne imposé par la matrice msg
    matriceMsg = []
    ligne = []
    l = 0
    nCases = int(length/nCol)
    while int(nCases * nCol) < length: nCases+=1
    nLin = nCases
    nCases = int(nCases * nCol)
    for c in range(nCases+1): 
        if l > nCol-1:
            matriceMsg.append(ligne)
            ligne = []
            l = 0
        if c < length: ligne.append(ord(m[c]))
        else: ligne.append(0)
        l+=1
    return matriceMsg

def calc_matrix_res(matriceCle, matriceMsg):
    global nCol
    global nLin

    for lineM in matriceMsg:
        for m in range(len(lineM)):
            for lineC in matriceCle:
                print("LineM[m] :", lineM[m])
                print("LineC[m] :", lineC[m])



start(sys.argv[1], sys.argv[2], int(sys.argv[3]))
