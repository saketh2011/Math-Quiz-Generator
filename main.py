ask = input("What level of math would you like?(copy paste: Algebra 1, Algebra 2, Geometry): ")

print("READ THIS PLEASE! Before the quiz(es) start, make sure to use / for division, * for multiplication, ^ for exponent, sqrt for (√ ), + for addition, - for subtraction, the imaginary unit as i, and write the plus/minus sign as +-. Moreover, all answers are expected exact and simplified unless specifically asked for. Do not write x=, just write the answer! Desmos is permitted for Algebra 1, but for Geometry or Algebra 2, only the TI-84 or a different advanced calculator is permitted. Good luck!")

score = 0

if str(ask) == "Algebra 1":
    print("okay")
# Algebra 2 Quizzes
elif str(ask) == "Algebra 2":
    y = int(input("Which unit?(dont include word Unit): "))
    # Unit 2 Algebra 2
    if int(y) == 2:
        print("Unfortunately, since unit 2 of Algbra 2 is mainly focused on graphing, we do not have a quiz. However, we can supply a practice packet with 10 questions, mimicking our quiz-style. Here it is: ")
    # Unit 3 Algebra 2
    if int(y) == 3:
        print("ABSOLUTE VALUES QUIZ:")
        # Unit 3 Question 1 Algebra 2
        unit3_q1_alg2 = input("-5=|8-x|-11, find x, and seperate with commas, and go from decreasing to increasing order: ")
        if str(unit3_q1_alg2) == "2,14" or str(unit3_q1_alg2) == "2, 14":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is 2,14")
        # Unit 3 Question 2 Algebra 2
        unit3_q2_alg2 = input("16|r-5| = -32: ")
        if str(unit3_q2_alg2) == "undefined" or str(unit3_q2_alg2) == "Undefined" or str(unit3_q2_alg2) == "No Solution" or str(unit3_q2_alg2) == "No solution" or str(unit3_q2_alg2) == "no solution" or str(unit3_q2_alg2) == "no Solution":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is undefined/no solution")
        # Unit 3 Question 3 Algebra 2
        unit3_q3_alg2 = input("-3(2p+8)<-4(2p+6) (include p in this problem): ")
        if str(unit3_q3_alg2) == "p<0" or str(unit3_q3_alg2) == "p < 0" or str(unit3_q3_alg2) == "p <0" or str(unit3_q3_alg2) == "p< 0":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is p<0")
        # Unit 3 Question 4 Algebra 2
        unit3_q4_alg2 = input("What is the interval notation of -3y+8<=-7 or 10y-3 <= -33 (copy paste:∞): ")
        if str(unit3_q4_alg2) == "(-∞,3] U [5,∞)" or str(unit3_q4_alg2) == "(-∞,3]U[5,∞)" or str(unit3_q4_alg2) == "(-∞,3]U [5,∞)" or str(unit3_q4_alg2) == "(-∞,3] U[5,∞)":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is (-∞,3] U [5,∞)")
        # Unit 3 Question 5 Algebra 2
        unit3_q5_alg2 = input("Find 4|9-3n|-9<75 in interval notation (copy paste:∞): ")
        if str(unit3_q5_alg2) == "(-4,10)" or str(unit3_q5_alg2) == "-4,10" or str(unit3_q5_alg2) == "-4, 10" or str(unit3_q5_alg2) == "(-4, 10)":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is (-4,10)")
        # Unit 3 Question 6 Algebra 2
        unit3_q6_alg2 = input("What is the interval notation of -1-4|x+9|<=-21 (copy paste:∞): ")
        if str(unit3_q6_alg2) == "(-∞,-14] U [-4,∞)" or str(unit3_q6_alg2) == "(-∞,-14]U [-4,∞)" or str(unit3_q6_alg2) == "(-∞,-14] U[-4,∞)" or str(unit3_q6_alg2) == "(-∞,-14]U[-4,∞)":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is (-∞,-14] U[-4,∞)")
        # Unit 3 Question 7 Algebra 2
        unit3_q7_alg2 = input("What is the vertex for the function 2/3|x+1|-1: ")
        if str(unit3_q7_alg2) == "(-1,1)" or str(unit3_q7_alg2) == "(-1, 1)" or str(unit3_q7_alg2) == "-1,1" or str(unit3_q7_alg2) == "-1, 1":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is (-1,1)")
        # Unit 3 Question 8 Algebra 2
        unit3_q8_alg2 = input("Would the function be shaded up or down, y<|x+4|-6: ")
        if str(unit3_q8_alg2) == "down" or str(unit3_q8_alg2) == "Down":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is Down")
        # Unit 3 Question 9 Algebra 2
        unit3_q9_alg2 = input("|3-x| + |x+1| = 4. Write in interval notation: ")
        if str(unit3_q9_alg2) == "[-1,3]" or str(unit3_q9_alg2) == "[-1, 3]":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is [-1,3]")
        # Unit 3 Question 10 Algebra 2
        unit3_q10_alg2 = input("|x+1| + |x+3| = 5. Seperate answers with comma: ")
        if str(unit3_q10_alg2) == "-9/2,1/2" or str(unit3_q10_alg2) == "-4.5,.5" or str(unit3_q10_alg2) == "-4.5, 0.5" or str(unit3_q10_alg2) == "-4.5, 0.5" or str(unit3_q10_alg2) == "-4.5, .5" or str(unit3_q10_alg2) == "-9/2, 1/2":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is -9/2,1/2")
    if int(y) == 4:
        # Unit 4 Algebra 2
        print("SOLVING QUADRATICS AND COMPLEX NUMBERS QUIZ:")
        # Unit 4 Question 1 Algebra 2
        unit4_q1_alg2 = input("What does i equal?: ")
        if str(unit4_q1_alg2) == "sqrt-1" or str(unit4_q1_alg2) == "sqrt(-1)":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong!, the correct answer is sqrt(-1)")
        # Unit 4 Question 2 Algebra 2
        unit4_q2_alg2 = input("Convert x^2-8x+18 into vertex form: ")
        if str(unit4_q2_alg2) == "(x-4)^2 + 2" or str(unit4_q2_alg2) == "(x-4)^2+2" or str(unit4_q2_alg2) == "(x-4)^2+ 2" or str(unit4_q2_alg2) == "(x-4)^2 +2":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong!, the correct answer is (x-4)^2 + 2")
        # Unit 4 Question 3 Algebra 2
        unit4_q3_alg2 = input("3x^2 - 5 = -446, solve for x.: ")
        if str(unit4_q3_alg2) == "+-7isqrt3" or str(unit4_q3_alg2) == "+-(7isqrt3)" or str(unit4_q3_alg2) == "(+-)(7isqrt3)" or str(unit4_q3_alg2) == "(+-7isqrt3)" or str(unit4_q3_alg2) == "+-(7i(sqrt(3))" or str(unit4_q3_alg2) == "+-7i(sqrt(3))":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong!, the correct answer is +-(7sqrt3)")
        # Unit 4 Question 4 Algebra 2
        unit4_q4_alg2 = input("(-11+3i)+(9+2i)? Hint: a+bi: ")
        if str(unit4_q4_alg2) == "-2+5i" or str(unit4_q4_alg2) == "-2 + 5i" or str(unit4_q4_alg2) == "-2 +5i" or str(unit4_q4_alg2) == "-2+ 5i":
            print("Your correct!")
            score += 1
        elif str(unit4_q4_alg2) == "5i-2":
            print("You have to use form a+bi! That is incorrect!")
        else:
            print("Your wrong!, the correct answer is -2+5i")
        # Unit 4 Question 5 Algebra 2
        unit4_q5_alg2 = input("(1+7i)(9+3i)-(4+2i) : ")
        if str(unit4_q5_alg2) == "-16+64i" or str(unit4_q5_alg2) == "-16 + 64i" or str(unit4_q5_alg2) == "-16+ 64i" or str(unit4_q5_alg2) == "-16 +64i":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong!, the correct answer is -16+64i")
        # Unit 4 Question 6 Algebra 2
        unit4_q6_alg2 = input("(1+8i)/(2-4i) Use parenthesis!: ")
        if str(unit4_q6_alg2) == "(-3+2i)/2" or str(unit4_q6_alg2) == "(-3 + 2i)/2" or str(unit4_q6_alg2) == "(-3+ 2i)/2" or str(unit4_q6_alg2) == "(-3 +2i)/2":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong!, the correct answer is (-3+2i)/2")
        # Unit 4 Question 7 Algebra 2
        unit4_q7_alg2 = input("x^2+16x-21=-5, solve for x(use completing the square): ")
        if str(unit4_q7_alg2) == "-8+-4sqrt5" or str(unit4_q7_alg2) == "-8+-4sqrt(5)" or str(unit4_q7_alg2) == "-8+-(4sqrt5)" or str(unit4_q7_alg2) == "-8+-(4sqrt(5))":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong!, the correct answer is -8+-4sqrt5")
        # Unit 4 Question 8 Algebra 2
        unit4_q8_alg2 = input("-x^2+10x=8, solve for x(use quadratic formula): ")
        if str(unit4_q8_alg2) == "5+-sqrt17" or str(unit4_q8_alg2) == "5+-sqrt(17)" or str(unit4_q8_alg2) == "5+-(sqrt17)" or str(unit4_q8_alg2) == "5+-(sqrt(17))":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong!, the correct answer is 5+-(sqrt(17))")
        # Unit 4 Question 9 Algebra 2
        unit4_q9_alg2 = input("Determine number and type of roots of -4x^4+84 = 10x: ")
        if str(unit4_q9_alg2) == "2 real rational roots" or str(unit4_q9_alg2) == "two real rational roots" or str(unit4_q9_alg2) == "2 real rational" or str(unit4_q9_alg2) == "2 real, rational roots":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong!, the correct answer is 2 real rational roots")
        # Unit 4 Question 10 Algebra 2
        unit4_q10_alg2 = input("Find three consecutive positive integers such that the product of the median integer and the largest integer is 72. Seperate with commas, and go from decreasing to increasing order: ")
        if str(unit4_q10_alg2) == "7,8,9" or str(unit4_q10_alg2) == "7, 8, 9" or str(unit4_q10_alg2) == "7, 8,9" or str(unit4_q10_alg2) == "7,8, 9":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong!, the correct answer is 7,8,9")
    if int(y) == 6:
        # Unit 6 Algebra 2
        print("ABSOLUTE VALUES QUIZ:")
        # Unit 6 Question 1 Algebra 2
        unit6_q1_alg2 = input("What is the cube root of 56r^8s^4? (write cube root as cube root) Follow example: What is the 4th root of 216m^3n^6? Answer:2mn^2 * 4th root of 3n^3: ")
        if str(unit6_q1_alg2) == "2r^2s * cube root 7r^2s" or str(unit6_q1_alg2) == "2sr^2 * cube root of 7sr^2" or str(unit6_q1_alg2) == "2sr^2 * cube root of 7r^2s" or str(unit6_q1_alg2) == "2r^2s * cube root of 7sr^2s":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is 2r^2s cube root of 7r^2s")
        # Unit 6 Question 2 Algebra 2
        unit6_q2_alg2 = input("What is the 4th root of 625c^23d^11? Use previous model to know how to structure your answer: ")
        if str(unit6_q2_alg2) == "5c^5d^2 * 4th root of c^3d^3" or str(unit6_q2_alg2) == "5d^2c^5 * 4th root of c^3d^3" or str(unit6_q2_alg2) == "5c^5d^2 * 4th root of d^3c^3" or str(unit6_q2_alg2) == "5d^2c^5 * 4th root of d^3c^3":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is 5d^2c^5 * 4th root of c^3d^3")
        # Unit 6 Question 3 Algebra 2
        unit6_q3_alg2 = input("(3+sqrt7)/(2+2sqrt7) Write square root as sqrt!: ")
        if str(unit6_q3_alg2) == "(2+sqrt7)/6" or str(unit6_q3_alg2) == "(2+sqrt(7))/6" or str(unit6_q3_alg2) == "(2+(sqrt(7))/6" or str(unit6_q3_alg2) == "(2+(sqrt7))/6":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is (2+sqrt7)/6")
        # Unit 6 Question 4 Algebra 2
        unit6_q4_alg2 = input("Rewrite in simplest radical form: (m^5/2)/(m^7/4)? Write like this: Example: The ___ root of _____: ")
        if str(unit6_q4_alg2) == "The fourth root of m^3":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is The fourth root of m^3")
        # Unit 6 Question 5 Algebra 2
        unit6_q5_alg2 = input("sqrt(6w-5) + 10 = 3, what is w?: ")
        if str(unit6_q5_alg2) == "No Solution" or str(unit6_q5_alg2) == "no solution" or str(unit6_q5_alg2) == "No solution" or str(unit6_q5_alg2) == "no Solution":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is No Solution!")
        # Unit 6 Question 6 Algebra 2
        unit6_q6_alg2 = input("-36=-9(c-12)^1/2, find c: ")
        if str(unit6_q6_alg2) == "c=28" or str(unit6_q6_alg2) == "28":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is 28!")
        # Unit 6 Question 7 Algebra 2
        unit6_q7_alg2 = input("sqrt(12-a)+7a=8a, what is a?: ")
        if str(unit6_q7_alg2) == "a=3" or str(unit6_q7_alg2) == "3":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is 3!")
        # Unit 6 Question 8 Algebra 2
        unit6_q8_alg2 = input("What is the domain of 3sqrt(x+1) in interval notation?: ")
        if str(unit6_q8_alg2) == "[-1,∞)" or str(unit6_q8_alg2) == "[-1, ∞)":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is [-1,∞)!")
        # Unit 6 Question 9 Algebra 2
        unit6_q9_alg2 = input("Find the inverse of (x-8)/3 (copy paste: f⁻¹(x)): ")
        if str(unit6_q9_alg2) == "f⁻¹(x) = 3x+8" or str(unit6_q9_alg2) == "f⁻¹(x)=3x + 8" or str(unit6_q9_alg2) == "f⁻¹(x)=3x +8" or str(unit6_q9_alg2) == "f⁻¹(x)=3x+ 8":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is f⁻¹(x)=3x+8")
        # Unit 6 Question 10 Algebra 2
        unit6_q10_alg2 = input("Is f(x) and g(x) inverses? f(x) = x^2+8 (x>=0) and g(x) = sqrt(x-8) (yes or no): ")
        if str(unit6_q10_alg2) == "Yes" or str(unit6_q10_alg2) == "yes":
            print("Your correct!")
            score += 1
        else:
            print("Your wrong! The correct answer is Yes!")


elif str(ask) == "Geometry": 
    print("yk ms pam is the best")
else:
    print("Please write an acceptable math course")
while ask == "":
    print("Please write a math course.")
    ask = input("What level of math would you like?(Algebra, Algebra 2, Geometry): ")

if score >= 7:
    print(f"Congrations, your total score is {score} out of 10! You passed!")
else:
    print(f"Sorry you failed with a {score} out of 10. Would you like to retry?")

print("Any incorrect answers? Any comments on the quizzes? Please don't hesitate to reach out to ddrdoom245@gmail.com. We truly appreciate it. Explanation to every answer is here.")
