"""
This code count all charges
"""
type_of_charges={"transport":0,"auto":0,"food":0,"medicament":0,"bill":0,"shoping":0,"beautiful":0\
    ,"rest":0,"hobby":0,"children":0,"holiday":0,"other charges":0}

user_input = ''
while user_input is not float:
    try:
        user_input = float(input('Enter a number: '))
    except ValueError:
        print('Please enter a valid number: ')
def charges():
     transport=float(input("Enter a number:"))
     return type_of_charges["transport"]
     auto=float(input("Enter a number:"))
     food=float(input("Enter a number:"))
     medicament=float(input("Enter a number:"))
     bill=float(input("Enter a number:"))
     shoping=float(input("Enter a number:"))
     beautiful=float(input("Enter a number:"))
     rest=float(input("Enter a number:"))
     hobby=float(input("Enter a number:"))
     children=float(input("Enter a number:"))
     holiday=float(input("Enter a number:"))
     other_charges=float(input("Enter another number:"))

result = sum(type_of_charges.values())
print("My charges today is"+result)

print('You entered {}'.format(a))
