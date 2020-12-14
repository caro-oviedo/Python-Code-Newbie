def widest_colum(list_name): 
    """ Finds the longest word in each sublist. 
    Returns a list with the width of each column.""" 

    col_witdths = [0] * len(list_name) 

    i = 0
    for column in list_name:
        longest_word = 0

        for word in column:
            if len(word) > longest_word:
                longest_word = len(word)
         
        col_witdths[i] = longest_word
        i += 1
    
    return col_witdths

def longest_word(list_name): 
    """Stores the number of rows. """
    long_word = [0] * len(list_name)  #Stores number of items in each sublist

    i = 0
    for column in list_name:  #counts words in each sublist
        l_word = 0

        for word in column: 
            l_word += 1
        long_word[i] = l_word
        i += 1
    return max(long_word) #Returns number of  rows to print



def print_table(list_name):
    """Prints the table with x right justification style"""

    column_widths = widest_colum(list_name) 
    number_rows = longest_word(list_name)
    
    for i in range(number_rows):
        for j in range(len(list_name)):
            try:
             print(list_name[j][i].rjust(column_widths[j]), end=' ')
            except IndexError: 
                print("-".rjust(column_widths[j]), end=' ') #Print - if the are no elements.
        print("")
             

        
        

table_data = [['apples', 'oranges', 'cherries', 'banana'], 
['alice', ' bob', 'carol'], 
['dogs', 'cats', 'moose', 'goose']   
]


print_table(table_data)