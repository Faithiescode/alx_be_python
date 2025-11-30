user_input = True
while user_input:
  num1 = int(input("Please enter the first number:"))
  num2 = int(input("Please enter the second number:"))
  operator = str(input("Please choose the operator (+, -, *, /):"))
  #special_number = 0

  match operator:
    case '+':
      result = num1 + num2
      print(f"The result is {result}\n", end="")
    case '-':
      result = num1 - num2
      print(f"The result is {result}\n", end="")
    case '*':
      result = num1 * num2
      print(f"The result is {result}\n",end="")
    case '/':
      if num2 != 0:
        result = num1/num2
        print("The result is {result}", end="")
      else:
        print("cannot be divisible by 0")
    case _:
      print("invalid selection")
        
        