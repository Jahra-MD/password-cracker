import hashlib
flag =0

pass_hash =input('enter md5 hash : ')

wordlist =input('File name : ')  #for opening file that contain passwords

try:
    pass_file =open(wordlist, "r")
except:
    print('no file found ')
    quit()

for word in pass_file:        #for comparing with each password
    enc_wrd =word.encode('utf-8')
    digest =hashlib.md5(enc_wrd.strip()).hexdigest()


    if digest ==pass_hash:
        print('Password found ')
        print('password is ' + word)
        flag =1
        break
if flag ==0:
    print("password is not in the list") 
