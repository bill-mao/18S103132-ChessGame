
import unittest
import sys
sys.path.append("./src")
from Game import *

class TestChessBoard(unittest.TestCase):

    def setUp(self):
        print("start test ChessBoard")
        self.board = ChessBoard()

    def tearDown(self):
        print("finish test ChessBoard")

    def test_isEnd2(self):
        print("error name")
        self.board._ChessBoard__winner = 3
        self.assertEqual(self.board.isEnd(), True)

    def test_move(self):
        act = ChessAction(ChessPlayer(Piece.Color.white, self.board), Piece.Color.white, 'king', ChessPosition('04'), ChessPosition('05'))
        self.board.move(act)
        self.assertEqual(self.board.board[0][5].getKind(), ChessPiece.Kind.king, 'check move king success')


if __name__ == "__main__":
    unittest.main()