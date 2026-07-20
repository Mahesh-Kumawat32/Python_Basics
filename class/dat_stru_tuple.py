#CREATION OF TUPLE:-----------
# t1 = (1,2,3,"Mahesh",3+8j)
# t2 = (1,2,3,4)
# t3 = (1,2,54,6,6)
# t4= t2+t3

#PRINT ELEMENTS(COMPLETE TUPLE) OF TUPLE USING PRINT FUCNTION
# print(t4)
# print(t1)

#ACCESS PART OF TUPLE USING SLICING IN TUPLE:------->>tuple[start:stop:steps]
# t = tuple("Python")
# # print(t[1:])
# print(t[::-1])
# print(t[-6:])

#USE del KEYWORD TO DELETE A ELEMENT FROM A TUPLE OR DELETE A TUPLE COMPLETELY:---------
# del t    


#METHODS OF TUPLE:----------
# print(len(t))       #len()--->used to find length of a tuple.


#UPDATE TUPLE USING TYPE CONVERSION:-------TUPLE-->LIST(make changes in it)--->TUPLE
# t = tuple("Python")
# t = list(t)
# t.append("Mahesh")
# t[0] = "Kumawat"
# t.remove("o")
# print(type(t))
# print(t)
# t = tuple(t)
# print(type(t))
# print(t)


#PRACTICE QUESTIONS::::::::::::::::

#CREATE TUPLE CONTAINING STUDENTS NAME
# t1 = ("Mahesh",'Bharati',"Satyam","Harsh","Meet","Kevin")

#ACCESS TUPLE ELEMENTS FIRST AND LAST
# print(t1[0])
# print(t1[len(t1)-1])

#FIND THE LENGTH OF TUPLE
# print(len(t1))

#CREATE A TUPLE STORE A NAME AND PERFORM SLICING FIRST AND LAST ELEMENT USING = (+,-)
# t2 = ("Mahesh",'Bharati',"Satyam","Harsh","Meet","Kevin")
# # print(t2[0::5])
# print(t2[-(len(t2))::len(t2)-1])

#CREATE A TUPLE ADD STUDENTS NAME AND ADD MORE NAME USING LIST CONVERSION---|
#CREATE TUPLE AND REMOVE TWO ITEMS USING LIST CONVERSION--------------------|--------->>ALL IN ONE CODE
#UPDATE STUDENTS NAME USING REMOVE AND APPEND OR INDEXING-------------------|
# t3 = ("Mahesh",'Bharati',"Satyam","Harsh","Meet","Kevin")
# print(type(t3))
# t3 = list(t3)-------tuple--->list
# t3.append("Prince") #it adds value doesn't effect other one
# t3[4]= "Sukhdev"    #it adds a specific index and remove the value which is already exists at that position
# print(t3)
# t3.remove("Sukhdev")
# print(t3)
# print(type(t3))
# t3 = tuple(t3)------again list ---->tuple
# print(type(t3))
# print(t3)


#FIND TUPLE USING LOOPS
# t4 = (1,2,3,4,"Mahesh",3+8j)
# for i in range(0,len(t4)):
#     print(t4[i], end = " ")