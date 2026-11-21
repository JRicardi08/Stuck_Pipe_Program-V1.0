import numpy as np

# Message to the user 
print("\nWelcome to the stuck pipe table. Program written by Jose Ricardi in Python.")

# Collect user input
choice = input(
    '\nWould you like to know the type of stuck pipe mechanism in the hole? "Y" or "N"\n'
).strip().lower()

# Conditional logic based on user input
if choice == "y":
    print("\nPlease answer the quiz below...\n")

    print(r'''
                /\ 
               /\/\ 

               |/\|
              //\/\\

              |\/\/|
             \|/\/\|   .''`/
      \''.    \`'. |  ||  /
       \ ||   |\ |||  || /
       _\||__/__\||_\_||/___

       |___________________|
        |  |   |   |   |  |
  ~~~~~~|~~|~~~|~~~|~~~|~~|~~~~~~
    ''')

    # Define the mechanisms and their corresponding scores
    MECHANISMS = ["Pack-off / Bridge off", "Differential Sticking", "Wellbore Geometry"]

    # Each question has a dictionary with the question text, options, and scores for each mechanism:
    # [Pack-off/Bridge off, Differential Sticking, Wellbore Geometry]
    questions_data = [
        {
            "question_number": 1,
            "question_text": "Pipe motion prior to sticking?",
            "options": [
                "(a) Move Up",
                "(b) Rotating Up",
                "(c) Move Down",
                "(d) Rotating Down",
                "(e) Static"
            ],
            "scores": {
                "a": [2, 0, 2],
                "move up": [2, 0, 2],
                "b": [0, 0, 2],
                "rotating up": [0, 0, 2],
                "c": [1, 0, 2],
                "move down": [1, 0, 2],
                "d": [0, 0, 2],
                "rotating down": [0, 0, 2],
                "e": [2, 2, 0],
                "static": [2, 2, 0]
            }
        },
        {
            "question_number": 2,
            "question_text": "Pipe motion after sticking?",
            "options": [
                "(a) Down Free",
                "(b) Down Restricted",
                "(c) Down Impossible"
            ],
            "scores": {
                "a":[0, 0, 2], 
                "down free":[0, 0, 2],
                "b":[1, 0, 2],
                "down restricted":[1, 0, 2],
                "c":[0, 0, 0],
                "down impossible": [0, 0, 0]
            }
        },
        {
            "question_number": 3,
            "question_text": "Pipe rotation after sticking?",
            "options": [
                "(a) Rotate Free",
                "(b) Rotate Restricted",
                "(c) Rotate Impossible"
            ],
            "scores": {
                "a": [0, 0, 2], 
                "rotate free": [0, 0, 2],
                "b":[2, 0, 2], 
                "rotate restricted": [2, 0, 2],
                "c": [0, 0, 0], 
                "rotate impossible": [0, 0, 0]
            }
        },
        {
            "question_number": 4,
            "question_text": "Circulating pressure after sticking?",
            "options": [
                "(a) Circulation not restricted",
                "(b) Circulation restricted",
                "(c) Circulation impossible"
            ],
            "scores": {
                "a":[0, 2, 2], 
                "circulation not restricted":[0, 2, 2],
                "b":[2, 0, 0], 
                "circulation restricted":[2, 0, 0],
                "c":[0, 0, 0], 
                "circulation impossible": [0, 0, 0]
            }
        }
    ]

    class StuckPipeQuiz:
        def __init__(self, questions, mechanisms):
            self.questions = questions
            self.mechanisms = mechanisms
            # Initial verctor zero: [0, 0, 0]
            self.total_scores = np.array([0, 0, 0])

        def run_quiz(self):
            for q in self.questions:
                print(f"\nQ-{q['question_number']}: {q['question_text']}")
                for option in q["options"]:
                    print(f"  {option}")

                while True:
                    answer = input("Your answer: ").strip().lower()
                    if answer in q["scores"]:
                        # vector addition to the total score
                        self.total_scores += np.array(q["scores"][answer])
                        break
                    print("Invalid choice. Please enter a valid letter or option name.")

            self.show_results()

        def show_results(self):
            print("\n" + "=" * 45)
            print("FINAL SCORE BREAKDOWN")
            print("=" * 45)

            for name, score in zip(self.mechanisms, self.total_scores):
                print(f"  {name:<25}: {score} points")

            max_score = np.max(self.total_scores)
            # search for mechanisms with the maximum score
            winners = [
                self.mechanisms[i]
                for i, score in enumerate(self.total_scores)
                if score == max_score
            ]

            print("-" * 45)
            print(f"Most likely mechanism(s): {', '.join(winners)}")
            print("=" * 45)

    quiz = StuckPipeQuiz(questions_data, MECHANISMS)
    quiz.run_quiz()

else:
    print("\nProgram exited. Have a great day!")
