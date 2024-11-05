def sum_of_squares(numbers): 
    # Bug: Incorrectly sums numbers instead of their squares
    return sum(numbers)  # This should be sum(n**2 for n in numbers)

if __name__ == "__main__":  # Bug: Incorrect variable name _name_ and _main_
    test_numbers = [1, 2, 3, 4]
    
    # Tiny extra implementation: Print the squares of the numbers
    squares = [n**2 for n in test_numbers]
    print("Squares of the numbers:", squares)
    
    print("Sum of squares:", sum_of_squares(test_numbers))  # Expected output: 30, but returns 10
