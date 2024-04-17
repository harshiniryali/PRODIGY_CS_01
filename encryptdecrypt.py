alphabet_list=['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def caesar(text,shift,type):
    cipher=""
    length=len(alphabet_list)
    if type=="d":
        shift*=-1
        length*=-1
    for i in text:
        if i not in alphabet_list:
            cipher+=i
            continue
        position=alphabet_list.index(i)
        new_position=position+shift
        new_position%=length
        cipher+=alphabet_list[new_position]
    return cipher
while True:
    user_req=input("Would you like to encrypt(e) or decrypt(d)?: ")
    text=input("Enter text(lowercase only): ").lower()
    try:
        shift=int(input("Enter shift/key value: "))
    except ValueError:
        print("Shift value must be an integer")
        continue
    if user_req=='e':
        print(f"The encrypted text is: {caesar(text,shift,user_req)}")
    elif user_req=='d':
        print(f"The decrypted text is: {caesar(text,shift,user_req)}")
    else:
        print("Invalid input try again")
        continue
    status=input("\nEnter 'y' to continue or 'n' to exit: ").lower()
    if status=='y':
        continue
    else:
        break