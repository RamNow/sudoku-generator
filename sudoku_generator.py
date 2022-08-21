# !/usr/bin/python
import sys
from Sudoku.Generator import *


def main() -> None:
    # setting difficulties and their cutoffs for each solve method
    difficulties = {
        'easy': (35, 5),
        'medium': (81, 15),
        'hard': (81, 20),
        'extreme': (81, 30),
        'insane': (81, 40),
    }

    # getting desired difficulty from command line
    difficulty_key = sys.argv[2]
    logical_cutoff, random_cutoff = difficulties[difficulty_key]

    # constructing generator object from puzzle file (space delimited columns, line delimited rows)
    file = sys.argv[1]
    gen = Generator(file)

    # applying 100 random transformations to puzzle
    gen.randomize(100)

    # getting a copy before slots are removed
    initial = gen.board.copy()

    # applying logical reduction with corresponding difficulty cutoff
    gen.reduce_via_logical(logical_cutoff)

    # catching zero case
    if random_cutoff != 0:
        # applying random reduction with corresponding difficulty cutoff
        gen.reduce_via_random(random_cutoff)

    # getting copy after reductions are completed
    final = gen.board.copy()

    # printing out complete board (solution)
    print("The initial board before removals was: \r\n\r\n{0}".format(initial))

    # printing out board after reduction
    print("The generated board after removals was: \r\n\r\n{0}".format(final))

    # solve the sudoku puzzle and print out the solution
    solver = Solver(final)
    solver.solve()
    print("The solution to the puzzle is: \r\n\r\n{0}".format(solver.board))


if __name__ == '__main__':
    main()
