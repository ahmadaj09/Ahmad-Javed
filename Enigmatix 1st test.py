# Question No 1

def fibnocci(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    else:
        return  fibnocci(n-1) + fibnocci(n-2)
while True:
    a = int(input("Enter the No: "))  
    if a == 00:
        break
    else:
        print(fibnocci(a))



# Question No 2

# For Loop
# --For Loop is used when we know the number of iteration

for i in range(10):
    print(i)

# While Loop
# -- While is used when we dont know the numbwer of iteration like unlimited iteration 
# -- In while loop we initailize the value first for limited no of iteration 

while True:
    inp = int(input("Enter the no: "))

    if inp == 00:
        break
    else:
        print("You are inside the while loop!")


# Do While

# In Python there is no do while loop 
# the main difference is in while loop the program run after satisfying the condition
# But in Do while program atleast run one time without checking the condition

i = 1
while i < 5:
    print(i)
    i+=1

# Question No 3

def find_second_largest(numbers):
    
    numbers = list(set(numbers))

   
    if len(numbers) < 2:
        return None
    largest = max(numbers)

    numbers.remove(largest)

    second_largest = max(numbers)
    return second_largest

numbers = [12, 67, 89, 65, 56]
result = find_second_largest(numbers)
print(f"The second largest number is: {result}")



# Question No 4

def remove_duplicates(lst):
    seen = set()  
    result = []   
    
    for item in lst:
        if item not in seen:
            result.append(item)  
            seen.add(item)      
    
    return result

numbers = [1,4,7,9,3,9,10,11,11,45]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)



# Question No 5

def factorial(no):
    if no == 1 or no == 0:
        return 1
    else:
        return no * factorial(no - 1)

num = 5
result = factorial(num)
print(f"Factorial of {num} is {result}")
