##
# Compute the area of the field , reporting the result in square acres
#

sq_per_acre=43560

# read the dimensions from the user
l=float(input("Enter the length of the field in feet : "))
w=float(input("Enter the width of the field in feet : "))

# Compute the area

acres=l*w/sq_per_acre

#display the result

print("The area of the field is ",acres," acres")