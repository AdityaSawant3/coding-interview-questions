
def find_lowest_missing(items):
	for i in range(1, len(items)):
		element = items[i-1]
		if element < 0 or items[i] < 0:
			continue
		else:
			if element+1 == items[i]:
				continue
			else:
				return element+1

def find_highest_missing(items):
	for i in range(len(items)-1, -1, -1):
		element = items[i]
		if element < 0 or items[i] < 0:
			continue
		else:
			if element-1 == items[i]:
				continue
			else:
				return element-1


list_items = [-6, 5, 3, 9, 4, 10, 2, 8, 12]
list_items.sort()
print(f"List: {list_items}")
lowest_missing_element = find_lowest_missing(list_items)
print(f"Lowest missing element in list the is {lowest_missing_element}.")
highest_missing_element = find_highest_missing(list_items)
print(f"Highest missing element in list the is {highest_missing_element}.")