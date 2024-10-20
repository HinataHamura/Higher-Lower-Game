from art import logo, vs
from game_data import data
import random
import os
import time


def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers and guess == "a":
        return True
    elif a_followers < b_followers and guess == "b":
        return True
    else:
        return False


def game():
    print(logo)
    game_on = True
    account_a = get_random_account()
    account_b = get_random_account()
    score = 0
    while game_on:
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            account_a = account_b

        else:
            print(f"Sorryy!That's Wrong.Final Score {score}")
            game_on=False

game()
