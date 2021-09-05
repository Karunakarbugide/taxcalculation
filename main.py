from tax_calculate import *

tct = Tax_Computation()

input_name = input("Please enter Name     :")
input_ssn = input("Enter SSN    : ")
input_income = input("Please enter income 2020  : ")


if input_ssn.isdigit():
    if len(input_ssn) == 9:
        SSN_num = input_ssn
    else:
        print('SSN number consist exact 9 digits')
else:
    print("Please Enter valid SSN Number")



tax_amount , rate = tct.tax_compute(input_income)

rate = float(rate)*100

print('_________________________________________________________')
print('|Name ................................{}|'.format( input_name))
print('|SSN .................................{}|'.format(input_ssn))
print('|2020 Income .........................{}|'.format(input_income))
print('_________________________________________________________')
print('Federal Income Tax Due: ${:,.2f} ( {} % of income)'.format(tax_amount, rate))
print('_________________________________________________________')

