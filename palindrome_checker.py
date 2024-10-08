class PalindromeChecker:
    def __init__(self, items):
        self.items = items

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def is_palindrome(self, string):
        # Clean the string: remove spaces and convert to lowercase
        result_string = ''.join(string.split()).lower()
        return result_string == result_string[::-1]

    # More Efficient method. Because it does not create new string.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def is_palindrome_using_pointer(self, string):
        result_string = ''.join(string.split()).lower()
        left = 0
        right = len(string)-1
        while (left <= right):
            if string[left] != string[right]:
                return False;
            left += 1
            right -= 1
        return True

    def print_list(self):
        for item in self.items:
            result = self.is_palindrome(item)
            print(f"{item} is palindrome: {result}")
        print()

    def print_list_another(self):
        for item in self.items:
            result = self.is_palindrome_using_pointer(item)
            print(f"{item} is palindrome: {result}")
        print()


if __name__ == "__main__":
    items = ["racecar", "hello", "A man a plan a canal Panama", "noon"]
    checker = PalindromeChecker(items)
    checker.print_list()
    checker.print_list_another()
