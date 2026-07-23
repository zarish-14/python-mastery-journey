print("========================================")
print("STUDENT MARKS ANALYZER")
print("========================================")
#marks of student in list
marks=[50,70,65,82,65] 
#display marks
idx=0
print("Marks\n")
for i in marks: 
    print("marks of student at ",idx, " = ",i)
    idx=idx+1
print("--------------------------------")
#total_marks
total_marks=0
i=0
while i < len(marks):
    total_marks=total_marks+marks[i]
    i=i+1
print("Total marks = ",total_marks)
#Calculate Averge marks
average=total_marks/len(marks)
print("Average = ",average)
#Calculate highest marks
highest=marks[0]
idx=0
high_idx=0
for i in marks:
    if (highest < marks[idx]):
        highest=marks[idx]
        high_idx=idx
    idx=idx+1
print("Highest marks = ",highest , " ,at index = ",high_idx)
#Calculate lowest marks
low=marks[0]
idx=0
low_idx=0
for i in marks:
    if (low > marks[idx]):
        low=marks[idx]
        low_idx=idx
    idx=idx+1
print("lowest marks = ",low , " ,at index = ",low_idx)
print("--------------------------------")
#Search student marks 
x=int(input("enter number to search= "))
idx=0
found=False
for el in marks:
    if( el == x):
        print("Found ",x," at = ",idx)
        found=True
        break
    idx=idx+1
if(not found):
    print("Number not found")
print("--------------------------------")

#Count pass Students:
pass_count=0
passing_marks=int(input("Enter passing marks= "))
if (passing_marks <0 or passing_marks >100):
     print("Invalid marks,Cannot Calculate Passed students")
else:
    for el in marks:
        if ( el >= passing_marks):
             pass_count=pass_count+1
    print("Passed Students = ",pass_count)
#Count fail Students:
fail_count=0
if (passing_marks <0 or passing_marks >100):
     print("Invalid marks,Cannot Calculate Failed students")
else:
    for el in marks:
        if ( el < passing_marks):
            fail_count=fail_count+1
    print("Failed Students = ",fail_count)
print("--------------------------------")
#Print Grades:
for i in marks:
    if ( i >= 90):
        print(i , " -> ","A+")
    elif (i>= 80):
        print(i , " -> ","A")
    elif (i>= 70):
            print(i , " -> ","B")
    elif (i>= 60):
            print(i , " -> ","C")
    elif (i>= 50 ):
            print(i , " -> ","D")
    elif (i < 50):
         print(i , " -> ","FAIL")
print("THANK YOU !")


