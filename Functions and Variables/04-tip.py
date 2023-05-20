# Calculate Tip and print it out 
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Convert price to float and remove $ sign 
def dollars_to_float(d):
    return float(d.lstrip('$'))

# Convert tip percentage and remove % sign 
def percent_to_float(p):
    return float(p.rstrip('%')) / 100

# Call main function
main()

# Test 
    # Input -> ($50.00, 15%), Output -> $7.50
    # Input -> ($100.00, 18%), Output -> $18.00
    # Input -> ($15.00, 25%), Output -> $3.75 