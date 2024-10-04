# Two Sum. Level-Easy

arr = [0, -1, 2, -3, 1]
target_num = -2

# Not an Efficient method.
# Time Complexity: O(n**2)
# Space Comlexity: O(1)
def two_sum_func1(arr, target):
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if arr[i] + arr[j] == target:
				return True
	return False

print(two_sum_func1(arr, target_num))

# Time Complexity: O(n(log(n)))
# Space Comlexity: O(1)
def binary_search(arr, low, high, target):
	while low <= high:
		mid = low + (high - low) // 2
		if arr[mid] == target:
			return True
		elif arr[mid] < target:
			high = mid - 1
		else:
			low = mid + 1
	return False

def two_sum_func2(arr, target):
	arr.sort()
	for i in range(len(arr)):
		check_this_value = arr[i] - target
		complement = binary_search(arr, i+1, len(arr)-1, check_this_value)
		if complement:
			return True
	return False

print(two_sum_func2(arr, target_num))

# Two Pointer technique
# Time Complexity: O(n(log(n)))
# Space Comlexity: O(1)
def two_sum_func3(arr, target):
	arr.sort()
	left = 0
	right = len(arr)-1

	while left <= right:
		sum = arr[left] + arr[right]
		if sum == target:
			return True
		elif sum < target:
			left += 1
		else:
			right -= 1
	return False

print(two_sum_func3(arr, target_num))
