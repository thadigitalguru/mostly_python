from random import shuffle

class ChessBoard:

    def __init__(self, variant=""):
        self.variant = variant
        self.position = self._get_starting_position()

    def show_position(self):
        print(self.position)

    def _get_starting_position(self):
        if self.variant == "fischer960":
            return self._get_fischer960_position()
        else:
            return "RNBQKBNR"

    @staticmethod
    def _get_fischer960_position():
        pieces = ["R", "N", "B", "Q", "K", "B", "N", "R"]
        shuffle(pieces)
        return ''.join(pieces)

board = ChessBoard(variant="fischer960")
board.show_position()