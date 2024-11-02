def calculate_average(numbers):
    if len(numbers) == 0:  # Check if the list is empty
        return 0  # Return 0 or handle empty list as needed

    total = sum(numbers)  # Calculate the sum of the list
    average = total / len(numbers)  # Calculate the average
    return average  # Return the average value

# Example usage:
numbers_list = [10, 20, 30, 40, 50]
average_value = calculate_average(numbers_list)
print(f"The average is: {average_value}")
