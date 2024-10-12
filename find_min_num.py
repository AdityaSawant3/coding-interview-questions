# Time Complexity: O(n)
# Space Complexity: O(1)
def find_min(items):
	min_num = items[0]
	for i in range(1, len(items)):
		if min_num <= 0 or items[i] <= 0:
			pass
		else:
			if min_num < items[i]:				
				pass
			else:
				min_num = items[i]
	return min_num

item_list = [6, 4, -2, 5, 9, -7, 0, 1]
min_number = find_min(item_list)
print(f"Minimum number in list is: {min_number}")