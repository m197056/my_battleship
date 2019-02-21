
import ship, game_board, sprites
import string
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
        self._my_hits: List[Tuple[int, int]] = []
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

    def guess(self, row, col) -> Tuple[int, Optional[ship.Ship]]:
        """
        Tell the other player whether a row and column guess is a hit or miss.
        Record the (row,col) guess in either self._their_hits or self._their_misses

        If a space is guessed twice do not hit the ship twice. That's cheating :)

        Returns a tuple of (status, ship) where
            status = 0: miss
                   = 1: hit
                   = 2: sunk

            ship   = None if a hit or miss
                   = ship object if sunk

        """
        my_ship: ship.Ship = self._board_matrix[row][col]

        # if my_ship is None the guess is a miss, otherwise its a hit

        # --------- BEGIN YOUR CODE ----------

        # Hit logic:
        # make sure this is a *new* hit (no double guesses)
        # add to _their_hits
        # hit the ship
        # check if ship is sunk
        # return either (1,None) or (2,my_ship)

        # Miss logic:
        # add to _their_misses
        # return (0, None)

        # --------- END YOUR CODE ----------


    def take_turn(self, opponent):
        """
        Prompt the user to guess a row and column. The user should enter a lower case letter
        followed by a number. Updates self._my_hits, self._my_misses, and self._sunk_ships
        """

        # --------- BEGIN YOUR CODE ----------

        # 1.) Prompt user for a guess. Valid input would be a string like c,4
        #     If the guess is not valid ask the user to enter another guess

        # 2.) Call opponent.guess() to check wether the guess is a hit or miss

        # 3.) Update my_hits, my_misses, and sunk_ships accordingly

        # 4.) If the sunk_ships array has 5 ships in it set self.complete to True

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
        for miss in self._their_misses:
            my_board.add_sprite(sprites.miss, miss)
        for hit in self._their_hits:
            my_board.add_sprite(sprites.hit, hit)

            # draw hit indicators on their board
        for miss in self._my_misses:
            their_board.add_sprite(sprites.miss, miss)
        for their_ship in self._sunk_ships:
            their_ship.draw(their_board)
        for hit in self._my_hits:
            their_board.add_sprite(sprites.hit, hit)
