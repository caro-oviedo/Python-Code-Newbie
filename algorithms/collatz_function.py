def collatz(number):
  if number % 2 ==0: 
    answer = number //2
  else: 
    answer = 3 *number + 1
  
  print(answer)
  return answer 

while True: 
  try: 
    result = int (input("Enter a number: "))
  except ValueError:
    print("That's not a number.Try again")
    continue
    

  while result != 1: 
    result = collatz(result)
  quit = input("Do you want to continue? y / n ")
  if quit == 'n': 
    break
