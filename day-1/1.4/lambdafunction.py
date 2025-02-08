# Lambda function to classify a number as "Positive", "Negative", or "Zero"
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

# Test the lambda function with different values
print("Result for 1:", n(1))      # Positive number
print("Result for -3:", n(-3))    # Negative number
print("Result for 0:", n(0))      # Zero

# Lambda function to calculate the square of a number
sqrt = lambda x: x ** 2

# Test the lambda function to find the square of 4
print("Square of 4:", sqrt(4))
