def power2(number):
    
    if (number == 0):
        return False
    if ((number & (~(number - 1))) == number):
        return True
    return False

number = int(input("Enter the number : "))

if(power2(number)):
    print("\nThe number is power of 2")
else:
    print("\nThe number is not power of 2")