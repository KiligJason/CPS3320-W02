#CPS3320-W02-Tutorial2
#Ziyiyang Wang 1098529
#Zhaoze Wang 1098471

#Enter a positive number
print("Please enter a positive number: ")
target_number = int(input())
#Test the number
if target_number < 0:
    print("You should retype the positive number")
    target_number = int(input())

if (target_number%2 == 0 and 
    target_number%3 == 0 and
    target_number%4 == 0):
    print("The number "+str(target_number)+" is multiply of 2,3,4")
else:
    print("The number "+str(target_number)+" is not a multiply of 2,3,4")

print("End of program")