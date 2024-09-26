import random

def fizz_buzz_game():
    print("ahhhh!!! Fizz_buzz _games? allow start BOOOOOOOOMMMMMMM!")
    
    score = 0
    num = 0  

    while True:
        
        select_random_number = random.randint(1, 10000000000000000000000000)  
        num += select_random_number
       
        correct_answer = fizz_buzz(num)

     
        player_answer = input(f"Current number is {num}. What's your answer? ")

       
        if player_answer.strip().lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was '{correct_answer}'.")
            break
    

    print(f"Game Over! Your score is: {score}")

def fizz_buzz(num):
   
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"  
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

fizz_buzz_game()
