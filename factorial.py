class Factorial:

	# Time Complexity: O(n)
	# Space Complexity: O(n)
	def factorial_using_recursion_approach(self, num):
		if num == 1:
			return num
		return num * self.factorial_using_recursion_approach(num - 1)

	# Time Complexity: O(n)
	# Space Complexity: O(1)
	def factorial_using_iterative_approach1(self, num):
		i = num
		while i != 1:
			i -= 1
			num *= i
		return num

	# Time Complexity: O(n)
	# Space Complexity: O(1)
	def factorial_using_iterative_approach2(self, num):
		fact = 1
		for i in range(2, num+1):
			num *= fact
			fact += 1
		return num

if __name__ == "__main__":

	factorial = Factorial()
	print(factorial.factorial_using_recursion_approach(4))
	print(factorial.factorial_using_iterative_approach1(4))
	print(factorial.factorial_using_iterative_approach2(4))