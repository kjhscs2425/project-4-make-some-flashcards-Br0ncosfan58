import random

flashcards_easy= {
    "How many teams make it to March Madness?": "68", 
    "In basketball, how many points is a shot made from beyond the arc worth?": "3 points",
    "In baseball what is it called when you win the division?": "winning the pennant",
    "Who is the only athlete to play in both a Super Bowl and a World Series? (Bo Jackson, Deion Sanders, Brian Jordan, Tim Tebow)": "Deion Sanders"
    "What is the term for scoring three goals in a single hockey game?": "A hat trick", #TODO: ADD MORE MAKE WITH LIST
}

flashcards_hard= {
    "What teams have won the last 5 World Series (2020-2024)?": "Dodgers (2020), Braves (2021), Astros (2022), Rangers (2023), Dodgers (2024)",
# "": "",
# "": "",
# "" :"",
# "": "",
# "": "",
# "": "",
# "": "",
# "": "",
# "": "",

}

easyquestions= list(flashcards_easy.keys())

randomquestions= random.sample(easyquestions, k=len(flashcards_easy))

score = 0
accuracy = 1
asked = 0
for randomquestion in randomquestions:
    response=input(randomquestion)
    if response == flashcards_easy[randomquestion]:
        print("Correct! ✅")
        score= score+1
        asked=asked+1
        accuracy=(score/asked)*100
        print(f"""Your score is {score}""")
        print(f"""Your accuracy is {accuracy}%""")
    else:
        print("Wrong! ❌")
        asked=asked+1
        accuracy=(score/asked)*100
        print(f"""Your score is {score}""")
        print(f"""Your accuracy is {accuracy}%""")