import random
from operator import itemgetter
from data import data
from art import logo, vs

# Print logo art
# initialize a score tally
# get a random number to index a random celebrity
# get another random number for another celebrity
# index those celebs to find their followers and print their info in the question
#


def run_game():
    print(logo)
    score = 0
    game_continues = True
    while game_continues:
        index1, celeb1 = get_celeb1()
        celeb2 = get_celeb2(index1)
        real_answer = compare_celebs(celeb1, celeb2)
        user_answer = ask_question(celeb1, celeb2)
        correct = compare_answers(real_answer, user_answer)
        if not correct:
            game_over(score)
            game_continues = False
        else:
            score += 1


def get_celeb1():
    index = random.randint(0, len(data) - 1)
    return index, data[index]


def get_celeb2(prev_index):
    new_index = prev_index
    while prev_index == new_index:
        new_index = random.randint(0, len(data) - 1)
    return data[new_index]


def ask_question(celeb1, celeb2):
    print(celeb1)
    print(celeb2)
    id1, name1, follower_count1, description1, country1 = itemgetter(
        "id", "name", "follower_count", "description", "country"
    )(celeb1)
    id2, name2, follower_count2, description2, country2 = itemgetter(
        "id", "name", "follower_count", "description", "country"
    )(celeb2)
    print(f"Compare A: {name1}, {description1}, from {country1}")
    print(vs)
    print(f"Against B: {name2}, a {description2}, from {country2}")
    return input("Who has more followers? Type 'A' or 'B': ")


def compare_celebs(celeb1, celeb2):
    if celeb1["follower_count"] > celeb2["follower_count"]:
        return "A"
    else:
        return "B"


def compare_answers(answer1, answer2):
    if answer1 == answer2:
        return True
    else:
        return False


def game_over(score):
    print(f"Sorry, that's wrong. Final score: {score}")


run_game()
