#ciao prova

import random
import sys


class Encoding:

    def __init__(self, password):
        self.password = password
        self.lista_binari = ""
        self.lista_random = ""
        self.lista_encoded = ""
        self.lista_grandezza = []
        self.binary_file()
        self.random_binary()
        self.crypt_file()
        self.save_file()


    def binary_file(self):
        for i in range(len(self.password)-1):
            binary = bin(ord(self.password[i]))[2:]
            self.lista_binari = self.lista_binari + str(binary)
            self.lista_grandezza.append(str(len(binary)))


    def random_binary(self):
        for i in range(len(self.lista_binari)):
            random_number = random.randint(0,1)
            self.lista_random = self.lista_random + str(random_number)
        write_file_key = open("crypt_file.key.txt","w")
        stringa_grandezza = " ".join(self.lista_grandezza)
        write_file_key.write(self.lista_random + "\n" + stringa_grandezza)
        write_file_key.close()


    def crypt_file(self):
        for i in range(len(self.lista_binari)):
            if self.lista_binari[i] == self.lista_random[i]:
                self.lista_encoded = self.lista_encoded + "0"
            else:
                self.lista_encoded = self.lista_encoded + "1"


    def save_file(self):
        open_file_crypt = open("crypt_file.txt","w")
        open_file_crypt.write(self.lista_encoded)
        open_file_crypt.close()




class Decoding:

    def __init__(self, crypt_password, key):
        self.crypt_password = crypt_password
        self.key = key
        self.lista_divisa = []
        self.lista_animata = []
        self.text = ""
        self.com_file()
        self.decrypt_file()
        self.converter()


    def com_file(self):
        elementi = self.key[0][:-1]
        numero_elementi = self.key[1].split(" ")
        for i in numero_elementi:
            i = int(i)
            stringa_divisa = ""
            for k in range(i):
                stringa_divisa = stringa_divisa + str(elementi[k])
            self.lista_divisa.append(stringa_divisa)
            elementi = elementi[i:]


    def decrypt_file(self):
        password_variabile = self.crypt_password
        for i in range(len(self.lista_divisa)):
            stringa_completa = ""
            for k in range(len(self.lista_divisa[i])):
                if password_variabile[k] == self.lista_divisa[i][k]:
                    stringa_completa = stringa_completa + "0"
                else:
                    stringa_completa = stringa_completa + "1"
            self.lista_animata.append(stringa_completa)
            password_variabile = password_variabile[len(self.lista_divisa[i]):]


    def converter(self):
        for i in self.lista_animata:
            i = int(i, 2)
            self.text = self.text + chr(i)
        print(self.text)




if __name__ == "__main__":
    
    if len(sys.argv) > 2:
        if sys.argv[2] == "-e":
            filename = sys.argv[2]
            read_file = open(filename).read()
            Encoding(read_file)
        
        elif sys.argv[2] == "-d":
            open_file_crypt = open("crypt_file.txt")
            open_file_key = open("crypt_file.key.txt")
            read_file_crypt = open_file_crypt.read()
            read_file_key = open_file_key.readlines()
            start_decrypt = Decoding(read_file_crypt, read_file_key)
            start_decrypt
