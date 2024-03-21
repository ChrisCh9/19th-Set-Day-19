#A shift code is where a message can be easily encoded and is one of the simplest codes to use. Each letter is moved forwards through the alphabet a set number of letters to be represented by a new letter. For instance, “abc” becomes “bcd” when the code is shifted by one (i.e. each letter in the alphabet is moved forward one character). You need to create a program which will display the following menu: If the user selects 1, they should be able to type in a message (including spaces) and then enter a number. Python should then display the encoded message once the shift code has been applied. If the user selects 2, they should enter an encoded message and the correct number and it should display the decoded message (i.e. move the correct number of letters backwards through the alphabet). If they select 3 it should stop the program from running. After they have encoded or decoded a message the menu should be displayed to them again until they select quit. 

alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '}

def get_data():
    mess = input("Enter your message in lowercase:")
    num = int(input("Enter a number:"))
    while num == 0 or num > 26:
        print("Enter a number from 1 to 26:")
    data = (mess,num)
    return (data)
        

def make_code(mess,num):
    new_mess = ""
    for x in new_mess:
        y = alphabet.index(x)
        y += num
        if y > 26:
            y -= 27
        char = alphabet[y]
        new_mess += char
    print(new_mess,"\n")

def decode(mess,num):
    new_mess = ""
    for x in new_mess:
        y = alphabet.index(x)
        y -= num
        if y < 0:
            y += 27
        char = alphabet[y]
        new_mess += char
    print(new_mess,"\n")

loop = True

while loop == True:
    print("1) Make a code")

    print("2) Decode a message")

    print("3) Exit\n")

    choice = int(input("Enter your selection: "))

    if(choice==1):
        (mess,num) = get_data()
        make_code(mess,num)
    elif(choice==2):
        (mess,num) = get_data()
        decode(mess,num)
    elif(choice==3):
        loop = False
    else:
        print("Incorrect choice")




"""def get_data():
    mess = input("Enter your message in lowercase")
    num = int(input("Enter a number"))
    while num == 0 or num > 26:
        print("Enter a number from 1 to 26")
    data = (mess,num)
    return (data)
        

def make_code():
    new_mess = ""
    for x in new_mess:
        y = alphabet.index(x)
        y += num
        if y > 26:
            y -= 27
        char = alphabet[y]
        new_mess += char
    print(new_mess,"\n")

def decode():
    new_mess = ""
    for x in new_mess:
        y = alphabet.index(x)
        y -= num
        if y < 0:
            y += 27
        char = alphabet[y]
        new_mess += char
    print(new_mess,"\n")"""