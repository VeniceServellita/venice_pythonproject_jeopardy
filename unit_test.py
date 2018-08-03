"""
Name: Venice Servellita
Class: CS521 01 - Summer 1 2018
Date: 06/22/2018
Description:
This module will perform unit tests
"""
    
from moneyQuestionAns import MoneyQuestAnsCat

def unit_test():
    """Sample unit test"""
    
    mqac = MoneyQuestAnsCat()
    mqac.set_amount('$1,000')
    mqac.set_question("question")
    mqac.set_answer('"answer" (answer1)')
    mqac.set_category("category")
    assert (mqac.get_amount() == '1000'), "Incorrect amount"
    assert (mqac.get_question() == "question"), "Incorrect question"
    assert (mqac.get_answer() == "answer answer1"), "Incorrect answer"
    assert (mqac.get_category() == "category"), "Incorrect category"
    assert (mqac.__repr__() == "Amount: 1000 Category:  category Question: question Answer:  answer answer1"), "Incorrect repr"
    print("All tests pass")
    
unit_test()



