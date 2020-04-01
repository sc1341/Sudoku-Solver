#!/usr/bin/env python3
#
# Sudoku Solver
# This is my version of a sudoku solver inspired by Computerphile's video


def is_possible(grid, x, y, n):
	# Checks columns and rows
	for i in range(0, len(grid)):
		if grid[i][y] == n or grid[x][i] == n:
			return False
	# Get the square coordinates by true dividing by 3 and multiplying by 3
	x0 = (x//3) * 3
	y0 = (y//3) * 3
	#Checks the square
	for i in range(0, 3):
		if grid[i+x0][y] == n or grid[x][y0+i] == n:
			return False
	return True
		
def solve(grid):
	## new grid of zeros to be filled in with the old grid
	#newgrid = [[0 for x in range(0, len(grid[0]))] for x in range(0, len(grid))]
	for x in range(0, len(grid)):
		for y in range(0, len(grid[x])):
			if grid[x][y] == 0:
				for i in range(1, len(grid[x])+1):
					if is_possible(grid, x, y, i):
						grid[x][y] = i
						solve(grid)
						# Backtracking 
						grid[x][y] = 0
				return
	for row in grid:
		print(row)
def main():
	grid = [[2, 3, 0, 4, 1, 5, 0, 6, 8], [0, 8, 0, 2, 3, 6, 5, 1, 9], [1, 6, 0, 9, 8, 7, 2, 3, 4], [3, 1, 7, 0, 9, 4, 0, 2, 5], [4, 5, 8, 1, 2, 0, 6, 9, 7], [9, 2, 6, 0, 5, 8, 3, 0, 1], [0, 0, 0, 5, 0, 0, 1, 0, 2], [0, 0, 0, 8, 4, 2, 9, 0, 3], [5, 9, 2, 3, 7, 1, 4, 8, 6]]
	solve(grid)


if __name__ == "__main__":
	main()

