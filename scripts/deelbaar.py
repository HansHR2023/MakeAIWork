

# Define the number eleven
number = 11

# As long as result is larger than zero:
while number > 0:
   # Subtract three
    number = number - 3
   # number -= 3 as an alternative

# Check if number is zero or not
if number == 0:
    # print result
    print("Number is divisible by 3")
else:
    print("Number is NOT divisible by 3")    




# Define the number eleven
numerator = int(input("What is the numerator?   "))
denominator = int(input("What is the denominator?   "))
numerator_org = numerator

# As long as result is larger than zero:
while numerator> 0:
   # Subtract three
    numerator -= denominator
   # number -= 3 as an alternative

# Check if number is zero or not
if numerator == 0:
    # print result
    print(f"The numerator {numerator_org} is divisible by {denominator}")
else:
    print(f"The numerator {numerator_org} is NOT divisible by {denominator}")    