name = input("Whats your name? ")
print("Hello", name,"! Lets calculate figure out your grade")

# labs :
labs = int(input("Enter the number of labs completed: "))
labs_weight = 0.2
if labs > 6:
    labs = 6
lab_grade = (labs*labs_weight)

# quizzes :
quizzes = int(input("Enter the number of quizzes/in-class actvities completed: "))
quizzes_weight = 0.15
if quizzes >6:
    quizzes = 6
quiz_grade = (quizzes*quizzes_weight)

# assignments :
a1 = float(input("Enter your grade for Assignment 1: "))
a2 = float(input("Enter your grade for Assignment 2: "))
a3 = float(input("Enter your grade for Assignment 3: "))
a4 = float(input("Enter your grade for Assignment 4: "))
a_weight = 0.04
a_grade = ((a1*a_weight) + (a2*a_weight) + (a3*a_weight) + (a4*a_weight))

# Midterms :
mt1 = float(input("Enter your grade for Midterm 1: "))
mt2 = float(input("Enter your grade for Midterm 2: "))
mt_weight = 0.125
mt_grade = ((mt1*mt_weight) + (mt2*mt_weight))

# Final :
final = float(input("Enter your grade for the Final exam: "))
final_weight = 0.18
final_grade = (final*final_weight)

# Prep :
prep = float(input("Enter your grade for the Midterms and Final preperation: "))
prep_weight = 0.06
prep_grade = (prep*prep_weight)


grade = (lab_grade + quiz_grade + a_grade + mt_grade + final_grade + prep_grade)
print("Your grade is:",float(round(grade,2)) ,",",name,"!")
      
