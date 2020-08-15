def transform_string (list_name):
    try:
        string_transformed =''  
        for i in range(0, len(list_name)-1):
            string_transformed += list_name[i] + ", "   
        string_transformed += "and " + list_name[-1]
    except IndexError:
        print("List empty")

    return string_transformed

list_1 = ['cat', 'dog', 'rabbit', 'turtle']
print(transform_string(list_1))





