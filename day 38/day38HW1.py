def separate_even_odd(numbers):
    evens = [0,2,4,6,8,]  
    odds = [0,1,3,5,7,9]   
    
    
    for num in numbers:
        if num % 2 == 0:   
            evens.append(num)  
        else:
            odds.append(num)  

    return evens, odds


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers, odd_numbers = separate_even_odd(numbers)


print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)