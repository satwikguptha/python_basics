def analyze_result(name,roll,marks=[]):
    total=sum(marks)
    average=total/len(marks)

    if average>=90:
        grade="A"
    elif average >=75:
        grade="B"
    elif average >=60:
        grade="C"
    elif average >=40:
        grade="D"  
    else:
        grade = "Fail"

    print(f"student : {name} (roll : {roll})")
    print(f"total : {total} , Average : {average}")
    print(f"grade : {grade}")

    below_40 = []
    for i in range(len(marks)):
        if marks[i] < 40:
            below_40.append(f"subject {i+1} ")  


    if below_40:
        print("subjects below 40 :",",".join(below_40))
    else:
        print("subjects below 40: NONE")            


analyze_result("satwik",52,[80,75,44,10,100,100])

   