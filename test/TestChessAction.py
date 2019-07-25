import sys
import os 
sys.path.append(os.path.abspath('./src'))
print(os.path.abspath('..'))
print(os.listdir())
from Game import *
import unittest

class TestChessAction(unittest.TestCase):

    def setUp(self):
        print("start test ChessAction")
        self.board = ChessBoard()
        player = ChessPlayer(Piece.Color.white, self.board)
        self.act = ChessAction(player, Piece.Color.white, 'king', ChessPosition('04'), ChessPosition('05'))


    def tearDown(self):
        print("finish test ChessAction")

    def test_init(self):
        self.board.move(self.act)
        self.assertEqual(self.board.board[0][5].getKind(), ChessPiece.Kind.king, 'check move king success')
        # with self.assertRaises(Exception):
        #     pass


if __name__ == "__main__":
    unittest.main()