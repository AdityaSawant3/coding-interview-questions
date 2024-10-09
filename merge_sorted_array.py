# Time Complexity : O(n1 + n2) 
# Auxiliary Space : O(n1 + n2)

class MergeSortedArray:

	def __init__(self, arr1, arr2):
		self.arr1 = arr1
		self.arr2 = arr2

	def merge_sort(self):
		i = 0
		j = 0
		k = 0

		arr1_len = len(self.arr1)
		arr2_len = len(self.arr2)

		arr3 = []

		while (i < arr1_len and j < arr2_len):
			if (self.arr1[i] < self.arr2[j]):
				arr3.append(self.arr1[i])
				i += 1
			else:
				arr3.append(self.arr2[j])
				j += 1

		
		# If there are remaining Copy elements
		while i < arr1_len:
			arr3.append(self.arr1[i])
			i += 1

		while j < arr2_len:
			arr3.append(self.arr2[j])
			j += 1

		return arr3

if __name__ == "__main__":
	array1 = [1, 3, 5]
	array2 = [2, 4, 6]

	merge = MergeSortedArray(array1, array2)
	print(f"Merged sorted array is {merge.merge_sort()}")
