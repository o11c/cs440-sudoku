test: stupid monkey brains searchNxN ;
%:
	./$@.py < puzzle.sudoku

doc:
	cd write_up && pdflatex sudoku.tex
