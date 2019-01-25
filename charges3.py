"""
This code count all charges
"""
type_of_charges={"transport":0,"auto":0,"food":0,"medicament":0,"bill":0,"shoping":0,"beautiful":0\
    ,"rest":0,"hobby":0,"children":0,"holiday":0,"other charges":0}

# user_input = ''
# while user_input is not float:
#     try:
#         user_input = float(input('Enter a number: '))
#     except ValueError:
#         print('Please enter a valid number: ')


def charges():

    for key in type_of_charges.keys():
        type_of_charges[key] = float(input("Enter a number for {x}:".format(x=key)))

    # This is the same as
     # user_input['transport'] = float(input("Enter a number:"))
     # user_input['auto']=float(input("Enter a number:"))
     # user_input['food']=float(input("Enter a number:"))
     # user_input['medicament']=float(input("Enter a number:"))
     # user_input['bill']=float(input("Enter a number:"))
     # user_input['shoping']=float(input("Enter a number:"))
     # user_input['beautiful']=float(input("Enter a number:"))
     # user_input['rest']=float(input("Enter a number:"))
     # user_input['hobby']=float(input("Enter a number:"))
     # user_input['children']=float(input("Enter a number:"))
     # user_input['holiday']=float(input("Enter a number:"))
     # user_input['other_charges']=float(input("Enter another number:"))

charges()

result = sum(type_of_charges.values())
print("My charges today is " + str(result))

#print('You entered {}'.format(a))
