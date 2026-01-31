#Students Attendance
print("Attendance List")
total_effect=int(input("Enter total effective of classroom: "))
#course hour
hour=int(input("When does your lesson start?(Enter in minute)"))

#classroom list
class_room=[]

#Attendants list
list_attendants=set()

#Make a loop so that all studants save their number 
t=0
while t<hour :
    i=int(input("Enter your number: "))
    if i > total_effect or i < 0:
        print("Doesn't exist!")
    else:
        list_attendants.add(i)
    t += 2

#Check attendance
for i in range(total_effect):
    if i in list_attendants:
        True
    else:
        continue
        

    
   
print("Attendants list: {} ".format(list_attendants))
