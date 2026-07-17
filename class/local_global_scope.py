#LOCAL VARIABLE INSIDE A FUNCTION
# def std():
#     name = "Mahesh"
#     print("name")
# std()
# print(name)---------this throw error because out side of 
                      #the function we don't have any varibale named 
                      #with name
                      

#GLOBAL VARIABLE
city = "Jodhpur"
def show():
    global position #first decalre varibale as a global 
    position = "Rajasthan"  #then asign value to it
    print(city)  
show()
print(position)