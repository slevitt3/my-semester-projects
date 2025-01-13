#Sadie Levitt
#12/2/24
#Pokemon Evolution Game

#Initial
#Global Variables
pokemon_level = 0
pokemon_name = "squirtle"

#Functions
def pokemon_evolution():
    def evolve():
        global pokemon_name
        if pokemon_level > 5 and pokemon_level < 10:
            pokemon_name = "pikachu"
        if pokemon_level >= 10:
            pokemon_name = "snore"
    def train():
        global pokemon_level
        pokemon_level = pokemon_level + 1
        global pokemon_level2
        pokemon_level2 = str(pokemon_level)
        print("Your pokemon level is " + pokemon_level2)
    def gym_battle():
        import random
        outcome = random.randint(1,2) #50% chance to win/lose
        if outcome == 1:
            print("You win!")
        if outcome == 2:
            print("You lose")
    def display_info():
        print("Your pokemon level is " + pokemon_level2)
        print("Your pokemon name is " + pokemon_name)
    def quit():
        print("Play again soon!")


    print("Welcome to Pokemon Evolution")
    while True:
        print("Choose today's activity: ")
        print("""1. Train
    2. Gym Battle
    3. Rest (Display Info)
    4. Quit""")
        option = int(input("Make your choice (1-4)"))
        if option == 1:
            evolve()
            train()
        if option == 2:
            gym_battle()
        if option == 3:
            evolve()
            display_info()
        if option == 4:
            quit()
            break
#main
pokemon_evolution()
