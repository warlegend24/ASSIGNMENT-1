#QUESTION 1:
print("ENTER NUMBERS HERE")
a=int(input())
b=int(input())
c=int(input())
print("AVERAGE=",(a+b+c)/3)

#QUESTION 2:
print("ENTER GROSS INCOME")
income=int(input())
standard_deduction=10000
dep_deduction=3000
tax_rate=20
print("ENTER NO. OF DEPENDANTS")
dependants=int(input())
taxable_income = (income)-(standard_deduction)-(dependants*dep_deduction)
print("INCOME TAX=",(taxable_income*tax_rate))

#QUESTION 3:
sid=int(input("ENTER SID="))
name=input("ENTER NAME=")
gender=input("ENTER GENDER(M/F/U)=")
branch=input("ENTER BRANCH=")
cgpa=float(input("ENTER CGPA="))
student=[sid,name,gender,branch,cgpa]
print("student details=",student)

#QUESTION 4:
s1=int(input("STUDENT 1 MARKS="))
s2=int(input("STUDENT 2 MARKS="))
s3=int(input("STUDENT 3 MARKS="))
s4=int(input("STUDENT 4 MARKS="))
s5=int(input("STUDENT 5 MARKS="))
marks=[s1,s2,s3,s4,s5]
marks.sort()
print("sorted list=",marks)

#QUESTION 5(a)
LIST=["RED","GREEN","WHITE","BLACK","PINK","YELLOW"]
LIST.pop(3)
print("REQURED OUTPUT",LIST)

#QUESTION 5(b)
LIST=["RED","GREEN","WHITE","BLACK","PINK","YELLOW"]
LIST.pop(4)
LIST[3]="PURPLE"
print("REQUIRED LIST=",LIST)





