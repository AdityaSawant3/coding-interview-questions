def fibonacci_series_func(num):
	first = 0
	second = 1
	items = []
	i = 0
	while i != num:
		hold = first + second
		items.append(hold)
		first = second
		second = hold
		i += 1
	return items

if __name__ == "__main__":
	fibonacci_series = fibonacci_series_func(10)
	print(fibonacci_series)