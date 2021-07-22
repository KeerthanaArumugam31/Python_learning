course={101:["python","3month",20000],102:["java","2month",10000],103:["sql","4month",40000]}
while True:
    id=int(input("Enter the id:"))
    if id in course:
        print("course name:",course[id][0])
        print("course duration:",course[id][1])
        print("course fee:",course[id][2])
    else:
        print("Invalid id")
        break
