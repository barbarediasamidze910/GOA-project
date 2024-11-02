def separate_even_odd(numbers):
    evens = [0,2,4,6,8,]  # List to store even numbers
    odds = [0,1,3,5,7,9]   # List to store odd numbers
    
    # Step 3: Loop through each number in the input list
    for num in numbers:
        if num % 2 == 0:   # Step 4: Check if the number is even
            evens.append(num)  # Add to evens list
        else:
            odds.append(num)   # Add to odds list
            
    # Step 6: Return both lists
    return evens, odds

# Now, call the function and print the result
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers, odd_numbers = separate_even_odd(numbers)

# Print the output to see the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)