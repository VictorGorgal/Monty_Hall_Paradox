import random

SAMPLE_SIZE = 10_000
TOTAL_DOORS = 3

doors = [False for _ in range(TOTAL_DOORS)]  # generates all the doors

total_wins = 0
total_loses = 0

for _ in range(SAMPLE_SIZE):
    prize = random.randint(0, TOTAL_DOORS - 1)
    door_picked = random.randint(0, TOTAL_DOORS - 1)

    doors[prize] = True  # "puts" the prize in a random "door"

    if prize == door_picked:  # eliminates total_doors - 2
        random_door = random.choice(doors[:door_picked] + doors[door_picked + 1:])  # gets a random element from a list that doesn't contain door_picked
        available_doors = [doors[door_picked], random_door]
    else:
        available_doors = [doors[door_picked], doors[prize]]

    door = available_doors[1]  # "changes" for the second door

    if door:
        total_wins += 1
    else:
        total_loses += 1

    doors[prize] = False


print(f'For a total of {SAMPLE_SIZE} simulations with each conatining {TOTAL_DOORS} doors each:')
print(f'{total_wins / SAMPLE_SIZE * 100 :.3f}% Wins')
print(f'{total_loses / SAMPLE_SIZE * 100 :.3f}% Loses')
