def removed_punctuation():
    user = input("Enter text: ")
    name = ""
    pun = '''.,?!:;'"()[]}{-—.../*&@_~^|'''

    for i in user:
        if i not in pun:  
            name += i
    
    print(f"Your text without punctuation is: {name}")
removed_punctuation()
