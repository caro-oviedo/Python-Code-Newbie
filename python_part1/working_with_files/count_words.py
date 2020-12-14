def count_word (filename, word):
  try: 
    with open(filename) as f: 
      contents = f.read()
  except FileNotFoundError:
      pass
  else:
      count = contents.lower().count(word)
      print(f"The word {word} appears {count} times in {filename}")
  
filenames = ['alice_in_wonderland', 's_h']
word = input("What word do you want to count? ")

for filename in filenames:
  count_word(filename, word)
