from board import Board
from field import Field
import random

b = Board()
b.clean_board()
Field(2, 2, False).bomb = True
b.print_board()
