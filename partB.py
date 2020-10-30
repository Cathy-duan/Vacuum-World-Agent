import sys
import random
import copy

def main():
	N = 5					
	data = sys.stdin.readlines()
	[grid,moves,initial] = database(data) 
	row = int(initial[0])			
	column = int(initial[1])
	n = 0
	for x in range(moves):
		dirt = float(grid[row][column])
		boundary= [0,0,0,0]
		if column == 0:
			boundary[0] = -1
		else:
			boundary[0] = float(grid[row][column-1])
		if row == 0:
			boundary[1] = -1
		else:
			boundary[1] = float(grid[row-1][column])
		if column == len(grid[0])-1:
			boundary[2] = -1
		else:
			boundary[2] = float(grid[row][column+1])
		if row == len(grid)-1:
			boundary[3] = -1
		else:
			boundary[3] = float(grid[row+1][column])
		action = greedy(dirt, boundary)
		if action == 'S':
			n = n + dirt
			grid[row][column] = format(float(0))
		elif action == 'L':
			column = column - 1
		elif action == 'U':
			row = row - 1
		elif action == 'R':
			column = column + 1
		elif action == 'D':
			row = row + 1
		print(action,format(float(n),'.15'))		
		if ((x+1)%N==0):			
			copy.deepcopy(grid)[row][column] = '[' + grid[row][column]+']'
			for y in range(len(copy.deepcopy(grid))):
				for z in range(len(copy.deepcopy(grid)[0])):
					print(copy.deepcopy(grid)[y][z],end=" ")
				print ("\n")
	print (moves," moves are over")

def database(data):
	for line in data:
		if 'GRID' in line:
			break
	
	if (line.split()[0]!='GRID:'):
		print("Data is not correct")
		return [0,0,0]
	else:
		try:
			rows = int(line.split()[1])
		except ValueError:
			print("Value Error for number of rows")
		try:
			columns = int(line.split()[2])
		except ValueError:
			print("Value Error for number of columns")
	for i in range(len(data)):
		line = data[i]
		if 'DIRT' in line:
			gridstart = i+1
			break
	grid = []
	for i in range(rows):
		for j in range(len(data[gridstart+i].split())):
			data[gridstart+i].split()[j] = format(float(data[gridstart+i].split()[j]),'.16')
		grid.append(data[gridstart+i].split())
	for line in data:
		if 'MOVES' in line:
			break
	
	moves = int(line.split()[1])
	for line in data:
		if 'INITIAL' in line:
			break
	
	initial = [int(line.split()[1])-1, int(line.split()[2])-1]
	return [grid, moves, initial]

def greedy(dirt,boundary):
	if dirt>0:
		return 'S'
	else:
		sequence = []
		dirt = max(boundary)
		if boundary[0] == dirt:
			sequence.append('L')
		if boundary[1] == dirt:
			sequence.append('U')
		if boundary[2] == dirt:
			sequence.append('R')
		if boundary[3] == dirt:
			sequence.append('D')
	action = random.choice(sequence)
	return action
		

	
if __name__ =="__main__":
	main()
