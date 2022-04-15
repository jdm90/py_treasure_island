import os
from art import logo

clear = lambda: os.system('cls')

print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

is_game_over = False

def play_game():
    left_or_right = input('\nYou\'re at a crossroad. Would you like to go "left" or "right"? ')
    if left_or_right == "left":
        swim_or_wait = input('\nYou come to a lake. You see an island in the middle of the lake. Type "swim" to swim across, or "wait" to wait for a boat. ')
        if swim_or_wait == "swim":
            print("\nUnfortunately the lake was very deep, and you are not the best swimmer.")
            print("Game over.")
            is_game_over = True
        else:
            door_color = input('\nYou arrive at the island unharmed. You find a house on the island with 3 doors... one "red", one "yellow", and one "blue". Which color door do you choose? ')
            if door_color == "red":
                print(f"\nYou opened the red door. A wild flame burns from behind the door, engulfing the area. Unfortunately you are trapped in the fire.")
                print("Game over.")
            elif door_color == "blue":
                print(f"\nYou opened the blue door. You enter a room of beasts!")
                print("Game over.")
            elif door_color == "yellow":
                print(f"\nYou opened the yellow door and found the treasure. YOU WIN!!!")
                print("Game over.")
            else:
                print("\nInvalid choice. Follow directions.")
                print("GAME OVER.")
    else:
        print("\nYou went right... right into a hole that you mistakingly fell into, that is. Better luck next time.")
        print("Game over.")
        is_game_over = True

while not is_game_over:
    play = input('\nWould you like to play the game? Type "y" or "n":  ')
    if play == "y":
        clear()
        print(logo)
        print("Alright, let's begin!")
        play_game()
    if play == "n":
        print("Goodbye.")
        is_game_over = True