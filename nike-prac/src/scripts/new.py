def add_numbers(a, b):
	"""Return the sum of two numbers a and b."""
	return a + b
    
#want to writ python code to test the add_numbers function
if __name__ == "__main__":
	# Test cases for the add_numbers function
	print(add_numbers(2, 3))  # Expected output: 5
	print(add_numbers(-1, 1)) # Expected output: 0
	print(add_numbers(0, 0))  # Expected output: 0
	print(add_numbers(1.5, 2.5)) # Expected output: 4.0		


#want to write a function that multiplies two numbers
def add_numbers(a, b):
	"""Return the sum of two numbers a and b."""
	return a + b


def multiply_numbers(a, b):
	"""Return the product of two numbers a and b."""
	return a * b


if __name__ == "__main__":
	# Test cases for both functions
	print("add_numbers tests:")
	print(add_numbers(2, 3))   # Expected output: 5
	print(add_numbers(-1, 1))  # Expected output: 0
	print(add_numbers(0, 0))   # Expected output: 0
	print(add_numbers(1.5, 2.5))  # Expected output: 4.0

	print("multiply_numbers tests:")
	print(multiply_numbers(2, 3))    # Expected output: 6
	print(multiply_numbers(-1, 1))   # Expected output: -1
	print(multiply_numbers(0, 0))    # Expected output: 0
	print(multiply_numbers(1.5, 2.5))  # Expected output: 3.75
