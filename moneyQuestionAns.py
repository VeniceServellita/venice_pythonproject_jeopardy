"""
Name: Venice Servellita
Class: CS521 01 - Summer 1 2018
Date: 06/22/2018
Description:

This module contains the MoneyQuestAnsCat class which holds the contents of 
the JEOPARDY_CSV.csv file, in particular the questions, answers, money values
and categories.
"""


class MoneyQuestAnsCat:  # class to hold contents of JEOPARDY_CSV.file
    
    def __init__(self): # constructs and initializes MoneyQuestAnsCat
        self.__amount = 0
        self.__question = None
        self.__answer = None
        self.__category = None

    def set_amount(self, amount):  # sets the money value of each question
        self.__amount = amount[1:].replace(',', '') # removes $ and commas 

    def set_question(self, question): # sets the question
        self.__question = question

    def set_answer(self, answer): # sets the answer
        # removes special characters such as ", (, and ) in some answers ---
        #  these make user's answers incorrect even if the text is correct
        self.__answer = answer.replace('"', '').replace('(','').replace(')','')

    def set_category(self, category): # sets the category
        self.__category = category

    def get_amount(self):  #gets the money value 
        return self.__amount

    def get_question(self): # gets the question
        return self.__question

    def get_answer(self): # gets the answer
        return self.__answer

    def get_category(self): # gets the category
        return self.__category

    def __repr__(self):  # evaluatable string representation of the object 
        return "Amount: " + str(self.__amount) + " Category: \
 " + self.__category + " Question: " + self.__question + " Answer: \
 " + self.__answer
    