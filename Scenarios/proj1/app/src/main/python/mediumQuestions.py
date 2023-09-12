import random
def random_number_med():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
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

    string1 = "Differentiation"
    string2 = "Integration"
    random_string = random.choice([string1, string2])
    return polynomial, random_string