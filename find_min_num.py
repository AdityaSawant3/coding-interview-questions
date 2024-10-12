def find_min(items):
	min_num = 0
	for i in range(1, len(items)):
		if items[i-1] < items[i]:
			if items[i-1] <= 0:
				pass
			else:				
				min_num = items[i-1]
	return min_num

item_list = [6, 4, -2, 5, 1, 9, -7, 0]
min_number = find_min(item_list)
print(f"Minimum number in list is: {min_number}")