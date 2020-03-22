from Crypto.Cipher import AES
import hashlib
import random
import sys

g=9
n=1001

a=random.randint(5, 10)

b=random.randint(10,15)

Alice=(g**a) % n

c=1
if (len(sys.argv)>1):
	c=int(sys.argv[1])

print 'g: ',g,' n: ',n
print 'Alice value: ',Alice
print 'a (Alice random): ',a
print 'b (Bob random): ',b

# === Bob calculates ===

if (c==0):
	Bob=(g**b) % n
else:
	Bob=Alice*((g**b) % n)

# === Alice calculates ===

key0 = hashlib.sha256(str((Bob**a) %n)).digest()
key1 = hashlib.sha256(str(((Bob/Alice)**a) %n)).digest()

cipher1 = AES.new(key0, AES.MODE_ECB)
cipher2 = AES.new(key1, AES.MODE_ECB)

print '\nAlice calculates these keys'
print 'Key 0: ',key0
print 'Key 1: ',key1

en0=cipher1.encrypt('Bob did it      ')
en1=cipher2.encrypt('Alice did it    ')


## === Bob decrypts
print '\nBob calculates this key:'
Bob_key = hashlib.sha256(str((Alice**b) %n)).digest()
print 'Bob key: ',Bob_key

cipher1 = AES.new(Bob_key, AES.MODE_ECB)

message_0=cipher1.decrypt(en0)
message_1=cipher1.decrypt(en1)

print '\nBob decrypts the messages:'
print 'Message 0: ',message_0
print 'Message 1: ',message_1
