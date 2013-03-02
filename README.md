Benjamin Longbons,
Eric Klinginsmith,
Sebastian Sanchez

Included Files:

cs440-sudoku:
1) brains.py
2) monkey.py
3) stupid.py
4) searchNxN.py
5) sudokuSolver.py
7) README

cs440-sudoku/stats:
1) searchNxNEasy.pdf
2) Top90SearchNxN.pdf
3) Top90Brains.pdf

cs440-sudoku/write_up:
1) sudoku.pdf

About the project:
This was a group project between the members listed in the header. The project
was to solve Sudoku puzzles using a search type algorithm. In addition a short
paper has been provided as a write-up for what we did to solve this problem.
There are four different implementations these are:

1) stupid
2) monkey
3) brains
4) searchNxN

How to run:
To run the implementations use sudlkuSolver.py. Do not use the the
implementation files by themselves! Instead type
"sudokuSolver.py -flag < inputFile" on the command line. -flag is a given flag,
a, b, c, or d to select the implementation you want to use and inputFile is a
text file containting one or more sudoku puzzles. If you do not include the inputFile
then you will be propted for one. If no flags are given then a help message
will be supplied.