import random

def random_number_easy():
    nums = [1, 2, 3]
    return str(random.choice(nums))


#!!!!!!!!GENERATE RANDOM MEDIUM DIFFICULTY DIFFRENTIATION AND INTEGRATION QUESTIONS
def easy_question():
    # Generate random polynomial
    polynomial = random_number_easy()+"x^"+random_number_easy()+" + "+random_number_easy()
    # Remove "0x^" and the number after it
    if "0x^" in polynomial:
        index = polynomial.index("0x^")
        end_index = polynomial.index(" ", index)
        polynomial = polynomial[:index] + polynomial[end_index+3:]

    # Remove "1" before "x"
    if "1x^" in polynomial:
        polynomial = polynomial.replace("1x^", "x^")

    # Remove "^1"
    if "^1 " in polynomial:
        polynomial = polynomial.replace("^1 ", " ")

    string1 = "'easy' : Differentiate the function: f(x) = "
    string2 = "'easy' : Integrate the function: f(x) = "
    random_string = random.choice([string1, string2])
    print(random_string + polynomial)
    return polynomial


def random_number_med():
    nums = [1, 2, 3, 4, 5, 6]
    return str(random.choice(nums))


#!!!!!!!!GENERATE RANDOM MEDIUM DIFFICULTY DIFFRENTIATION AND INTEGRATION QUESTIONS
def med_question():
    # Generate random polynomial
    polynomial = random_number_med()+"x^"+random_number_med()+" + "+random_number_med()+"x^"+random_number_med()+" + "+random_number_med()+"x^"+random_number_med()+" + "+random_number_med()
    # Remove "0x^" and the number after it
    if "0x^" in polynomial:
        index = polynomial.index("0x^")
        end_index = polynomial.index(" ", index)
        polynomial = polynomial[:index] + polynomial[end_index+3:]

    # Remove "1" before "x"
    if "1x^" in polynomial:
        polynomial = polynomial.replace("1x^", "x^")

    # Remove "^1"
    if "^1 " in polynomial:
        polynomial = polynomial.replace("^1 ", " ")

    string1 = "'medium' : Differentiate the function: f(x) = "
    string2 = "'medium' : Integrate the function: f(x) = "
    random_string = random.choice([string1, string2])
    print(random_string + polynomial)
    return polynomial


def random_number_lower():
    nums = [-3,-2,-1,0,0.5]
    return str(random.choice(nums))
def random_number_upper():
    nums = [1,1.5 ,2, 3, 4]
    return str(random.choice(nums))

#!!!!!!!!GENERATE RANDOM MEDIUM DIFFICULTY DIFFRENTIATION AND INTEGRATION QUESTIONS
def hard_question():
    a = easy_question()
    b = med_question()
    c = random_number_lower()
    d = random_number_upper()
    string1 = "'hard' : Differentiate the function: f(x) = " + a + " from first principals."
    string2 = "'hard' : Integrate the function: f(x) = " + a + " between the limits " + c + " and " + d
    random_string = random.choice([string2])
    return random_string, a, c, d