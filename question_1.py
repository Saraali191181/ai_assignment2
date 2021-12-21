# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 23:50:01 2021

@author: hp
"""
from logic2 import *



# in Englis : carrot's color is orange 
carrots = symbol("carrots")
orange = sybmol("orange")
knowledge_q1=AND(Implication (carrots,orange))
# to print output formula
print (knowledge_q1.formula())
#---------------------------------------------------------------------


# in English: person likes carrots if person is vegetarian 
person = symbol ("person")
vegetarian = symbol("vegetarian(x)")
like_person_carrots = symbol("like (x,carrots)")
knowledge_q2=AND(Implication (vegetarian,person))

# to print output formula

print (knowledge_q2.formula())

#---------------------------------------------------------------------

# in English : student pass if student study hard

pass_exam = symbol ("pass(x)")
study_hard = symbol("sh(x)")
student = symbol("student")
knowledge_q3=AND(Implication (AND(student,sh),pass_exam))

# to print output formula

print (knowledge_q3.formula())

#---------------------------------------------------------------------

# in English : who will pass??

print (knowledge_q3.formula())

#---------------------------------------------------------------------

# in English : which course professor teaches ??

course = symbol("course(x)")
professor = symbol("prof")
teaches_a_course = symbol ("teaches(x)")

knowledge_q5=AND(Implication (AND(prof,teaches),course))

# to print output formula

print (knowledge_q5.formula())


#---------------------------------------------------------------------

# in English :if x&&y are enemies then x hates y and fights y

enemies = symbol ("enemies (x,y)")
hates= symbol ("hates(x,y)")
fights = symbol("fights(x,y)")

knowledge_q6=AND(Implication (AND(hates,fights),enemies))

# to print output formula

print (knowledge_q6.formula())
