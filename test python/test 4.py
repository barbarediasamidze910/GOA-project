moms_name = str(input("enter your moms name: "))
dads_name = str(input("enter your dads name: "))
grandma_name = str(input("enter your grandmas name: "))
grandpas_name = str(input("enter your grandpas name: "))
family = [grandma_name,dads_name,grandpas_name,moms_name]
number = int(input("enter a number from 0-3: "))
if number == 0:
    print(family[0])
elif number == 1:
    print(family[1])
elif number == 2:
    print(family[2])
elif number == 3:
    print(family[3])
else:
    print("that number cannot be submmited")