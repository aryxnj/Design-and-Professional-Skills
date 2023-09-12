import numpy as np
import random
from main import run, userValid, runInte, userValidInte
def randomQuestionGenerator():
    # Define the coefficients of the polynomial
    randomArr = []
    randomLength = random.randint(1, 5)
    for x in range (randomLength):
        randomArr.append(random.randint(1, 5))
    p = np.array(randomArr)
    return p


    # Compute the derivative of the polynomial
    dpdx = np.polyder(p)

    print(dpdx)
    return list(dpdx)

def convert(string):
    listStr = string.split("x")
    for x in range(len(listStr)):
        try:
            listStr[x] = int(listStr[x])
        except ValueError as e:
            listStr[x] = 1
    return listStr
def run1():
    a = list(randomQuestionGenerator())
    string1 = "Find differential of y = "
    # for x in range(0, len(a)):
    #     if x == len(a)-1:
    #         string1 += str(a[x]) + "x" + "<sup>" + str((len(a) - 1) - x) + "</sup>"
    #     else:
    #         string1 += str(a[x]) + "x" + "<sup>" + str((len(a) - 1) - x) + "</sup>" + " + "
    # return string1
    string1 = ""
    for x in range(0, len(a)):
        if x == len(a)-1:
            string1 += str(a[x]) + "x" + "^" +str((len(a) - 1) - x)
        else:
            string1 += str(a[x]) + "x" + "^" + str((len(a) - 1) - x) + " + "
    return string1
def returnQuestion(a):
    string1 = ""
    for x in range(0, len(a)):
        if x == len(a)-1:
            string1 += str(a[x]) + "x" + "^" +str((len(a) - 1) - x)
        else:
            string1 += str(a[x]) + "x" + "^" + str((len(a) - 1) - x) + " + "
    return string1
def userValidation(question, userAnswer, diffInt):
    try:
        if diffInt == "Differentiation":
            print("IN DIFF")
            print(f"initial user answer: {userAnswer}")
            questionSolution = run(question)
            print(questionSolution)
            userAnswer1 = userValid(userAnswer)
            print("userAnswer" + str(userAnswer1))
            if questionSolution == userAnswer1:
                print("true")
                return "True"
            else:
                print("not true")
                return str(questionSolution)
        else:
            print("IN INTTT")
            questionSolution = userValidInte(runInte(question))
            userAnswer = userValidInte(userAnswer)
            if questionSolution == userAnswer:
                print("true")
                return "True"
            else:
                print("not true")
                return str(questionSolution)
    except:
        print("doesnt work")