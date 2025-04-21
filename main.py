import random
import json
import os

if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        last_data = json.load(f)
    print("Previous session summary:")
    print(f"Score: {last_data['score']}")
    print(f"Accuracy: {last_data['accuracy']:.1f}%")
    print(f"Questions Asked: {last_data['asked']}\n")


def save_data(score, accuracy, asked):
    data = {
        "score": score,
        "accuracy": accuracy,
        "asked": asked

    }
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def print_all_past_performance():
    print("Past Performance Summary:")
    for question, wrongs in stats.items():
        print(f"{question}: {wrongs} wrong")

stats = {}

def save_stats(stats):
    with open("stats.json", "w") as f:
        json.dump(stats, f, indent=4)

def flashcards(flashcard_set, stats):
    score = 0
    asked = 0
    questions = list(flashcard_set.keys())
    weighted_questions = questions + [q for q in stats if q in flashcard_set for _ in range(stats[q])]
    random.shuffle(weighted_questions)
    incorrect_questions = []
    for question in questions:
        response = input(question + " ")
        if response.lower().strip() == flashcard_set[question].lower().strip():
            print("Correct! ✅")
            score += 1
        else:
            print("Wrong! ❌")
            incorrect_questions.append(question)
        asked += 1
        accuracy = (score / asked) * 100
        print(f"Your score is {score}")
        print(f"Your accuracy is {accuracy:.1f}%\n")

    for question in incorrect_questions:
        stats[question] = stats.get(question, 0) + 1

    return score, accuracy, asked

flashcards_easy= {
    "How many teams make it to March Madness?": "68", 
    "In basketball, how many points is a shot made from beyond the arc worth?": "3",
    "In baseball what is it called when you win the division?": "winning the pennant",
    "How many colors are in a rainbow?": "7",
    "How many innings is a baseball game (assuming extra innings DO NOT happen)": "9",
    "Who painted the Mona Lisa?": "leonardo da vinci",
    "Who was the first president of the United States?": "george washington",
    "What is the capital of California?": "sacramento",
    "What video game character has a brother named Luigi who wears green?": "mario",
    "What is the term for scoring three goals in a single hockey game?": "hat trick"

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

save_data(score, accuracy, asked)

#_________________________________________________________________________________

flashcards_hard= {
    "What teams have won the last 5 World Series (2020-2024)?": "dodgers, braves, astros, rangers, dodgers",
    "Who is the only athlete to play in both a Super Bowl and a World Series? (Bo Jackson, Deion Sanders, Brian Jordan, Tim Tebow)": "deion sanders",
    "Why does 6 + 4 + 3 = 2 in baseball?": "6-4-3 double play",
    "What is the SF Giants ballpark called?": "oracle park",
    "What is Spain's busiest cruise port?": "barcelona",
    "Which Thanksgiving favorite did Marcus L. Urann invent?": "cranberry sauce",
    "What is the fastest land animal?": "cheetah",
    "Who is considered the fastest man in the world?": "usain bolt",
    "What is the largest mammal in the world?": "blue whale",
    "What is the name of our galaxy?": "milky way"
}

hardquestions= list(flashcards_hard.keys())

randomquestions= random.sample(hardquestions, k=len(flashcards_hard))

score, accuracy, asked = flashcards(flashcards_easy, stats)
save_data(score, accuracy, asked)

score, accuracy, asked = flashcards(flashcards_hard, stats)
save_data(score, accuracy, asked)

save_stats(stats)
print_all_past_performance()