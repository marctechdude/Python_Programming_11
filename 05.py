### Old modulo string replace
print("Clayton has %d excellent %s players this season." % (4, 'basketball'))
###

### Old modulo all 4 floats lined up
print("%7.2f" % 45.23)
print("%7.2f" % 3.03)
print("%7.2f" % 139.80)
print("%2.2f" % 2948.09)
###
### Old modulo 11 blank spaces in front of +54
print("%+14d" % 54)
###
### Old modulo Output exponent with 6 spaces in front
print("%16.4e" % 652.16)
###
###Using new method
print("The current temperature outside the {0:s} airport is {1:6.1f} celsius" .format('Vancouver', 5.6))

print("The population of {a:s}, Columbia is {b:1.3f} million." .format(a='Bogota', b=6.763))
###
### New method + variables
mycity = 'Phoenix'

myfloat = 4.574

print("The population of {0:s} Arizona is {1:1.3f} million" .format(mycity, myfloat))
###
### Using spacing and text-align
print("{0:s} {1:>13s} {2:>13s} {3:8.2f}" .format('Laptop:', 'MacbookPro', 'Cost:', 1579.00))
print("{0:s} {1:>13s} {2:>13s} {3:8.2f}" .format('Laptop:', 'Surface Pro 4', 'Cost:', 1439.00))
###