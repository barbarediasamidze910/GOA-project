def calculate_average(numbers):
    if len(numbers) == 0:  
        return 0  

    total = sum(numbers)  
    average = total / len(numbers)  
    return average  


numbers_list = [10, 20, 30, 40, 50]
average_value = calculate_average(numbers_list)
print(f"The average is: {average_value}")
