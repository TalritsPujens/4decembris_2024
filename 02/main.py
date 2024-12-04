""" Method 1 """

num = int(input("Give me a number to check: ")) # piešķir mainīgajam ievadīto vērtību ar šo pārbaudīs
check = int(input("Give me a number to divide by: "))  #pešķir mainīgajam iievadīto vērtīvu ar šo vērtību dalīs

if num % 4 == 0:  # pārbauda vai skaitlis dalās ar četri
    print(num, "is a multiple of 4") #izprintē šo ja skaitlis dalās ar 4
elif num % 2 == 0: #pārbauda vai skaitlis ir pāra skaitlis
    print(num, "is an even number") #ja ir tad izprintē ka ir pāra skaitlis
else:
    print(num, "is an odd number") # ja nav tad izprintē ka ir nepāra

if num % check == 0: #pārbauda vai divi ievadītie skaitļi dalās viens ar otru
    print(num, "divides evenly by", check)  #ja dalās izprintē ka dalās
else:
    print(num, "doesn't divide evenly by", check) #ja nedalās izprintē ka nedalās

""" Method 2 """
num = int(input("Enter a number: ")) #pešķir mainīgajam ievadīto vērtību
mod = num % 2 # aprēķina aatlikumu dalot šo skaitli ar 2
if mod > 0:# pārbauda vai atlikums ir lielāks par nulli
    print("You picked an odd number.") # ja ir tad izprintē ka skaitlis ir nepāra
else:
    print("You picked an even number.") # ja nav izprintē ka skaitlis ir pāra
