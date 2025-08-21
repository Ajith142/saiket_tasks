def analyze_file(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            text=file.read()
            print(text)
    #character count
        char_count=len(text)
        print("char_count:",char_count)
    #line_count
        with open(filename,"r",encoding="utf-8") as file:
         lines=len(file.readlines())
         print("lines:",lines)
    #word_cont
        words=text.split()
        word_count=len(words)
        print("word_count:",word_count)
    #word_freq
        word_freq={}
        for word in words:
            word = word.lower().strip(".,!?\"'()[]{}:;")
            if word:
                word_freq[word] = word_freq.get(word,0)+1
            sorted_freq=sorted(word_freq.items(),key=lambda x:x[1],reverse=True)
        for word, freq in sorted_freq:
             print(f"{word}-{freq}")  
    except Exception as e:
        print(e)
#getting input file
filename=input("enter the file name:")    
analyze_file(filename)