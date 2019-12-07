#!/usr/bin/env python
# coding: utf-8

# In[10]:


import random

LENGTH_OF_CODE = 4

ALLOWED_CHARACTERS = ['1', '2', '3', '4']

def generate_code():
    """Returns secret code, which is a randomly generated four-element list of numbers between 1-4.
    
    """
    #iterates through a 4 element range and picks a random value from ALLOWED_CHARACTERS to add to a list after each iteration
    nums = [] 
    for i in range(LENGTH_OF_CODE):
        p =int(random.choice(ALLOWED_CHARACTERS)[:LENGTH_OF_CODE])
        nums.append((p))
    print((nums))
    
    
def wrong_code_length(code_breaker_attempt):
    """Returns True if the length of the code_breaker_attempt is not the allowed length set LENGTH_OF_CODE.
    Input: code_breaker_attempt - a list of any length
    Outputs: Boolean value to tell you whether of not the list is the right length for the game
    """
    if len(code_breaker_attempt) == LENGTH_OF_CODE:
        return False
    else:
        return True


def wrong_characters(code_breaker_attempt):
    """Returns True if code_breaker_attempt contains characters that are not allowed,
    which is set by ALLOWED_CHARACTERS.
    
    Input: code_breaker_attempt - a list of any length
    Outputs: Boolean value to tell you whether of not the list contains the right characters for the game (False- allowed : True- not allowed)
    """
    #iterates through each element in the attempt and checks if that element is an allowed character returning False for all allowed
    for i in code_breaker_attempt:
        if i not in ALLOWED_CHARACTERS:
            return True
    return False


def get_code_breaker_attempt():
    """The code breaker attempts to guess the secret code. This functions returns that attempt as a four-element list. This function also checks to make sure if the
    attempt is valid (the right length and using valid letters). If not, then it continues to ask for a valid answer until one is given."""
    #first step generates a code for the player of the right length and using valid characters
    code_breaker_attempt = []
    for i in range(LENGTH_OF_CODE):
        p =int(random.choice(ALLOWED_CHARACTERS)[:LENGTH_OF_CODE])
        code_breaker_attempt.append((p))

    
    #second step compares the player code to the game's code and returns the value when matching
    #trying to not make random code what we want
    while code_breaker_attempt == generate_code():
        return code_breaker_attempt 

    

def check_numbers(code, code_breaker_attempt):
    """ Checks if numbers guessed by the code breaker exist in the secret code. Returns the number of correct colors.
    
    Input: 2 lists, one of the mastermind code and one of the player attempt
    Output: number of correct colors
    """
    #matches is a copy of code
    ##by iterating through the attempt, the code will count each time it sees an element and remove it so that there's no double counting
    ###get the number of correct colors by subtracting the amount that dont match (which is what matches.remove in the if statement is) from the length of the code
    matches = code[:]
    for i in code_breaker_attempt:
        if matches.count(i) != 0:
            matches.remove(i)
    return LENGTH_OF_CODE-len(matches)

def check_order(code, code_breaker_attempt):
    """  Checks if numbers are in the same position as the corresponding number in the code. 
        Returns the number of colors in the correct position.
        
        Input: 2 lists, one of the mastermind code (code) and one of the player attempt (code_breaker_attempt)
        Output: number of correct numbers
    """  
    #converts strings in list to integers
    code_numbers = [int(i) for i in code]
    code_breaker_attempt_numbers = [int(j) for j in code_breaker_attempt]
    
    #checked gets rid of already searched values and gives you the number that match
    checked = LENGTH_OF_CODE
    for x in range(LENGTH_OF_CODE):
        match = abs(code_numbers[x]-code_breaker_attempt_numbers[x])
        if match > 0:
            checked -= 1
    return checked


def get_key_pegs(numbers_check, order_check):
    """
    Key pegs returns feedback to code breaker about how much of their code is correct.

    Red: Number is in the right position
    White: Number is in the wrong position
    Empty: Number (or duplicate of number) does not exist in the secret code.
    """
    ##shows number of red white and empty, should be 4 elements i.e ['Red', 'Red', "White", 'Empty'] for the codes that follow:
    ##gen - [1, 1, 2, 3] and attempt- [1, 1, 3, 4]

    
    empty = 0

    for i in range(LENGTH_OF_CODE):
    
        num_reds = order_check * ['Red']
    
        num_whites = (numbers_check - order_check) * ['White']
        
        num_empties = (LENGTH_OF_CODE - len(num_reds)- len(num_whites)) * ['Empty']

    return num_reds + num_whites + num_empties


def give_player_feedback(key_pegs):
    """Lets the player know how close they are to guessing the random code"""
    
    print(str(key_pegs.count("Red")) + " Red")
    print(str(key_pegs.count('White')) + ' White')
    print(str(key_pegs.count('Empty')) + ' Empty')

MAX_ATTEMPTS = 10

def mastermind():
    games = 1
    while games:
        games+=1
    if generate_code() < 10:
        return False
    else:
        return True
    if 'Red' == 4:
        return 'win'
    elif 'Red' != 4:
        return code


# In[ ]:




# In[ ]:




