def new_quiz(questions, choices):
    guesses = []
    correct_guesses = 0
    q_num = 0

    for q in questions:
        q_num += 1
        print(f"Question #{q_num}: {q}")

        for c in choices[q_num - 1]:
            print(c)

        guess = input("Enter your choice (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess not in "ABCD":
            print("_________________________________________")
            print(f"Your answer: {guess} \n" f"Correct answer: {questions[q]} ")
            print("Error: Invalid choice, no marks!")
            print("_________________________________________")
            continue

        is_correct = check_answer(guesses[q_num - 1], questions[q])
        if is_correct:
            correct_guesses += 1

    show_score(guesses)


def check_answer(user_ans, correct_ans):
    print("_________________________________________")
    print(f"Your answer: {user_ans} \n" f"Correct answer: {correct_ans} ")

    if user_ans == correct_ans:
        print(f"You are correct!")
        print("_________________________________________")
        return True
    else:
        print(f"You are wrong :(")
        print("_________________________________________")
        return False


def show_score(guesses):
    ans_list = []
    for q in questions:
        ans_list.append(questions[q])

    print(f"Answers: {ans_list}")
    print(f"Guesses: {guesses}")


questions = {
    "In New York State, summer is warmer than winter because in summer New York State has: ": "D",
    "Which object forms by the contraction of a large sphere of gases causing the nuclear fusion of lighter elements into heavier elements? ": "C",
    "Evidence that the universe is expanding is best provided by the: ": "A",
    "The largest circular storm in our solar system is on the surface of which of the following plants?": "A",
    "One of the largest volcanos in our solar system is named Olympus Mons. This volcano is located on: ": "D",
    "Of the following four times, which one best represents the time it takes energy generated in the core of the sum to reach the surface of the sun and be radiated? ": "D",
    "Which one of the following moon features is named Copernicus? Is it a: ": "B",
    "Which of the following statements is true for BOTH Saturn and Jupiter? ": "C",
    "If you were watching a star collapsing to form a black hole, the light would disappear because it: ": "A",
    "In which spectral region is it possible for astronomers to observe through clouds? ": "B",
}

choices = [
    [
        "A. Fewer hours of daylight and receives low angle insolation",
        "B. Fewer hours of daylight and recieves high angle insolation.",
        "C. More hours of daylight and receives low angle insolation.",
        "D. More hours of daylight and receives high angle insolation. ",
    ],
    ["A. Comet", "B. Planet", "C. Star", "D. Moon"],
    [
        "A. Red shift in the light from distant galaxies",
        "B. Change in the swing direction of a Foucault pendulum on Earth ",
        "C. Parallelism of Earth's axis in orbit.",
        "D. Sprial shape of the Milky Way Galaxy",
    ],
    ["A. Jupiter", "B. Venus", "C. Uranus", "D. Earth"],
    ["A. Jupiter's moon Callisto", "B. Venus", "C. Saturn's moon Titan", "D. Mars"],
    [
        "A. Three minutes",
        "B. Thirty days",
        "C. One thousand years",
        "D. One million years",
    ],
    ["A. Sea", "B. Crater", "C. Mountain range", "D. Rill"],
    [
        "A. Only one rotates rapidly while the other rotates very slowly.",
        "B. Their periods of rotation are linked to their period of revolution.",
        "C. Both rotate faster than the Earth.",
        "D. Both rotate slower than the Earth.",
    ],
    [
        "A. Is strongly redshifted",
        "B. Is strongly blueshifted",
        "C. Its color suddenly becomes black",
        "D. None of the above",
    ],
    ["A. Visual", "B. Radio", "C. Ultraviolet", "D. X-Ray"],
]

print(
    "Welcome to Astronomy Quiz Hard Edition!\nLet's proceed through 10 M/C questions and see how many you can get right. \n"
)

play_again = True
while play_again:
    new_quiz(questions, choices)

    play_again = input(
        "Would you like to play again? Enter 'Y' to play again. "
    ).upper()
    if play_again == "Y":
        play_again = True
        print("\n\n\n_________________________________________")
    else:
        print("Goodbye! ")
        play_again = False
