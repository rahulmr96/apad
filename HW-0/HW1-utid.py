
def customEncrypt(usr_str,N,D,*args):   ##Task 1
    rev_usr_str=usr_str[::-1]
    encrypt_lst=[]
    ovr_flow_lst=[]  ##Incase the value goes above 126 (ASCII limit)
    undr_flow_lst=[]  ##Incase the value goes below 34 (Ignoring ASCII value of '!' and ' ')
    
    try:
        overflow_encrypt=args[1][::-1]    ###Optional argument to see if overflow has happened
        underflow_encrypt=args[0][::-1]   ###Optional argument to see if underflow has happened
    except:
        pass

    for i in range(0,len(rev_usr_str)):
        ascii_val_org=ord(rev_usr_str[i])
        ovr_flow_flag=0
        undr_flow_flag=0
        ascii_val=ascii_val_org+(D*N)
        
        if(ascii_val>126):
            ovr_flow_flag=1                ###Flag to indicate overflow, i.e. greater than 126
            ascii_val=ascii_val%126+34     ### If the ascii value is greater than 126, it will not encrypt it. So we force it to fall within our ASCII range of 34 & 126
        
        elif(ascii_val<34):
            undr_flow_flag=1                ###Flag to indicate undeflow, i.e lesser than 34
            ascii_val=ascii_val+34         ### If the ascii value is lesser than 34, it won't encrypt it. So we force it to fall within our ASCII range of 34 & 126
                
        try:                                    ####Checks to see if an overflow, underflow flag is given to the character within the string
            if overflow_encrypt[i]==1 or underflow_encrypt[i]==1:
                ascii_val=overflow_underflow_encrypt(ord(rev_usr_str[i]),N,D,overflow_encrypt[i],underflow_encrypt[i])
        except:
            pass

        encrypt_lst.append(ascii_val)
        undr_flow_lst.append(undr_flow_flag)
        ovr_flow_lst.append(ovr_flow_flag)
        
        encrypt_val=''.join(chr(i) for i in encrypt_lst)
    return encrypt_val,undr_flow_lst,ovr_flow_lst

def overflow_underflow_encrypt(string,N,D,overflow_encrypt,underflow_encrypt):  ##Exception when the ranges fall out of our ASCII range (34-126)
    if overflow_encrypt==1:
        return string+(D*N)-34+126
    elif underflow_encrypt==1:
        return string+(D*N)-34

def testCustomEncrypt():          ###Task 2
    while True:
        try:
            input_string_username=input('Enter userID as text:  ')
            input_string_password=input('Enter password as text:    ')            
            if input_string_username.find('!')>-1 or input_string_username.find(' ')>-1 or input_string_password.find('!')>-1 or input_string_password.find(' ')>-1:
                print("\nError: Input string has '!' or ' '. Please try again")
                continue
            add_char=int(input('Enter the value of n (ASCII shifter):   '))
            if(add_char<=0):
                print('Error: The value of n cannot be less than 1. Please try again')
                continue
            direction=int(input('Enter the value of d (Direction):  '))
            if not(direction==-1 or direction==1):
                print(direction)
                print("Error: Direction can only be -1 or +1")
                continue
        
            break
        except ValueError:
            print("Error: Please enter a valid number!")
            continue

    encrypted_val_username,undrflow_u,ovrflow_u=customEncrypt(input_string_username,add_char,direction)
    encrypted_val_password,undrflow_p,ovrflow_p=customEncrypt(input_string_password,add_char,direction)
    
    print("This is the encrypted userID:    ",encrypted_val_username)        
    print("This is the encrypted password:  ",encrypted_val_password)

    decrypted_val_username,undrflow_decrypt_u,ovrflow_decrypt_u=customEncrypt(encrypted_val_username,add_char,-1*direction,undrflow_u,ovrflow_u)
    decrypted_val_password,undrflow_decrypt_p,ovrflow_decrypt_p=customEncrypt(encrypted_val_password,add_char,-1*direction,undrflow_p,ovrflow_p)

    print("This is the original userID: ",decrypted_val_username)
    print("This is the original password:   ",decrypted_val_password)


print('############## MIS 385N HW 0###########################################\n')
print("\t\t Rahul Mohan Rangarao \t\t\n")
print("##############  Custom Encryption Algorithm ####################\n\n\n")
testCustomEncrypt()



#  Task 3
# The 1st combination (asamant,Temp123) and the 4th combination (skharel   Life15$) are present in the database 
# The 2nd username (aissa) and the 3rd username (bjha) are present in the database file but the passwords do not match 
# The 5th username does not meet the requirement for userid since it contains a '!' 
