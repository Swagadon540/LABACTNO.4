#laman loob
def check_number(num):
    if num % 2 == 0:
        print(f"{num} is an Even number.")
    else:
        print(f"{num} is an Odd number.")

#main q
num = int(input("Enter a number: "))
check_number(num)