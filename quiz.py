import random
import sys

class QuizGame:
    def __init__(self, questions, num_questions=10):
        self.num_questions = min(num_questions, len(questions))
        self.score = 0
        self.questions = random.sample(questions, self.num_questions)

    def ask_question(self, question, correct_answer):
        user_answer = input(f"{question}: ") or ""  # Default to an empty string if user input is None
        user_answer_lower = user_answer.lower()  # Convert user's answer to lowercase

        if user_answer_lower == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

    def play_game(self, student_id, student_name):
        print(f"Welcome, {student_name} (ID: {student_id}), to the Quiz Game!")

        for question, correct_answer in self.questions:
            self.ask_question(question, correct_answer)

        print(f"\nYour final score is: {self.score}/{self.num_questions}")
        if self.score == self.num_questions:
            print("Congratulations! You got all the questions right!")
        else:
            print("Better luck next time!")

def main():
    # Define a list of questions as tuples (question, correct_answer)
    questions = [
        ("What is the capital of France?", "Paris"),
        ("Who is Mickey Mouse's girlfriend?", "Minnie"),
        ("What is the color of an apple?", "Red"),
        ("How many fingers does a typical human have on one hand?", "Five"),
        ("What comes after Monday?", "Tuesday"),
        ("How many legs does a cat have?", "Four"),
        ("What is the opposite of 'day'?", "Night"),
        ("What do you use to write on paper?", "Pencil"),
        ("What is the capital of the United States?", "Washington, DC"),
        ("What is the largest planet in our solar system?", "Jupiter"),
        ("How many colors are there in a rainbow?", "Seven"),
        ("What is the capital of England?", "London"),
        ("Which animal says 'moo'?", "Cow"),
        ("What is the shape of a traffic stop sign?", "Octagon"),
        ("How many sides does a triangle have?", "Three"),
        ("What do bees collect from flowers?", "Nectar"),
        ("What is the smallest prime number?", "Two"),
        ("What is the opposite of 'happy'?", "Sad"),
        ("Which planet is closest to the Sun?", "Mercury"),
        ("What is the currency of Japan?", "Yen"),
    ]

    # Get student ID and name
    student_id = input("Enter your student ID: ").strip()
    student_name = input("Enter your name: ").strip()

    quiz = QuizGame(questions, num_questions=10)
    quiz.play_game(student_id, student_name)
    # Explicitly raise SystemExit with the appropriate exit code
    raise SystemExit(0)

if __name__ == "__main__":
    import sys
    sys.exit(main())
