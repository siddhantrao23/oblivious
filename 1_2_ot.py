from Crypto.Cipher import AES
import hashlib
import random
import sys

# initialise publically agreed variables
g = 9
p = 1001

class Alice:
    def __init__(self):
        self.a = random.randint(5, 10)
        print ('Random a: ' + str(self.a))
    def compute_first(self, g):
        self.A = (g ** self.a) % p
        print ('\nAlice: ' + str(self.A))
    def compute_sharedkey(self, B):
        self.key0 = hashlib.sha256(str((B**self.a) %p)).digest()
        self.key1 = hashlib.sha256(str(((B/self.A)**self.a) %p)).digest()
        print ('\nAlice calculates these keys')
        print ('Key 0: ' + self.key0)
        print ('Key 1: ' + self.key1)
    def encrypt(self):
        cipher1 = AES.new(self.key0, AES.MODE_ECB)
        cipher2 = AES.new(self.key1, AES.MODE_ECB)
        self.en0 = cipher1.encrypt('Bob did it      ')
        self.en1 = cipher2.encrypt('Alice did it    ')

class Bob:
    def __init__(self, c):
        self.b = random.randint(10, 15)
        print ('Random b: ' + str(self.b))
        self.c = c
    def compute_first(self, g, A):
        if(self.c == 0):
            self.B = (g ** self.b) % p
        else:
            self.B = A * ((g ** self.b) % p)
        print ('Bob: ' + str(self.B))
    def compute_sharedkey(self, A):
        self.shared_key = hashlib.sha256(str((A ** self.b) % p)).digest()
        print ('\nBob calculates this key:')
        print ('Bob key: ' + self.shared_key)
        print("")

    def decrypt(self, en0, en1):
        cipher = AES.new(self.shared_key, AES.MODE_ECB)
        message_0 = cipher.decrypt(en0)
        message_1 = cipher.decrypt(en1)

        print (message_0)
        print (message_1)

def main():
    c = int(input("Bob enter choice (0 or 1)"))
    alice = Alice()
    bob = Bob(c)

    alice.compute_first(g)
    bob.compute_first(g, alice.A)

    alice.compute_sharedkey(bob.B)
    alice.encrypt()

    bob.compute_sharedkey(alice.A)
    bob.decrypt(alice.en0, alice.en1)

if __name__ == "__main__":
    main()
