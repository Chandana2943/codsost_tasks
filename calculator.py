first_num = input("Enter your first number:")
sec_num = input("Enter your second number:")
opt = input("1. addition\n2. subtraction\n3. multiplication \n4. division\n5. square\nselect operation between two numbers\nChoose a number:")
if first_num.isdigit() and sec_num.isdigit() and opt.isdigit and int(opt) < 6 and int(opt) > 0:
 if int(opt) == 1:
    result= int(first_num) + int(sec_num)
    print("Result: ",result)
 elif int(opt) == 2:
    result= int(first_num) - int(sec_num)
    print("Result: ",result)
 elif int(opt) == 3:
    result= int(first_num) * int(sec_num)
    print("Result: ",result)
 elif int(opt) == 4:
    result= int(first_num) / int(sec_num)
    print("Result: ",result)
 elif int(opt) == 5:
    result= int(first_num) ** int(sec_num)
    print("Result: ",result)
else:
    print("you have entered incorrect value! ")