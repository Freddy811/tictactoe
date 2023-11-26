import unittest
from tictactoe import check_winner, is_game_board_full

class TestTicTacToe(unittest.TestCase):
    def test_check_winner(self):
        board1 = [['X', 'O', 'X'],
                  ['O', 'X', 'O'],
                  ['X', ' ', 'O']]
        self.assertTrue(check_winner(board1))

        board2 = [['O', 'O', 'X'],
                  ['X', 'X', 'O'],
                  ['O', 'X', ' ']]
        self.assertFalse(check_winner(board2))

        board3 = [['X', 'O', 'X'],
                  ['O', 'X', 'O'],
                  ['X', 'O', 'X']]
        self.assertTrue(check_winner(board3))

        board4 = [['X', 'O', 'X'],
                  ['O', 'X', 'O'],
                  ['O', 'X', 'O']]
        self.assertFalse(check_winner(board4))

    def test_is_board_full(self):
        board1 = [['X', 'O', 'X'],
                  ['O', 'X', 'O'],
                  ['X', 'O', 'X']]
        self.assertTrue(is_game_board_full(board1))

        board2 = [['X', 'O', 'X'],
                  ['O', 'X', 'O'],
                  ['X', ' ', 'X']]
        self.assertFalse(is_game_board_full(board2))

        board3 = [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]
        self.assertFalse(is_game_board_full(board3))

if __name__ == '__main__':
    unittest.main()