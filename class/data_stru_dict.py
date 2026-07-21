# student = {
#     "name":"Mahesh",
#     "age": 19,
#     "degree": "Computer Science"
# }
# print(student)                    #TO SHOW DICTIONARY USE PRINT FUNCTION
# print(student["name"])            #TO ACCESS A SPECIFIC ELEMENT USE KEY
# print(student.get("age"))         #get(key) IT IS ALSO USED TO ACCESS SPECIFIC ELEMENT 

# num = dict(name= "sum", age=20)   #ANOTHER WAY TO CREATE DICTIONARY USING dict() method
# print(num)
# print(type(num))

# student["city"] = "Pali"          #TO ADD ELEMENTS IN DICTIONARY
# student["name"] = "Suresh"        #TWO UPDATE A KEY VALUE ALSO WE USE KEY
# del student["name"]               #USING del KEY WORD WE CAN DELETE A SPECIFIC ELEMENT OF DICTIONARY
# del student                       #USING del WE CAN ALSO DELETE A DICTIONARY
# print(student)

# val = student.pop("name")           #pop(key) REMOVES THE ELEMENT OF GIVEN KEY BUT RETURN THE REMOVED VALUE
# print(val)

# student.clear()             #ITS CLEAR THE DICTIONARY NOT DELETE IT MEANS REMOVE ALL ELEMENTS
# print(student)

# for i in student.keys():      #ACCESS ELEMENTS USING FOR LOOPS USING keys() method
#     print(i)
# for i in student.values():    #ACCESS ELEMENTS USING FOR LOOPS USING values() method
#     print(i)
# for a,b in student.items():     #ACCESS ELEMENTS USING FOR LOOPS USING items() method
#     print(f"{a} : {b}")


# data = {        #NESTED DICTIONARY
#     "student1" : {"name":"Mahesh", "age":19},
#     "student2" : {"name":"Bharati", "age":19},
#     "student3" : {"name":"Satyam", "age":20}
# }
# print(data["student1"]["name"])     #WAY TO ACCESS ELEMENT OF A NESTED DICTIONARY
# for a,b in data["student1"].items():    #WAY TO ACCESS ELEMENTS OF A DICTIONARY USING item() method
#     print(f"{a} : {b}")


#PRACTICE QUESTIONS==============================================================>>
#CREATE A DICTIONARY AND ADD ATLEAST FIVE STUDENT NAME KEYS AS : NAME, AGE, COURSE
# std1={"name":"Mahesh","age":19, "course":"computer science"}
# std2={"name":"Bharati","age":19, "course":"computer science"}
# std3={"name":"Satyam","age":20, "course":"computer science"}
# std4={"name":"Atendra","age":20, "course":"computer science"}
# std5={"name":"Arvind","age":40, "course":"Bsc IT"}

#CREATE A EMPLOYEE DICTIONARY AND ACCESS VALUES USING keys() AND get() METHODS AND ADD A NEW EMPLOYEE USING BUILT IN FUCNTION
# emp = {"name1":"Amit sharma", "name2":"Jon hajenberg", "name3":"John Brandon"}
# print(emp["name1"])
# print(emp.get("name3"))
# for i in emp.keys():
#     print(i)
# for i in emp.values():
#     print(i)
# for a,b in emp.items():
#     print(f"{a} : {b}")

#CREATE A NESTED DICTIONARY AND ACCESS THEIR ELEMENTS USING FOR LOOP
# student_data = {
#     "student1" :{"name":"Mahesh","age":19, "course":"computer science"},
#     "student2" :{"name":"Bharati","age":19, "course":"computer science"},
#     "student3" :{"name":"Satyam","age":20, "course":"computer science"},
#     "student4" :{"name":"Atendra","age":20, "course":"computer science"},
#     "student5" :{"name":"Arvind","age":40, "course":"Bsc IT"}
# }
# for a,b in student_data.items():      #IT PRINTS COMPLETE OUTER DICTIONARY 
#     print(f"{a} : {b}")
# for a,b in student_data["student1"].items():  #IT PRINTS ONLY DATA OF A NESTED DICTIONARY
#     print(f"{a} : {b}")
