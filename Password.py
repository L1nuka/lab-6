# Linuka Hewagama

def encode(oldPass):
    newPass = ""
    for x in oldPass:
        if int(x) > 6:
            newPass += str(int(x) - 7)
        else:
            newPass += str(int(x) + 3)
    return newPass

if __name__ == '__main__':
    ans = 0
    data = ""
    while(True):
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        ans = int(input("Please enter an option: "))
        
        if ans == 1:
            data = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")

        if ans == 2:
            print(f"The encoded password is {data}, and the original password is {decode(data)}")
            
        if ans == 3:
            break