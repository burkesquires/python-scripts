Pwd_Key = 4 #modify to set personalised Key

#Function to Encode the user given data
def Cipher(Text):
    
    Cipher_Text = ''.join(chr(ord(i) + Pwd_Key ) for i in Text)
    return Cipher_Text + '\n'

#Function to store the encrypted data.
def Entry(Data):
    with open('Data.txt', 'a') as file:
        file.write(Data)
        print('\nEntered data has been successfully encrypted and recorded..!!!\n')
'''

print(En_Data)
'''
#Function to display the encrypted data.
def Extract():

    En_Records,De_Records = [],[]

    with open('Data.txt', 'r') as file:
        x = file.readlines()

        En_Records.extend(iter(x))
        for En_Record in En_Records:
            En_Text = En_Record
            De_Text = "".join(
                (chr(ord(En_Text[j]) - Pwd_Key)) for j in range(len(En_Text))
            )


            De_Records.append(De_Text)

    return De_Records


while True:
    print(" 1 -> Enter Data ")
    print(" 2 -> Display Stored Data ")
    print(" 0 -> Exit \n")

    opt = int(input("Enter the option : "))
    print("\n")

    if opt == 0:
        exit()

    elif opt == 1:
        Data = input("Enter your data :\n")
        En_Data = Cipher(Data)
        Entry(En_Data)

    elif opt == 2:
        user_key = int(input("Enter the Key to decrypt : "))

        if user_key == Pwd_Key:
            L = Extract()
            for i in range(len(L)):
                print(L[i][:-1])
            print("\n")

        else:
            print("Wrong key !! ")

    else:
        print("Enter valid option !!")








