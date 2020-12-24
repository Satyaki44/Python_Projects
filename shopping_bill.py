sum = 0
while(True):
    user=input("Enter the item price or press q to quit:")
    if(user != "q"):
        sum=sum+int(user)
        print(f"Your total order cost till now is {sum}")
    else:
        print(f"Your total bill is {sum}. \n Thank you for shopping with us")
