# Take user input and pass it to the energyCalc function
def main():
    userInput = int(input())
    print(energyCalc(userInput)) # Print output

# Take user Input as mass and return Energy value
def energyCalc(mass):
    return ( mass * 300000000**2 )

# Call main function
main()

# Test
    # Input -> 1, Output -> 90000000000000000
    # Input -> 14, Output -> 1260000000000000000
    # Input -> 50, Output -> 4500000000000000000
