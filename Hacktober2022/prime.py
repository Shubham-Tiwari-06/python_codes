# Program to check if a number is prime or not


# To take input from the user
num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
else:
    #n=1 isn't prime
    flag=True
# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")