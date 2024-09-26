movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

total_amount = 0 
for _,budget in movies:
    total_amount += budget 

average_budget=total_amount/len(movies)
print(f'Average Budget of this movies is : {average_budget}')

for movie,budget in movies:
    if budget>average_budget:
        print(f'{movie} has higher budget and {(int(budget - average_budget))} is higher than average.')

