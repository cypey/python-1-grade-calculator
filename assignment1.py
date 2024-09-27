name = input("What's your name? ")
print("Hello", name,"! Lets calculate your grade")

# labs :
labs = int(input("Enter the number of labs completed: "))
# labs_weight = 0.2
if labs >6:
    labs = 6
lab_grade = (((labs/6)*0.20)*100)

# quizzes :
quizzes = int(input("Enter the number of quizzes/in-class actvities completed: "))
# quizzes_weight = 0.15
if quizzes >6:
    quizzes = 6
quiz_grade = (((quizzes/6)*0.15)*100)

# assignments :
a1 = float(input("Enter your grade for Assignment 1: "))
a2 = float(input("Enter your grade for Assignment 2: "))
a3 = float(input("Enter your grade for Assignment 3: "))
a4 = float(input("Enter your grade for Assignment 4: "))
# a_weight = 0.04
a_grade = ((a1*0.04) + (a2*0.04) + (a3*0.04) + (a4*0.04))

# Midterms :
mt1 = float(input("Enter your grade for Midterm 1: "))
mt2 = float(input("Enter your grade for Midterm 2: "))
# mt_weight = 0.125
mt_grade = ((mt1*0.125) + (mt2*0.125))

# Final :
final = float(input("Enter your grade for the Final exam: "))
# final_weight = 0.18
final_grade = (final*0.18)

# Prep :
prep = float(input("Enter your grade for the Midterms and Final preperation: "))
# prep_weight = 0.06
prep_grade = (prep*0.06)


grade = (lab_grade + quiz_grade + a_grade + mt_grade + final_grade + prep_grade)
print("Your grade is:",float(round(grade,2)) ,",",name,"!")