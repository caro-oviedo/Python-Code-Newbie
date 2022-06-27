def recur(loopTimes, counter):
  if loopTimes > 0:
    print(f"This is loop iteration {counter}")
    recur(loopTimes -1, counter + 1)
  else: 
    print("The loop is complete")

def main():
  loopTimes = int(input("How many times would you like to repeat?\n"))
  counter = 1
  recur(loopTimes, counter)


main()
  
