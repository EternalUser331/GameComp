# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 12:20:15 2020

@author: user
"""

import random 
import time

isRunning = True 



def main () :
    print("WonderField")
    loopQuestions()
    
    
main()

questions = ["Год рождения Льва Толстова?"]
FalseAnswers = [["1829", "1838", "1825"]]
TrueAnswers = { 
        0 : "1828"
        }

def ChooseRandomQuestion():
    index = random.randint(0, len(questions)) - 1
    return index














def displayAnswers(index) : 
    
    print("Possible answers : ")
    curAnswers = [TrueAnswers.index].append(FalseAnswers[0])
    curAnswers = curAnswers.sort()
    return curAnswers


def displayQuestion(index) : 
    print(index)
    print("Get ready for answering ... ")
    question = questions[index]
    time.sleep(1)
    print(question)
    answers = displayAnswers(index)
    

def questionManager () : 
    ChosenQuestion = ChooseRandomQuestion()
    print(ChosenQuestion)
    displayQuestion(ChosenQuestion)
    


def loopQuestions ():
    while isRunning:
        questionManager()
