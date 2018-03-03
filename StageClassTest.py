#Stage Test Suite

#The files are getting filled with test code and debug code.
# As the code is reactivated everytime we want to test something.
#I am worried its getting out of hand.
#Thus, If you do indeed have test code you want to make, make it in a seperate file, such as this
#and import the file to be tested. It will be much cleaner this way.
import StageClass
#Tests for sliding
stage = StageClass.Stage(6)
print()
stage.letFill()
print()
stage.gridDisplay()
print()
stage.slide(1,1,'r', 3)
print("Sliding 1,1 3 to the right")
print()
stage.gridDisplay()
print()
stage.slide(1, 1, 'l', 4)
print("Sliding 1,1, 4 to the left")
print()
stage.gridDisplay()
print()
stage.slide(1, 1, 'd', 4)
print("Sliding 1,1 4 spots down")
print()
stage.gridDisplay()
print()
stage.slide(1, 1, 'u', 4)
print("Sliding 1,1, 4 spots up")
print()
stage.gridDisplay()
print()
print("Sliding 3,4 5 spots to the right")
print()
stage.slide(3, 4, 'r', 5)
stage.gridDisplay()
       

