import random

def rand():
    secret_number=random.randint(1,100)
    attempts=0
    try:
        while(True):
            print("start your game\n")
            player_number=int(input("enter the number 1to 100:"))
            attempts+=1
            if secret_number > player_number:
                print("it is very low")
            elif secret_number < player_number:
                print("it is very high")
            else:
                print("yeah you won")
                print(attempts)
                exit()      
    except Exception as e:
        print(e)
        
rand()


