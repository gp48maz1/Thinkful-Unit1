#tip_calc.py

import sys

meal = float(sys.argv[1])
tax = float(sys.argv[2])
tip = float(sys.argv[3])

tax_value = meal * tax
meal_with_tax = tax_value + meal
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value


print "The base cost of your meal was ${0:.2f}".format(meal)
print "You need to pay ${0:.2f} for tax.".format(tax_value)
print "Tipping as a rate of {0}%, you should leave ${1:.2f} for a tip".format( int(100*tip), tip_value)

print "The grand total of your meal is ${0:.2f}.".format(total)