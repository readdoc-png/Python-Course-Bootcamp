#Exercise 1 : Mailing Address

print("Muhamad Yusuf Hidayat")
print("Departement of Computer Science")
print("National Institute Technology Bandung")
print("2500 National Institute Technology Bandung")
print("4XXXX, Bandung")
print("Indonesia")

#Exercise 2 : Hello

name = input("What is your name ?")
print (f"Hello {name}", "Good Morning")

#Exercise 3 : Area of Room

#Give user input
lenth = input ("Lenth of Room")
width = input("Width of Room")

#Type convertion from str to floating point numbers
l_convert = float (lenth)
w_convert = float(width)

#Calculate area l * w
area = w_convert * l_convert

#Display output
print (f"{area}", "meters")

#Exercise 4 : Area of a Field

#Value that convert from square feet to acre
SQFT_PER_ACRE = 43560

#Length user input
length = input("Lenth of Area ?")

#Width user input
width = input("Width of Area ?")

#Type conversion from string to float number
length_cov = float(length)
width_cov = float(width)

#Calculate total area in acre
total_area = length_cov * width_cov / SQFT_PER_ACRE

#Print the calculation result
output = print(f"There are {total_area} square feet in an acres")

#Exercise 5 : Bottle Deposits

#Compute the refund amount for a collection of bottles
LESS_DEPOSITE = 0.10
MORE_DEPOSITE = 0.25

# Read the number of containers of each size from the user
less = input("How many containers 1 litre or less?" " ")
more = input("How many containers more that 1 litre?" " ")

# Type conversion
less_int = int(less)
more_int = int(more)

# Calculate refund amount
refund = LESS_DEPOSITE * less_int + MORE_DEPOSITE * more_int

# Display output
print("Your total refund will be $%.2f." % refund)

#Exercise 6 : Tax & Tip

#User cost input
meal_cost = input("Cost of a meal?" " " "Rp.")

#Type convert
meal_cost_conv = float(meal_cost)
# In this case, I use restaurant tax
#Tax & Tip Rate
Tax = 0.10
Tip = 0.18

#Tax calculation
tax = meal_cost_conv * Tax
#Tip calculation
tip = meal_cost_conv * Tip

#Total bill calculation (Tip, Tax and Food cost)
total_bill = tip + tax + meal_cost_conv
output = "The tax is Rp.%.2f and the tip is Rp.%.2f, making the total Rp.%.2f" % (
    tax,
    tip,
    total_bill,
)

#Display output
print(output)

#Exercise 7 : Sum of the first n Positive Integers

#User input
number = input("Give a number :")

#Type convertion from string to integer
int_number = int(number)

#Calculate with formula x = (n)( n + 1) / 2
sum = (int_number) * (int_number + 1) / 2
print("The sum of the first", int_number, "positive integer is", sum)

#Exercise 8 : Widget and Gizmos 

#Widget weight and gizmos weight in grams
Widget_weighs = 75
Gizmos_weighs = 112

#User give 2 input, the split it
a, b = input("Enter Widget & Gizmos weight value: ").split()

#Display output value a and b. a = widget weight, b = gizmoz weight
print("Your Widget Weight Value : ", a)
print("Your Gizmoz Weight Value: ", b)

#Type convertion from str to int
a = int(a)
b = int(b)

#Calculate total weight (output in grams
total_weighs = (75 * a) + (112 * b)

#String formatting for display output
output = (
    "The Widget weighs is .%.0f grams and the Gizmos weight is %.0f grams, making the total weight is %.0f grams"
    % (a, b, total_weighs)
)

#Display output
print(output)
#

# Exercise 10 : Arithmetic
# Import math library to call log10 function
# from math import log10

# # Give user input from keyboard
x = input("Type first number  : ")
y = input("Type second number : ")

# # Type conversion (str to int)
x = int(x)
y = int(y)

# # Calculate the x and y value and display output
print(x, "+", y, "is", x + y)
print(x, "-", y, "is", x - y)
print(x, "*", y, "is", x * y)
print(x, "/", y, "is", x / y)
print("The base 10 logarithm of", x, "is", log10(x))
print(x, "x^y", y, "is", x**y)

# Exercise 11 : Fuel Efficiency
print("Fuel Efficiency")
x = input("Type a number : ")
x = float(x)
calculate = 235 / x
print(calculate, "L/100KM")

# Exercise 12 : Distance Between Two Points on Earth


import math

print("Distance Between Two Points on Earth")

# # Latitude
t1 = float(input("Give input for t1 : "))
t1 = math.radians(t1)

g1 = float(input("Give input for g1 : "))
g1 = math.radians(g1)

# # Longitude
t2 = float(input("Give input for t2 : "))
t2 = math.radians(t2)

g2 = float(input("Give input for g2 : "))
g2 = math.radians(g2)

# #Dilatation
dlat = t2 - t1
dlon = g2 - g1

# formula to calculate distance between two point of earth
a = math.sin(dlat / 2) ** 2 + math.cos(t1) * math.cos(t2) * math.sin(dlon / 2) ** 2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

distance = 6371.01 * c
print("The distance between the two points is {:.2f} kilometers.".format(distance))


# Exercise 13 : Making Change

PENNY_COINS = 1
NICKEL_COINS = 5
DIME_COINS = 10
QUARTER_COINS = 25
LOONIE_COINS = 100
TONIE_COINS = 200

change = input("Masukan kembalian yang ingin dipecahkan $")
change = int(change)

print(" ", change // TONIE_COINS, "toonies")
change = change % TONIE_COINS


# Exercise 14 : Height Unit

IN_PER_FT = 12
CM_PER_IN = 2.54


# Read the height from the user
print("Enter your height:")
feet = int(input(" Number of feet: "))
inches = int(input(" Number of inches: "))

# Compute the equivalent number of centimeters
cm = (feet * IN_PER_FT + inches) * CM_PER_IN

# Display the result
print("Your height in centimeters is:", cm)
