#9's odd index is 4
import time

oddnumber = int(input("Enter odd number: "))
print("Your odd number is: ")
print(oddnumber)

oddindex = int(input("Enter odd index: "))
print("Your odd index is: )")
print(oddindex)

print("All values assigned, starting triad calculation..")
time.sleep(1)
print("Assigning numbers..")
time.sleep(1)
print("Calculating second number...")
SecondNumber = (oddnumber) * (oddindex) + (oddindex)
time.sleep(3)
print("Caluclating third number...")
ThirdNumber = (SecondNumber) + 1
time.sleep(2)
print("Triad calculated!")
print("Your completed triad is: ")
print(oddnumber)
print(SecondNumber)
print(ThirdNumber)
