#A python code for a lucky wheel game\
# Description: This code simulates a lucky wheel game where the player can spin a wheel with three counters.
# Each counter can show one of three symbols: ❤️, 🔥, or 🍀.
# The player wins the jackpot if all three counters show the same symbol,
# and they get a close call if two counters match. 
# The game keeps track of the number of spins, wins, and losses, 
# it calculates the probability of winning the jackpot at the end.

import random
import time

count_times = 0
count_win = 0
count_lose = 0

def spin_wheel():
    global count_win, count_lose
    counter1 = ["❤️","🔥","🍀"]     #there can be three different counters or a single counter popping the shapes using random module
    counter2 = ["❤️","🔥","🍀"]
    counter3 = ["❤️","🔥","🍀"]
    wheel1 = random.choice(counter1)
    wheel2 = random.choice(counter2)
    wheel3 = random.choice(counter3)
    print(f"{wheel1}   {wheel2}   {wheel3}")
    time.sleep(1.5)   #usage of time module to make it realistic and can be given a loading interface in between.
    
    if wheel1 == wheel2 == wheel3:
        print("Congratulations! You won the jackpot!")
        count_win += 1
    elif wheel1 == wheel2 or wheel1 == wheel3 or wheel2 == wheel3:
        print("that was close try again!")
    else:
        count_lose += 1
        print("Better luck next time!")
    return count_win, count_lose

print("Welcome to the Lucky Wheel Game!")
print("Please enter S to spin the wheel or Q to quit.").upper()  #Even if user input is 's' or 'q' it takes uppercase charecter.
while True:
    user_input = input("Enter your choice: ").upper()
    if user_input == "S":
        count_times += 1
        spin_wheel()
    elif user_input == "Q":
        print("Thank you for playing! Goodbye!")
        break
    else:     
        print("Invalid input. Please enter S to spin or Q to quit.")
    
print(f"You spun the wheel {count_times} times and won {count_win} times.")
print(f"probabilty of winning the jackpot: {count_win/count_times*100:.2f}%")
