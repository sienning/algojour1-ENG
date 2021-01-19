from hashlib import sha256
from datetime import datetime
import random
import sys

on = True
blockchain = []

def calculateHash(block):
        """
        fct qui permet de créer un hashcode courant
        """
        bloc = str(block.index) + str(block.previousHash) + str(block.timestamp) + str(block.data) + str(block.nonce)
        return(sha256(bloc.encode('utf-8')).hexdigest())

def create_blockchain(nbBlocks, nbZeros):
    i = 1
    resBC = []
    if nbBlocks > 0:
        data = make_random()
        b = Block(0, None, data)
        b.make_hashcode(nbZeros)
        resBC.append(b)
        while i < nbBlocks:
            data = make_random()
            b = Block(i, resBC[i-1].currentHash, data)
            b.make_hashcode(nbZeros)
            resBC.append(b)
            i+=1
        return resBC

def make_random(): # Crée une chaîne de 10 caractères aléatoires
    random_string = ''
    for _ in range(10):
        # Considering only upper and lowercase letters
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        # Convert to lowercase if the flip bit is on
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
        # Keep appending random characters using chr(x)
        random_string += (chr(random_integer))
    return random_string

class Block:
    def __init__(self, index, previousHash, data):
        self.index = index
        self.previousHash = previousHash  # Hashcode du bloc précédent
        self.data = data  # Données ou transaction
        self.nonce = 0  # Preuve de travail : s'incrémente à chaque tentative
        self.timestamp = datetime.now()  # Date de sa création
        self.currentHash = calculateHash(self)  # Hashcode courant

    def make_hashcode(self, nbZeros):
        """
        Fonction qui crée un nouveau hashcode conforme (avec un nombre de 0 imposé)
        """
        debutHash = calculateHash(self)[:2]
        modeleHash = ""
        i = 0
        if nbZeros > 0:
            while i < nbZeros:
                modeleHash+= "0"
                i+=1
            while debutHash != modeleHash:
                self.nonce+=1
                debutHash = calculateHash(self)[:nbZeros]
            self.currentHash = calculateHash(self)


class Blockchain:
    def __init__(self, nBlocks, nbZeros):
        self.arrayBlocks = create_blockchain(nBlocks, nbZeros)

def new_blockchain():
    global blockchain
    nbBlocks = int(input("Create a new blockchain\n\nNumber of blocks (int) : "))
    nbZeros = int(input("\nEnter number of 0 in hashcode (int), 0 < x < 5 (excluded) : "))
    if nbZeros > 5 or nbZeros < 0  :
        while nbZeros > 5 or nbZeros < 0  :
            nbZeros = int(input("Warning ! Enter an integer between 0 and 5 (excluded) : "))
    blockchain = Blockchain(nbBlocks, nbZeros)

def start():
    global on
    while on :
        print("Menu Blockchain :\n")
        print("* New blockchain : b")
        print("* View blockchain : v")
        print("* Add block to a blockchain : a")
        print("* Quit : q")

        response = input("\Choice : ")
        
        if response == 'q':
            print("Bye")
            on = False
        elif response == 'b':
            new_blockchain()
        elif response == 'v':
            print("En construction")
        elif response == 'a':
            print("En construction")
        else: 
            print("Wrong entry")
        
start()