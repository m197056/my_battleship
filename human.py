

import ship, game_board, sprites
from random import randint
from typing import List, Tuple, Optional


class Human:
    """ A human player"""

    def __init__(self):

        # list of ship objects
        self._my_ships: List[ship.Ship] = []
        # list of (row,col) coordinates for misses
        self._my_misses: List[Tuple[int, int]] = []
        # list of (row,col) coordinates for hits
        self._my_hit: List[Tuple[int, int]] = []

        # list of ship objects
        self._sunk_ships: List[ship.Ship] = []
        # list of (row,col) coordinates
        self._their_misses: List[Tuple[int, int]] = []
        # list of (row,col) coordinates for their hits
        self._their_hits: List[Tuple[int, int]] = []

        # the board matrix is a 10x10 structure with
        # pointers to ship objects. Initialize to all
        # None values- no ships are on the board
        self._board_matrix: List[List[Optional[ship.Ship]]] = [[None] * 10 for _ in range(10)]

        # set to True if all opponent's ships are sunk
        self.complete: bool = False

    def initialize(self):
        """ Create a valid ship layout
        This function populates
        _my_ships and _board_matrix

        Ship Type  | Length
        -----------|-------
        Carrier    |   5
        Battleship |   4
        Cruiser    |   3
        Submarine  |   3
        Destroyer  |   2

        * the ship type is just FYI, it is not used in the game *
        """

        # 1.) create ship of the given length at a random (row,col)
        #     position either horizontal or vertical
        # 2.) check if this conflicts with any of the other ships by
        #     by making sure that every entry in _board_matrix is None
        # 2b.) If the ship is not valid, retry step 1
        # 3.) If the ship is valid set the appropriate elements _board_matrix array
        #     equal to the ship
        # Example: to place a vertical destroyer at C2:
        #    board_matrix[2][2] = my_ship
        #    board_matrix[3][2] = my_ship

        for ship_length in [5, 4, 3, 3, 2]:
            valid_place = False
            while not valid_place:
                # --------- BEGIN YOUR CODE ----------
                hztlFlag = bool(randint(0, 1))  # True for horizontal, false for vertical

                if hztlFlag:
                    xloc = randint(0, 10 - ship_length)
                    yloc = randint(0, 9)
                    xend = xloc + ship_length - 1
                    xvals = range(xloc, xend + 1)
                    yvals = [yloc] * ship_length

                else:
                    xloc = randint(0, 9)
                    yloc = randint(0, 10 - ship_length)
                    yend = yloc + ship_length - 1
                    xvals = [xloc] * ship_length
                    yvals = range(yloc, yend + 1)

                valid = []

                for x in xvals:
                    for y in yvals:
                        if self._board_matrix[y][x] is None:
                            valid.append('Yes')
                        else:
                            valid.append('No')

                if 'No' in valid:
                    valid_place = False
                else:
                    valid_place = True
                    my_ship = ship.Ship(ship_length, yloc, xloc, not hztlFlag)
                    self._my_ships.append(my_ship)
                    for x in xvals:
                        for y in yvals:
                            self._board_matrix[y][x] = my_ship


            # --------- END YOUR CODE ----------

    def print_board(self):
        """
        Print the player's board as text, useful for debugging
        """

        print("=" * 10)
        for row in self._board_matrix:
            for entry in row:
                if entry is None:
                    print("_", end="")
                else:
                    print(entry.length, end="")
            print("")
        print("=" * 10)

    def draw(self, my_board: game_board.GameBoard, their_board: game_board.GameBoard):

        """ Add sprites to the game board's to indicate
        ship positions, guesses, hits, etc """

        for my_ship in self._my_ships:
            my_ship.draw(my_board)
