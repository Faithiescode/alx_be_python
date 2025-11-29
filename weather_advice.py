user_input = str(input("what is the weather like today\n(sunny/rainy/cold)?: "))

if user_input == 'sunny':
  print("wear a t-shirt and sunglasses")
elif user_input == 'rainy':
  print("Don't forget your umbrella and a raincoat.")
elif user_input == 'cold':
  print("Make sure to wear a warm coat and a scarf.")
  
else:
  print("sorry i dont have any recommendation for this weather")