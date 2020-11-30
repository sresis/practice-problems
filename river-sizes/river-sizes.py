def riverSizes(matrix):
	sizes = []
	x = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 1:
				x = dfs(matrix, i, j)
				sizes.append(x)
	return sizes

def dfs(matrix, x, y):
	if x >= len(matrix) or y >= len(matrix[0]) or x < 0 or y < 0 or matrix[x][y] != 1:
		return 0
	matrix[x][y] = 0
	return 1 + dfs(matrix, x+1, y) + dfs(matrix, x-1, y) + dfs(matrix, x, y-1) + dfs(matrix, x, y+1)