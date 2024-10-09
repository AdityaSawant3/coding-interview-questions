class Find_Duplicates:

	# 1st Approach:
	# Time Complexity: O(n)
	# Space Complexity: O(n)
	def find_duplicates_using_set(self, list_items):
		s = set()
		list1 = []
		for item in list_items:
			if item in s:
				list1.append(item)
			else:
				s.add(item)
		print(list1)

find_duplicate = Find_Duplicates()

if __name__ == "__main__":
	lists = [2, 3, 5, 2, 8, 34, 1, 23, 34, 5]
	find_duplicate.find_duplicates_using_set(lists)