from random import randint
from art import logo,vs
from game_data import data
import random


game_should_continue=True
score=0

account_a = random.choice(data)
account_b = random.choice(data)

while game_should_continue:

    #display logo
    print(logo)

    #take random from data
    account_a = account_b
    account_b = random.choice(data)


    #Format of A & B
    def format(account):
        '''takes the account the data and returns in format'''
        account_name = account["name"]
        account_description = account["description"]
        account_country = account["country"]
        return f"{account_name}, {account_description}, from {account_country}"
    print(f"Compare A: {format(account_a)}")
    print(vs)
    print(f"Against B: {format(account_b)}")

    def check_answer(user_guess, a_followers, b_followers):
        '''Take a user's guess and the follower counts and returns if they got it right'''
        if a_followers>b_followers:
            return user_guess =='A'
        else:
            return user_guess == 'B'


    if account_a == account_b:
        account_b = random.choice(data)


    #ask to guess A or B??
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    #compare A with B
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score+=1
        print(f"You are right !!!!! Current score: {score}")
        print("\n" * 30)
    else:
        print(f"Sorry, that's wrong  Final score: {score}")
        game_should_continue = False


