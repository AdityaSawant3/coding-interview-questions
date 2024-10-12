# Time Complexity: O(n)
# Space Complexity: O(1)
def find_max(items):
	max_num = items[0]
	for i in range(1, len(items)):
		if max_num > items[i]:
			pass
		else:
			max_num = items[i]
	return max_num


item_list = [6, 4, -2, 5, 12, 1, 9, -7, 0]
max_number = find_max(item_list)
print(f"Maximum number in list is: {max_number}")