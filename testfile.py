import unittest
from unittest.mock import patch
from quiz import QuizGame, main

class TestQuizGame(unittest.TestCase):
    @patch("builtins.input", side_effect=["123", "John Doe"] + [""] * 10)
    def test_main(self, mock_input):
        with self.assertRaises(SystemExit):
            main()

    @patch("builtins.input", side_effect=["Paris", "Minnie", "Green"])  # Example inputs for testing
    def test_play_game(self, mock_input):
        quiz = QuizGame([
            ("What is the capital of France?", "Paris"),
            ("Who is Mickey Mouse's girlfriend?", "Minnie"),
            ("What is the color of an apple?", "Green"),
        ], num_questions=3)
        quiz.play_game("123", "John Doe")
        self.assertEqual(quiz.num_questions, 3)
        self.assertGreaterEqual(quiz.score, 0)
        self.assertLessEqual(quiz.score, 3)

    @patch("builtins.input", side_effect=["Paris", "Minnie", "Green"])  # Example inputs for testing
    def test_ask_question_correct(self, mock_input):
        quiz = QuizGame([
            ("What is the capital of France?", "Paris"),
            ("Who is Mickey Mouse's girlfriend?", "Minnie"),
            ("What is the color of an apple?", "Green"),
        ])
        quiz.ask_question("What is the capital of France?", "Paris")
        self.assertEqual(quiz.score, 1)

    @patch("builtins.input", side_effect=["London", "Mickey", "Blue"])  # Example inputs for testing
    def test_ask_question_incorrect(self, mock_input):
        quiz = QuizGame([
            ("What is the capital of France?", "Paris"),
            ("Who is Mickey Mouse's girlfriend?", "Minnie"),
            ("What is the color of an apple?", "Green"),
        ])
        quiz.ask_question("What is the capital of France?", "Paris")
        self.assertEqual(quiz.score, 0)

if __name__ == "__main__":
    unittest.main()
