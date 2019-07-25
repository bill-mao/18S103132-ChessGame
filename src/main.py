from enum import Enum


class Piece:
    Color = Enum('colors', ('white', 'black'))

    def __init__(self, color, kind):
        self._color = color
        self._kind = kind

    def getColor(self):
        return self._color

    def getKind(self):
        return self._kind


class GoPiece(Piece):
    def __init__(self, color):
        super().__init__(color, kind='same')


class ChessPiece(Piece):
    Kind = Enum('kinds', ('king', 'queen', 'rook', 'bishop', 'knight', 'pawn'))

    # def __init__(self, color, kind):
    #     super().__init__(color, kind)


class Position:
    def __init__(self, string):
        self.x = int(string[0])
        self.y = int(string[1])

    def check(self):
        pass


class GoPosition(Position):
    def __ini__(self, string):
        self.x = int(string[:2])
        self.y = int(string[2:])

    def check(self):
        return self.x > -1 and self.x < 18 and self.y > -1 and self.y < 18


class ChessPosition(Position):
    def check(self):
        return self.x > -1 and self.x < 8 and self.y > -1 and self.y < 8


class Board:
    def printBoard(self):
        pass

    def move(self, action):
        pass

    def isEnd(self):
        pass

    def winner(self):
        pass


class ChessBoard(Board):
    def __init__(self):
        self.__winner = None
        self.__whiteKing = ChessPiece(ChessPiece.Color.white, ChessPiece.Kind.king)
        self.__blackKing = ChessPiece(ChessPiece.Color.black, ChessPiece.Kind.king)
        self.actionList = []

        self.board = [[None] * 8 for i in range(8)]
        self.board[0][0] = ChessPiece(ChessPiece.Color.white, ChessPiece.Kind.rook)
        self.board[0][1] = ChessPiece(ChessPiece.Color.white, ChessPiece.Kind.knight)
        self.board[0][2] = ChessPiece(ChessPiece.Color.white, ChessPiece.Kind.bishop)
        self.board[0][3] = ChessPiece(ChessPiece.Color.white, ChessPiece.Kind.queen)
        self.board[0][4] = self.__whiteKing
        self.board[0][5] = ChessPiece(ChessPiece.Color.white, ChessPiece.Kind.bishop)
        self.board[0][6] = ChessPiece(ChessPiece.Color.white, ChessPiece.Kind.knight)
        self.board[0][7] = ChessPiece(ChessPiece.Color.white, ChessPiece.Kind.rook)
        self.board[1][:] = [ChessPiece(
            ChessPiece.Color.white, ChessPiece.Kind.pawn) for i in range(8)]

        self.board[7][0] = ChessPiece(ChessPiece.Color.black, ChessPiece.Kind.rook)
        self.board[7][1] = ChessPiece(ChessPiece.Color.black, ChessPiece.Kind.knight)
        self.board[7][2] = ChessPiece(ChessPiece.Color.black, ChessPiece.Kind.bishop)
        self.board[7][3] = ChessPiece(ChessPiece.Color.black, ChessPiece.Kind.queen)
        self.board[7][4] = self.__blackKing
        self.board[7][5] = ChessPiece(ChessPiece.Color.black, ChessPiece.Kind.bishop)
        self.board[7][6] = ChessPiece(ChessPiece.Color.black, ChessPiece.Kind.knight)
        self.board[7][7] = ChessPiece(ChessPiece.Color.black, ChessPiece.Kind.rook)
        self.board[6][:] = [ChessPiece(
            ChessPiece.Color.black, ChessPiece.Kind.pawn) for i in range(8)]

        self.printBoard()

    def printBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                p = self.board[i][j]
                if p is None:
                    print('++++++\t', end='')
                    continue
                prefix = '白' if p.getColor() == p.Color.white else '黑'
                print(prefix + str(p.getKind().name) + '\t', end='')
            print()

    # return bool
    def move(self, action):
        if self.board[action.pos2.x][action.pos2.y] == self.__blackKing:
            self.__winner = 'white'
        if self.board[action.pos2.x][action.pos2.y] == self.__whiteKing:
            self.__winner = 'black'
        self.board[action.pos2.x][action.pos2.y] = self.board[action.pos1.x][action.pos1.y]
        if action.pos1.x != action.pos2.x and action.pos1.y != action.pos2.y:
            self.board[action.pos1.x][action.pos1.y] = None
        self.printBoard()
        return True

    def isEnd(self):
        return self.__winner is not None

    def winner(self):
        return self.__winner


class GoBoard(Board):
    def __init__(self, ):
        self.__countWhite = 0
        self.__countBlack = 0
        self.SIZE = 18

        self.board = [[None] * self.SIZE for i in range(self.SIZE)]
        self.printBoard()

    def getCount(self):
        return self.__countBlack, self.__countWhite

    def move(self, action):
        posLi = action.positions
        pieceColor = action.color
        if action.kind == 'lift':
            for p in posLi:
                self.board[p.x][p.y] = None
        elif action.kind == 'place':
            self.board[posLi[0].x][posLi[0].y] = GoPiece(pieceColor)

        self.printBoard()
        return True

    def isEnd(self):
        return True if self.__countBlack + self.__countWhite >= self.SIZE else False

    def winner(self):
        if self.__countWhite == self.__countBlack:
            return "Tie"
        return Piece.Color.white if self.__countWhite > self.__countBlack else Piece.Color.black

    def printBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                p = self.board[i][j]
                if p is None:
                    print('++\t', end='')
                    continue
                prefix = '白' if p.getColor() == p.Color.white else '黑'
                print(prefix + '\t', end='')
            print()


class Rule:
    def __init__(self, board):
        self.board = board

    def check(self, action):
        pass


class ChessRule(Rule):
    # override
    '''piece -- player b,w
    overboard
    existed piece; or None '''

    def check(self, action):
        board = self.board
        # player piece same color?
        if action.player.color != action.color:
            print("please move your color piece")
            return False
        # overstep the boundary? 
        if not action.pos1.check() or not action.pos2.check():
            print("overstep the boundary")
            return False
        # not exist
        if board.board[action.pos1.x][action.pos1.y] is None:
            print("this position doesn't have a piece")
            return False
        return True


class GoRule(Rule):

    def check(self, action):
        board = self.board
        kind = action.kind
        # player piece same color?
        if action.player.color != action.color and kind == 'place':
            print("please place your color piece")
            return False
        # player piece same color?
        if action.player.color == action.color and kind == 'lift':
            print("please lift other's color piece")
            return False

        if kind == 'place':
            # not exist
            if board.board[action.positions[0].x][action.positions[0].y] is not None:
                print("this position already have a  piece")
                return False
        else:
            # not exist
            for p in action.positions:
                if board.board[p.x][p.y] is None:
                    print("this position doesn't have a piece")
                    return False

        # overstep the boundary?
        for p in action.positions:
            if not p.check():
                print("overstep the boundary")
                return False

        return True


class Action:
    def __init__(self, player, color, kind):
        self.player = player
        self.kind = kind
        self.color = color


class ChessAction(Action):
    def __init__(self, player, color, kind, pos1, pos2):
        super().__init__(player, color, kind)
        self.pos1 = pos1
        self.pos2 = pos2
        # eat piece?


class GoAction(Action):
    def setPositions(self, positions):
        self.positions = positions


class Player:
    def __init__(self, color, board):
        self.color = color
        self.board = board

    def myTurn(self):
        pass


class ChessPlayer(Player):

    def myTurn(self, ):
        move = ''
        # *** input check, where check action should be 
        # pawn check 
        # action check
        while True:
            print("player:", self.color.name, "please input your instruction")
            move = input()
            # input check 
            # digit check
            if not move.isdigit() or len(move) != 4:
                print("player:", self.color.name, "input format error, please input correct instruction")

                continue
            p1, p2 = ChessPosition(move[:2]), ChessPosition(move[2:])
            # position check
            if not p1.check() or not p2.check():
                print("player:", self.color.name, "input format error, please input correct instruction")

                continue
            act = ChessAction(self, self.color, 'move', p1, p2)
            return act

class GoPlayer(Player):
    def myTurn(self):
        while True:
            print("player:", self.color.name, "please input your instruction like "+ \
                  "start with 0 is place piece, 1 is lift piece;  positions every two digit")
            move = input()
            # input check
            # digit check
            if not move.isdigit() :
                print("player:", self.color.name, "input format error, please input correct instruction")

                continue

            kind = 'place' if move.startswith('0') else 'lift'
            posLi = []
            if kind == 'place':
                posLi = [GoPosition(move[1:5])]
            else:
                for i in range(1, len(move), 4):
                    posLi.append((GoPosition(move[i:i+4])))

            # position check
            # if not p1.check() or not p2.check():
            #     print("player:", self.color.name, "input format error, please input correct instruction")
            #
            #     continue
            color = self.color if kind == 'place' else \
                Piece.Color.white if self.color == Piece.Color.black else Piece.Color.black
            act = GoAction(self, color, kind)
            act.setPositions(posLi)
            return act


class Game:
    def __init__(self, gameName):
        self.gameName = gameName
        print("start a ", gameName)

    def start(self):
        pass


class MyChessAndGoGame(Game):
    def __init__(self):
        Game.__init__(self, 'Chess game')

    def start(self):
        while True:
            print("welcome to play my game. you can play either Chess or Go int this game ")
            print("enter 'go' or 'chess' to start a game, enter 'end' to terminate game loop.")
            # flag = input()
            # todo 
            flag = 'go'
            if 'end' == flag:
                print("You have ended the game.")
                break
            if 'chess' == flag:
                board = ChessBoard()
                rule = ChessRule(board)
                player1 = ChessPlayer(ChessPiece.Color.black, board)
                player2 = ChessPlayer(ChessPiece.Color.white, board)
                while not board.isEnd():
                    while True:
                        # input check is in myTurn() fuc
                        act1 = player1.myTurn()
                        if not rule.check(act1):
                            print("action error")
                            continue
                        board.move(act1)
                        # board.printBoard()
                        break
                    if not board.isEnd():

                        while True:
                            act2 = player2.myTurn()
                            if not rule.check(act2):
                                print("action error")
                                continue
                            board.move(act2)
                            # board.printBoard()
                            break
                print('the winner is ', board.winner())

            if 'go' == flag:
                board = GoBoard()
                rule = GoRule(board)
                player1 = GoPlayer(Piece.Color.black, board)
                player2 = GoPlayer(Piece.Color.white, board)
                while not board.isEnd():
                    while True:
                        # input check is in myTurn() fuc
                        act1 = player1.myTurn()
                        if not rule.check(act1):
                            print("action error")
                            continue
                        board.move(act1)
                        # board.printBoard()
                        break
                    if not board.isEnd():
                        while True:
                            act2 = player2.myTurn()
                            if not rule.check(act2):
                                print("action error")
                                continue
                            board.move(act2)
                            # board.printBoard()
                            break
                print('the winner is ', board.winner())



if __name__ == "__main__":
    MyChessAndGoGame().start()
