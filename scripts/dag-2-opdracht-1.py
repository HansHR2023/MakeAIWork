print((512-282)/(47*48+5))


asknumber = int(input("Enter a number:   "))
print("The square of " + str(asknumber) + " is " + str(asknumber * asknumber))


import random
x = random.randint(1,50)
y = random.randint(2,5)
print(pow(x,y))


x = int(input("Enter the first number X:   "))
y = int(input("Enter the second number Y:   "))
print("Bereken: |x-y|/(x+y)")
print(abs(x-y)/(x+y))


a = str(input("Enter some words:   "))
print(len(a))
for i in range(0,10):
    print(a)
print(a[0])
print(a[0:3])
print(a[-3:])
print(a[::-1])
if a[2] in a:
    print(a[2])
else:
    print("The string does not contain a 7th sense")

print(a[1:-1])
print(a.upper())
print(a.replace("a","e"))

# replace every letter, not every character => use isalpha
for i in range(len(a)):
    a.replace(a[i]," ")
