programing_dictionary={"Amotivation":"a reduction in the motivation to initiate or persist in goal-directed behaviour","Angeliferous":"resembling an angel","Angered":"fill someone with anger","Angsting":"to feel or express anxiety, apprehension, or insecurity","Blert":"a fool"}
x=input("enter the word you want the meaning")
print(programing_dictionary[x])
programing_dictionary["Amotivation"]="Demotivated"
print(programing_dictionary["Amotivation"])
programing_dictionary={}
print(programing_dictionary)
for value in programing_dictionary:
    print(value)
x={1:"harshit",2:"vaibhav",3:"ankit"}
x[4]="Gopal"
for things  in x:
    print(things)
    print(x[things])
    student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades={}
for value in student_scores:
    z=student_scores[value]
    if z>90 and z<=100:
        student_grades[value]="outstanding"
    elif(81<z<=90):
        student_grades[value]="exceed Expectations"
    elif(71<z<=80):
        student_grades[value]="Acceptable"
    else:
        student_grades[value]="Fail"
