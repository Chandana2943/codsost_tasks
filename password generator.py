import random
length = input("Enter length of password:")
password= "".join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$_&') for _ in range(int(length)))
print(password)