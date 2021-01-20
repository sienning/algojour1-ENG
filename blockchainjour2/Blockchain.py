from hashlib import sha256
from datetime import datetime
import random
import time
import os

on = True
blockchain = []
nZeros = 0

def calculateHash(block):
        """
        fct qui permet de créer un hashcode courant
        """
        bloc = str(block.index) + str(block.previousHash) + str(block.timestamp) + str(block.data) + str(block.nonce)
        return(sha256(bloc.encode('utf-8')).hexdigest())

def create_blockchain(nbBlocks, nbZeros):
    i = 1
    resBC = []
    global nZeros
    nZeros = nbZeros
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

class OldBlock:
    def __init__(self, index, previousHash, data, nonce, timestamp, currentHash):
        self.index = index
        self.previousHash = previousHash  # Hashcode du bloc précédent
        self.data = data  # Données ou transaction
        self.nonce = nonce  # Preuve de travail : s'incrémente à chaque tentative
        self.timestamp = timestamp  # Date de sa création
        self.currentHash = currentHash  # Hashcode courant

class Blockchain:
    def __init__(self, nBlocks, nbZeros):
        self.arrayBlocks = create_blockchain(nBlocks, nbZeros)

def new_blockchain():
    global blockchain
    length = len(blockchain)
    os.system('clear')

    print("\nCreate a new blockchain :")
    print("(random data) \n\n")
    if length > 0:
        response = input("If you create a new blockchain, the previous one will be deleted.\nContinue ? (Y/N) : ")
        if response == 'Y' or response == 'y':
            blockchain = []
            f= open("saved_blockchain.txt","w+")
            f.write('')
            f.close()
            blockchain = generate_blockchain()
            print("\n--- Blockchain created ! ---")
            time.sleep(1)
        elif response == 'N' or response == 'n':
            print("\n--- Going back to menu ---")
            time.sleep(1)
        else : 
            response = input("Continue ? (Y/N) : ")
    else:
        blockchain = generate_blockchain()
        print("\n--- Blockchain created ! ---")
        time.sleep(1)

def generate_blockchain():
    nbBlocks = int(input("Number of blocks (int) : "))
    nbZeros = int(input("\nEnter number x of 0 in hashcode (int), 0 < x < 5 (excluded) : "))
    if nbZeros > 5 or nbZeros < 0  :
        while nbZeros > 5 or nbZeros < 0  :
            nbZeros = int(input("Warning ! Enter an integer between 0 and 5 (excluded) : "))
    bc = Blockchain(nbBlocks, nbZeros)
    return bc.arrayBlocks

def view_blockchain():
    global blockchain
    i = 0
    quit = False
    length = len(blockchain)
    res = ""
    os.system('clear')

    while quit == False:
        print("\nView blockchain : \n")
        while i < length:
            print("\nBlock #", blockchain[i].index +1 )
            time.sleep(0.05)
            print("[ \n     Index : ", blockchain[i].index)
            time.sleep(0.05)
            print("     Previous Hashcode : ", blockchain[i].previousHash)
            time.sleep(0.05)
            print("     Timestamp : ", blockchain[i].timestamp)
            time.sleep(0.05)
            print("     Nonce : ", blockchain[i].nonce)
            time.sleep(0.05)
            print("     Data : ", blockchain[i].data)
            time.sleep(0.05)
            print("     Current Hashcode : ", blockchain[i].currentHash)
            time.sleep(0.05)
            print("]")
            i+=1
        res = input("Exit (q) : ")
        if res == 'q' or res == 'Q':
            quit = True

def view_one_block(block):
    print("\nBlock #", block.index+1)
    time.sleep(0.05)
    print("[ \n     Index : ", block.index)
    time.sleep(0.05)
    print("     Previous Hashcode : ", block.previousHash)
    time.sleep(0.05)
    print("     Timestamp : ", block.timestamp)
    time.sleep(0.05)
    print("     Nonce : ", block.nonce)
    time.sleep(0.05)
    print("     Data : ", block.data)
    time.sleep(0.05)
    print("     Current Hashcode : ", block.currentHash)
    time.sleep(0.05)
    print("]")

def add_block():
    global blockchain
    global nZeros
    length = len(blockchain) - 1
    os.system('clear')
    print("nZeros", nZeros)
    print("Add a block :\n\n")
    response = input("Do you need random data ? (Y/N) : ")
    if response == "Y" or response == "y":
        data = make_random()
        b = Block(blockchain[length].index+1, blockchain[length].currentHash, data)
        b.make_hashcode(nZeros)
        blockchain.append(b)
    elif response == "N" or response == "n":
        is_data = False
        while is_data == False:
            data = input("Enter your data : ")
            print("Is this your data ? (Y/N) : ", data)
            res_data = input()
            if res_data == "Y" or res_data == "y": # Si la data convient
                b = Block(blockchain[length].index+1, blockchain[length].currentHash, data)
                b.make_hashcode(nZeros)
                blockchain.append(b)
                is_data = True
            elif res_data == "N" or res_data == "n": # Si la data ne convient pas
                out = input("Do you want random data ? (Y/N) : ")
                if out == "Y" or out == "y": # Possibilité de changer d'avis et d'ajouter une data aléatoire
                    data = make_random()
                    b = Block(blockchain[length].index+1, blockchain[length].currentHash, data)
                    b.make_hashcode(nZeros)
                    blockchain.append(b)
                    is_data = True
                else: is_data = False
            else: is_data = False
    print("\n--- Block created ---")
    time.sleep(1)

def delete_blockchain():
    os.system('clear')
    global blockchain
    
    print("Deleting your blockchain :\n\n")
    response = input("Are you sure you want to delete your blockchain ?\nYou will loose everything you saved (Y/N) : ")
    if response == "y" or response == "Y":
        time.sleep(0.9)
        blockchain = []
        f= open("saved_blockchain.txt","w+")
        f.write('')
        f.close()
        print("\n--- Blockchain deleted ---")
        time.sleep(1)
    elif response == "n" or response == "N":
        print("\n--- Going back to menu ---")
        time.sleep(1)
    else:
        response = input("Are you sure you want to delete your blockchain ? (Y/N) : ")

def add_retrieve(index, previousHash, data, nonce, timestamp, currentHash):
    global blockchain
    t = timestamp[:10]+" "+timestamp[11:26]
    new_timestamp = datetime.strptime(t, '%Y-%m-%d %H:%M:%S.%f')
    b = OldBlock(index, previousHash, data, nonce, new_timestamp, currentHash)
    blockchain.append(b)
    
def retrieve_blockchain():
    file_bc  = open("saved_blockchain.txt", 'r')
    global nZeros
    current_block = "index : 0"
    index_block = ""

    index = 0
    previousHash = ""
    data = ""
    nonce = 0
    timestamp = ""
    currentHash = ""

    for line in file_bc:
        if line[:6] == "nZeros": # Première ligne
            nZeros = int(line[9:])
        elif line[:8] == "index : " : # A chaque nouveau bloc
            index_block = line
            index = int(line[8:])
        
        if current_block == index_block:
            if line[:15] == "previousHash : ":
                previousHash = str(line[15:])
            if line[:7] == "data : ":
                data = str(line[7:])
            if line[:8] == "nonce : ":
                nonce = int(line[8:])
            if line[:12] == "timestamp : ":
                timestamp = line[12:]
            if line[:14] == "currentHash : ":
                currentHash = str(line[14:])
                add_retrieve(index, previousHash.strip('\n'), data.strip('\n'), nonce, timestamp, currentHash.strip('\n'))
        else:
            current_block = index_block
    file_bc.close

def save_blockchain():
    global blockchain
    global nZeros

    length = len(blockchain)
    
    os.system('clear')
    print("Saving your blockchain...\n\n")
    time.sleep(0.9)

    f= open("saved_blockchain.txt","w+")
    f.write('nZeros : %d\r\n' % nZeros)
    for i in range(length):
        f.write("\nindex : %d\r\n" % blockchain[i].index)
        f.write("previousHash : %s\r\n" % blockchain[i].previousHash)
        f.write("data : %s\r\n" % blockchain[i].data)
        f.write("nonce : %s\r\n" % blockchain[i].nonce)
        f.write("timestamp : " + str(blockchain[i].timestamp) + "\n")
        f.write("currentHash : " + blockchain[i].currentHash + "\n")
    f.close()
    print("\n--- Blockchain saved ---")
    time.sleep(1)

def check_block():
    global blockchain
    length = len(blockchain)
    check = False
    quit = False

    os.system('clear')
    print("Check one block : \n\n")
    print("You have %d blocks in your blockchain." % length)
    response = int(input("Which one do you want to check ? : "))

    while check == False:
        if response <= 0 or response > length:
            response = int(input("--- Wrong Entry ---\n\nWhich one do you want to check ? : "))
        else:
            while quit == False:
                os.system('clear')
                print("This is your block", response)
                view_one_block(blockchain[response-1])
                res = input("Exit (q) : ")
                if res == 'q' or res == 'Q':
                    quit = True
            check = True

def remove_block():
    global blockchain
    length = len(blockchain)
    remove = False
    while remove == False:
        os.system('clear')
        print("Remove one block : \n\n")
        print("You have %d blocks in your blockchain." % length)
        response = int(input("Which one do you want to remove ? : "))
        if response <= 0 or response > length:
            response = int(input("--- Wrong Entry ---\n\nWhich one do you want to remove ? : "))
        else:
            os.system('clear')
            print("Do you want to remove this block %d ?" % response)
            view_one_block(blockchain[response-1])
            res = input("Yes (Y) / No (N) : ")
            if res == 'Y' or res == 'y':
                print("supprimer bloc")
                time.sleep(1)
                remove = True
            elif res == 'N' or res == 'n':
                print("Changer de bloc")
                remove = False

def start():
    """
    Fonction Start
    Démarre le programme et ne s'arrête pas tant que l'entrée est 'q'
    Affiche le menu
    c : Créer une nouvelle blockchain
    v : Voir la blockchain créée
    a : Ajouter un bloc à la blockchain
    b : Vérifier un bloc spécifique
    r : Retirer un bloc de la blockchain
    s : Sauvegarde la blockchain créée
    d : Supprime la blockchain et sa sauvegarde
    """
    global on
    global blockchain
    
    file_bc = open("saved_blockchain.txt", 'r')
    file_length = len(file_bc.read())
    file_bc.close
    if file_length > 0:
        retrieve_blockchain() # Si sauvegarde existante : on réattribue les données

    while on :
        file_bc = open("saved_blockchain.txt", 'r')
        file_length = len(file_bc.read())
        file_bc.close

        os.system('clear')
        print("\n*** Menu Blockchain ***\n")
        print("* Create new blockchain : c")
        print("* View your blockchain : v")
        print("* Add block to your blockchain : a")
        print("* Check one block from your blockchain : b")
        # print("* Remove one block from your blockchain : r")
        print("* Save your blockchain : s")
        print("* Delete your blockchain : d")
        print("\n* Quit : q")
        if file_length > 0: print("(You have already saved a blockchain)")
        response = input("\nChoice : ")

        if response == 'q':
            print("Bye")
            on = False
        elif response == 'c': new_blockchain() # Create new blockchain 

        elif response == 'v': # View your blockchain
            if len(blockchain) > 0: view_blockchain()
            else:
                print("\n\n--- First create a blockchain. ---\n")
                time.sleep(1)

        elif response == 'a': # Add block to your blockchain
            if len(blockchain) > 0: add_block()
            else:
                print("\n\n--- First create a blockchain. ---\n")
                time.sleep(1)

        elif response == 'b': # Check one block from your blockchain
            if len(blockchain) > 0: check_block()
            else:
                print("\n\n--- First create a blockchain. ---\n")
                time.sleep(1)

        elif response == 'r': # Remove one block from your blockchain
            # if len(blockchain) > 0: remove_block()
            if len(blockchain) > 0: 
                print("\n\n--- En construction ---\n")
                time.sleep(1)
            else:
                print("\n\n--- First create a blockchain. ---\n")
                time.sleep(1)

        elif response == 's': # Save your blockchain
            if len(blockchain) > 0: save_blockchain()
            else:
                print("\n\n--- First create a blockchain. ---\n")
                time.sleep(1)

        elif response == 'd': # Delete your blockchain
            if len(blockchain) > 0: delete_blockchain()
            else:
                print("\n\n--- First create a blockchain. ---\n")
                time.sleep(1)
        else: # Wrong entry
            print("\n\n--- Wrong entry. ---\n")
            time.sleep(1)

start()