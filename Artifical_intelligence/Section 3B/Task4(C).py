def sort_words_with_ascii_check(text):

    alphb = text.split()

    for i in range(len(alphb)):
        for j in range(0, len(alphb) - i - 1):
  
            if alphb[j] > alphb[j + 1]:
                
                alphb[j], alphb[j + 1] = alphb[j + 1], alphb[j]


    return " ".join(alphb)


user= input("Enter text: ")


sort_text = sort_words_with_ascii_check(user)
print("YOUR SORT TEXT:", sort_text)
