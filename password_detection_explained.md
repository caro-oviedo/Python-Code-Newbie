# Strong Password Detection (Regular Expressions)  
![Website](https://img.shields.io/website?label=License&style=flat-square&up_color=blue&up_message=Apache%202.0&url=http%3A%2F%2Fwww.apache.org%2Flicenses%2FLICENSE-2.0.html)


> Disclaimer: I'm a code newbie learning Python. I know there are better ways of solving this problem but this is my best shot at it so far. 


## The problem 

This is a variation of a project exercise from the book  [Automate the Boring Stuff](https://nostarch.com/automatestuff2) in which we have to write a function —using regular expressions— that checks whether a password is strong or not.     

[You can find the complete code here](https://github.com/caro-oviedo/Python-Code-Newbie/blob/master/is_valid_password_detection.py)


## Variation 
If a password is not strong, I thought it would be better to let the user know why it's not strong enough. To do so, I read Python's docs to learn more about [regular expression operations](https://docs.python.org/3/library/re.html)  


### Creating the regular expression
1. I start creating the regular expression with the requirements the password needs to meet to be strong:   

    ```python
    pass_valid = re.compile(r'((?P<digit>\d)|(?P<Special>[!@#$%^&*])|(?P<uppercase>[A-Z])|(?P<lowercase>[a-z]))*') 

    ```

+ Here I group the requirements using `(?P<name>)` for each of the groups because later I'll use the `groupdict()` function, which returns a dictionary. The keys of this dictionary will be the name of the groups, and the values, the matches found. If there are no matches, the default value is `none`.   

### Validating the password   
1. First, I check  the password's length. If it is more than 8 characters long, I store the matches using `re.match()`  


    ```python
    if len(password)<8: 
        print("Password must be at least 8 characters long\n")       
    else:
        pass_matches = re.match(pass_valid, password) 
    ```   

2. I use `groupdict()` to create a dictionary with all the matches and the group names.   

    ```python
        conditions = []                                               
        for key,item in (pass_matches.groupdict()).items():            
            if item == None:                                            
            conditions.append(key)
     
    ```   


    + What I want to know now, is if there is a group that has a **none** value. This means that a requirement hasn't been met and since we used `(?P<name>)` in the regex we can know which that requirement is.  
    + The `for loop` looks for the matches that have **none** value and _appends_ the **keys** in a list called `conditions` (I'm just interested in the keys because they will give me the names of the requirements)

3. The `if-statement` prints the names of the groups that haven't been met —stored in `conditions`.  
    + If `conditions` is empty, then that means all the conditions have been met. The `else-statement` returns `False`, which I use to break out of the `while loop`.

    ```python
        if conditions:                                                     
        print("\nPassword must include these type of characters: ")
        for condition in conditions:                                  
            print(condition )                                          
        else:
            return False   
    ```   
    ```python
        while True: 
            user_password = input("Enter your password: (Press 'q' to quit at any time) ")
            if user_password =='q':
                break

            valid_password = _is_valid_password(user_password)
            if valid_password == False:                               
                print("Strong password")
                break  
    ```

          


[![Twitter Follow](https://img.shields.io/twitter/follow/Caro_Oviedo_?color=1DA1F2&logo=twitter&style=for-the-badge)](https://twitter.com/Caro_Oviedo_)

