class Search_Algorithm:

	# Time Complexity: O(n)
	# Spacec Complexity: O(1)
	def linear_search_func(self, items, target):
		for i in range(len(items)):
			if items[i] == target:
				return i
		return -1

	# Time Complexity: O(n log n)
	# Spacec Complexity: O(1)
	def binary_search_func(self, items, target):
		items.sort()
		left = 0
		right = len(items) - 1
		while left <= right:
			mid = left + (right - left) // 2 # Floor Division
			if items[mid] == target:
				return mid
			elif items[mid] < target:
				left = mid + 1
			else:
				right = mid - 1
		return -1

if __name__ == "__main__":

	item_list = [7, 2, 56, 23, 17, 75, 65, 89, 14, 36, 75]

	search = Search_Algorithm()

	linear_search_result = search1.linear_search_func(item_list, 17)
	print(f"Linear search result: {linear_search_result}")
	
	binary_search_result = search1.binary_search_func(item_list, 56)
	print(f"Binary search result: {binary_search_result}")