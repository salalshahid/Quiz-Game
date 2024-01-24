import unittest
from unittest.mock import patch
from quiz import QuizGame, main

class TestFunctionalQuizGame(unittest.TestCase):
    @patch("builtins.input", side_effect=["123", "John Doe", "Paris"] * 10)
    def test_full_game_flow(self, mock_input):
        with self.assertRaises(SystemExit):
            main()

    @patch("builtins.input", side_effect=["123", "John Doe", "Paris"] * 10)
    def test_full_game_scoring(self, mock_input):
        with patch("builtins.print") as mock_print:
            with self.assertRaises(SystemExit):
                main()

        # Extracting the printed output to check the scoring
        printed_output = [call[0][0] for call in mock_print.call_args_list]
        score_line = printed_output[-2]  # Assuming the score line is the second-to-last line

        # Extracting the score from the printed output
        score_position = score_line.find("Your final score is: ") + len("Your final score is: ")
        score = int(score_line[score_position:].split('/')[0].strip())

        # Asserting that the score is within the expected range
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 10)

if __name__ == "__main__":
    unittest.main()
