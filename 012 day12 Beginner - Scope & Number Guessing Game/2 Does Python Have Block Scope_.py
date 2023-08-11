################### Scope ####################
""" 
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}") """

#  # Local Scope
""" 
def drink_position():
    potion_strength = 2
    print(potion_strength)

drink_position()
print(drink_position); """

#  # Global Scope
""" player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)
"""

# there is no block scope

# game_lever = 3 
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_lever < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)