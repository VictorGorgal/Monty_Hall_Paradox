# Monty Hall Paradox
Inspired by: youtu.be/4Lb-6rxZxx0

The problem consists of 3 doors, where behind only one of them there is a prize, after the participant has chosen the door, one of the 2 other doors where the prize is not is revealed.
The participant can then choose whether to change the chosen door or not.

There will always be a chance of (T - 1) / T to win the prize if the participant wants to change the door, where T is the total number of doors (in this case 2/3).
If we play the game with 100 doors, after one of the doors is chosen, another 98 doors are revealed that do not contain the prize, leaving only the chosen door and another random one, in this case there will be a 99/100 chance of winning the prize if the participant change the door.

The algorithm consists of a dynamic algorithm and it is possible to choose any number greater than or equal to 3 doors, where 10_000 simulations will be run and the percentage of participants who changed the door will be shown along with the percentage of those who decided not to change the door.
