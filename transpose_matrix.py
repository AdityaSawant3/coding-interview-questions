# Transpose of Matrix

class Transpose_of_Matrix:

	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

	def take_input(self):
		for i in range(self.rows):
			for j in range(self.cols):
				data = int(input(f"Enter the data at matrix[{i}][{j}]: "))
				self.matrix[i][j] = data

	# Time Complexity: O(M * N)
	# Space Complexity: O(M * N)
	def find_transpose1(self):
		transpose_matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
		for i in range(self.rows):
			for j in range(self.cols):
				transpose_matrix[i][j] = self.matrix[j][i]
		self.print_matrix(transpose_matrix)


	# Time Complexity: O(N ** 2)
	# Space Complexity: O(1)
	def find_transpose2(self):
		# transpose_matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
		for i in range(self.rows):
			for j in range(i+1, self.cols):
				self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
		self.print_matrix(self.matrix)

	def print_matrix(self, matrix):
		for i in matrix:
			print(i)


if __name__ == "__main__":
	rows = int(input("How main rows do you want: "))
	columns = int(input("How main cloumns do you want: "))
	T = Transpose_of_Matrix(rows, columns)
	T.take_input()
	T.find_transpose1()
	T.find_transpose2()