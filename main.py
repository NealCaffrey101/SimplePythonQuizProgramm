import json
import time
import random
"""
with open('Quiz.json') as file:
    data = json.load(file)

print(str(data["questions"][0]["question1"]))

answer = input("What is your answer? ")
if answer == str(data["correct_answers"][0]["correct_answer1"]):
    print("Congratulations that was right!")
else:
    print("That was wrong you looser")
"""

data = input("Press S to start: ")
i = 1
if data == "s" or data == "S":
    with open('Quiz.json') as file:
        data = json.load(file)
    print(str(data["questions"][i-1]["question1"]))
    print(str(data["answers"][i-1]))
    user_answer = input("What is your answer? ")
    if user_answer == str(data["correct_answers"][0]["correct_answer1"]):
        print("Congratulations that was right!")
    else:
        print("That was wrong you looser")
        time.sleep(3)
        quit()

else:
    quit()

