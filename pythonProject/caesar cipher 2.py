'''alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("Type 'encode' for encrypt,type 'decode' for decrypt:\n").lower()
text=input("type your message :\n").lower()
shift=int(input("type the shift number :\n"))'''
print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88    
                             
                          88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           ''')
def encrypt(original_text,shift_by):
                            
                            cipher_text=""
                            for latter in text:
                                shift_by=alphabet.index(latter)+shift
                                shift_by%=len(alphabet)
                                cipher_text += alphabet[shift_by]
                            print(f"The encoded text is :\n{cipher_text}")
def decrypy(original_text,shift_by):
                                cipher_text=""
                                for latter in text:

                                    

                                    shift_by=alphabet.index(latter)-shift
                                
                                    shift_by%=len(alphabet)
                                    cipher_text += alphabet[shift_by]
                                print(f"The decoded text is :\n{cipher_text}")
should_continue=True
while should_continue:
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction=input("Type 'encode' for encrypt,type 'decode' for decrypt:\n").lower()
    text=input("type your message :\n").lower()
    shift=int(input("type the shift number :\n"))
    if direction=="encode":
            encrypt(original_text=text,shift_by=shift)
    else:
            decrypy(original_text=text,shift_by=shift)
    restart=input("type 'yes 'to restart .otherwise 'no':\n").lower()
    if restart=="No":
         should_continue=False
         print("good bye")