def write():
    txt=input("enter you want to add:")
    with open(r"C:\Users\Ajith\new_pro\data.txt","w") as f:
        f.write(txt.strip("\r\n")+"\n") 
def read():
            with open(r"C:\Users\Ajith\new_pro\data.txt","r") as f:
                viewed_file=f.read()
                print(viewed_file)
                print("\n")
def append():
    txt=input("enter you want to add:\n")
    with open(r"C:\Users\Ajith\new_pro\data.txt","a") as f:
        f.write(txt.strip("\r\n") + ("\n"))
def find_replace():
     with open(r"C:\Users\Ajith\new_pro\data.txt","r+") as f:
          viewed_file=f.read()
          find_word=input("enter a word to find:")
          replace_word=input("enter the replace word:")
          if find_word in viewed_file:
              viewed_file=viewed_file.replace(find_word,replace_word)
              print(viewed_file)
          else:
              print("word is not in the file")      \
                            
def exit():
    print("exiting") 
#display menu
while True:
    try: 
        print("1.write")
        print("2.read")
        print("3.append") 
        print("4.find_replace")
        print("5.exit")  
        print("\n")
        option=int(input("enter your option:"))
        if option==1:
            write()
        elif option==2:
            read()
        elif option==3:
            append()
        elif option==4:
            find_replace()
        else:
            exit()
    except Exception as e:
        print(e)