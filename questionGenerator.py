"""
Name: Venice Servellita
Class: CS521 01 - Summer 1 2018
Date: 06/22/2018
Description:

This module contains the QuestionGenerator class which imports and reads the
pertinent data from JEOPARDY_CSV.csv file, and generates the questions list
using methods from the MoneyQuestAnsCat module. Questions containing external
links (as indicated by "a href") will be ignored. The module creates two lists,
regular and final, based on the Value column. Regular Jeopardy questions have
a $ value while and final Jeopardy questions are indicated by the word "None"
in the value column. The lists are shuffled in order to get random data.
One question from the final Jeopardy list will be added to the end of the
regular questions list.
"""

import csv
from random import shuffle
from moneyQuestionAns import MoneyQuestAnsCat

class QuestionGenerator:
    def __init__(self, num_questions):  # initializes the class
        self.question_list = self.__create_question_list(num_questions)
        self.total = 0

    def __should_ignore(self,amount, question):
        """ excludes questions containing external links"""
        if "a href" in question: 
            return True
        else:
            return False

    def __is_final(self, amount):
        """ distinguishes Final Jeopardy questions from regular questions"""
        if amount == "None":
            return True
        else:
            return False

    def __create_question_list(self, num_questions):
        """
        This function reads the csv file and creates an object using
        MoneyQuestionAns class to get the question, answer, amount and
        category. Two lists are generated - one list for regular Jeopardy
        questions and one list for Final Jeopardy questions. The lists
        are then shuffled to randomize and combined, the last element
        of the list is from the final Jeopardy questions list.
        """
        dataList = []  # holds the regular Jeopardy questions
        finalList = []  # holds the final Jeopardy questions

        with open("JEOPARDY_CSV.csv", "r", encoding="utf-8") as infile:
            reader = csv.reader(infile)
            next(reader)[1:]  # skips the header row

            for row in reader:  # scans each row

                m = MoneyQuestAnsCat() # creates an object 
                category = row[3]  # reads the category (column 3)
                amount = row[4]    # reads the amount (column 4)
                question = row[5]  # reads the question (column 5)
                answer = row[6]    # reads the answer ( column 6)
                if self.__should_ignore(amount, question): # excludes questions with "a href"
                    continue
                # sets the category, question and answer
                m.set_category(category) 
                m.set_question(question)
                m.set_answer(answer)

                if self.__is_final(amount):
                    finalList.append(m)   # appends data to finalList
                else:
                    m.set_amount(amount)
                    dataList.append(m)  # appends data to dataList

            # randomizes the lists                   
            shuffle(dataList)
            shuffle(finalList)

        # combines list, only one question from finalList is added to end of dataList           
        return dataList[:num_questions] + [finalList[0]] 
