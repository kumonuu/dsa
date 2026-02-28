def function(num):
    sum_ = 0
    for i in range(1,num+1):
        sum_ += i
    return sum_

print(function(10))

def recursive_function(num):
    if num <= 1:
        return num
    return recursive_function(num-1) + num

print(recursive_function(10))

def normal_factorial(num):
    product = 1
    for i in range(1,num+1):
        product *= i
    return product

print(normal_factorial(3))
        
def recursive_factorial(num):
    if num <= 1:
        return num
    return recursive_factorial(num-1) * num

print(recursive_factorial(3))

def normal_exponentiation(num1,num2):
    return pow(num1,num2)

print(normal_exponentiation(3,2))

def recursive_exponentiation(num1,num2):
    if num2 == 0:
        return 1
    return num1 * recursive_exponentiation(num1,num2-1)
    
print(recursive_exponentiation(3,2))