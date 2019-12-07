#!/usr/bin/env python
# coding: utf-8

# In[57]:


import Mastermindv2
import unittest

class TestLength(unittest.TestCase):
    
    def test_wrong_code_length(self):
        self.assertEqual(Mastermindv2.wrong_code_length(['1', '2', '4', '3']), False)
        self.assertEqual(Mastermindv2.wrong_code_length(['1', '2', '4', '5', '4']), True)
        self.assertEqual(Mastermindv2.wrong_code_length(['1', '2']), True)
        

#2nd unit test
class TestCharacters(unittest.TestCase):
    
    def test_wrong_characters(self):
        self.assertEqual(Mastermindv2.wrong_characters(['1', '2', '4', '3']), False)
        self.assertEqual(Mastermindv2.wrong_characters(['b', 'e', 'e', 'p']), True)
        self.assertEqual(Mastermindv2.wrong_characters(['1','a', 'b', 'c']), True)

#3rd unit test

class TestAttempt(unittest.TestCase):
    
    def test_get_code_breaker_attempt(self):
        self.assertEqual(Mastermindv2.get_code_breaker_attempt(), Mastermindv2.generate_code())

#4th unit test
    def test_check_order(self):
        self.assertEqual(Mastermindv2.check_order(['1', '1', '2', '4'], ['1', '1', '2', '4']), 4)
        self.assertEqual(Mastermindv2.check_order(['1', '1', '2', '4'], ['2', '1', '3', '4']), 2)
        self.assertEqual(Mastermindv2.check_order(['2', '1', '2', '1'], ['3', '1', '4', '3']), 1)
        
        
#5th unit test
    
    def test_get_key_pegs(self):
        self.assertEqual(Mastermindv2.get_key_pegs(1, 2),  ['Red', 'Red', 'Empty', 'Empty'])
        self.assertEqual(Mastermindv2.get_key_pegs(3, 4), ['Red', 'Red', 'Red', 'Red'])
        self.assertEqual(Mastermindv2.get_key_pegs(4, 3),  ['Red', 'Red', 'Red', 'White'])
        


        
unittest.main(argv=[''], verbosity=2, exit=False) # magic line that runs all your unit tests


# In[58]:


#integration test
import unittest
import Mastermindv2

class TestMastermind(unittest.TestCase):
    def test_wrong_code_length(self):
        self.assertEqual(Mastermindv2.wrong_code_length(['1', '2', '4', '3']), False)
        self.assertEqual(Mastermindv2.wrong_code_length(['1', '2', '4', '5', '4']), True)
        self.assertEqual(Mastermindv2.wrong_code_length(['1', '2']), True)
        
    def test_wrong_characters(self):
        self.assertEqual(Mastermindv2.wrong_characters(['1', '2', '4', '3']), False)
        self.assertEqual(Mastermindv2.wrong_characters(['b', 'e', 'e', 'p']), True)
        self.assertEqual(Mastermindv2.wrong_characters(['1','a', 'b', 'c']), True)
        
    #encapsulates first 3 functions
    def test_get_code_breaker_attempt(self):
        self.assertEqual(Mastermindv2.get_code_breaker_attempt(), Mastermindv2.generate_code())
        
    def test_check_numbers(self):
        self.assertEqual(Mastermindv2.check_numbers(['1', '1', '2', '4'], ['1', '1', '2', '4']), 4)
        self.assertEqual(Mastermindv2.check_numbers(['1', '1', '2', '4'], ['2', '1', '3', '4']), 3)
        self.assertEqual(Mastermindv2.check_numbers(['2', '1', '2', '1'], ['3', '1', '4', '1']), 2)
        
    def test_check_order(self):
        self.assertEqual(Mastermindv2.check_order(['1', '1', '2', '4'], ['1', '1', '2', '4']), 4)
        self.assertEqual(Mastermindv2.check_order(['1', '1', '2', '4'], ['2', '1', '3', '4']), 2)
        self.assertEqual(Mastermindv2.check_order(['2', '1', '2', '1'], ['3', '1', '4', '3']), 1)
            
    def test_get_key_pegs(self):
        self.assertEqual(Mastermindv2.get_key_pegs(1, 2),  ['Red', 'Red', 'Empty', 'Empty'])
        self.assertEqual(Mastermindv2.get_key_pegs(3, 4), ['Red', 'Red', 'Red', 'Red'])
        self.assertEqual(Mastermindv2.get_key_pegs(4, 3),  ['Red', 'Red', 'Red', 'White'])

        
        

