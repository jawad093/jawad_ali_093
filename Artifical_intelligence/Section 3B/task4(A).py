def Luhn_Algorithm():
    user_card = input("Enter the Card Number: ")

    if len(user_card) != 16:
        print("Invalid Card Number")
        return
    
    card_number = [int(digit) for digit in user_card]
 
    card_number.reverse()
    
    for i in range(1, len(card_number), 2):
        card_number[i] *= 2
        if card_number[i] > 9:
            card_number[i] -= 9
    
    total_sum = sum(card_number)

    if total_sum % 10 == 0:
        print("Valid Card Number")
    else:
        print("Invalid Card Number")

Luhn_Algorithm()
