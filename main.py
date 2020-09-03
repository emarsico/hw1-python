def translateGrade(g):
  if g == "A" :
    return 4.0
  elif g == "A-" :
    return 3.67
  elif g == "B+" :
    return 3.33
  elif g == "B" :
    return 3.0
  elif g == "B-" :
    return 2.67
  elif g == "C+" :
    return 2.33
  elif g == "C" :
    return 2.0
  elif g == "D" :
    return 1.0
  else :
    return 0
  

gradepoint1 = input("Enter your course 1 letter grade: ")
credit1 = float(input("Enter your course 1 credit: "))
print("Grade point for course 1 is : " + str(translateGrade(gradepoint1)))

gradepoint2 = input("Enter your course 2 letter grade: ")
credit2 = float(input("Enter your course 2 credit: "))
print("Grade point for course 2 is : " + str(translateGrade(gradepoint2)))

gradepoint3 = input("Enter your course 3 letter grade: ")
credit3 = float(input("Enter your course 3 credit: "))
print("Grade point for course 3 is : " + str(translateGrade(gradepoint3)))

GPA = (translateGrade(gradepoint1) * credit1 + translateGrade(gradepoint2) * credit2 + translateGrade(gradepoint3) * credit3) / (credit1 + credit2 + credit3) 
print("Your GPA is: " + str(GPA))