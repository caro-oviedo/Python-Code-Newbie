import random 
from irregularverbs import irregular_verbs 

verbs = irregular_verbs()

for test_set in range (5):
    #Create the quiz and asnwer key files
    test_file = open(f'irregularsquiz{test_set + 1}.txt', 'w')
    answer_key_file = open(f'irregularsquiz_answers{test_set + 1}.txt', 'w')

    #write out the header for the quiz
    test_file.write('Name: \n\nDate: \n\n')
    test_file.write(f"------- IRREGULAR VERBS TEST ------- SET {test_set + 1} \n")
    test_file.write("\n\n")

    #Shuffle the order of the verbs
    infinitives = list(verbs.keys())
    random.shuffle(infinitives)

    test_file.write("What's the past tense of the following verbs? \n")

    #Loop through all the verbs, making a question for each. 
    for  verb_number in range(80):
        correct_answer = verbs[infinitives[verb_number]]

        test_file.write(f"{verb_number + 1 }. {infinitives[verb_number]} \n")
        
        correct_answer = verbs[infinitives[verb_number]]
        answer_key_file.write(f"{verb_number + 1}. {correct_answer} \n")
    
    test_file.close()
    answer_key_file.close()

