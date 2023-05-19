# Call convert function that take user Input
def main():
    userInput = input()
    print(convert(userInput)) # Print output after convert it 

# Convert user input
def convert(emotIcons):
    return emotIcons.replace(':)', '🙂').replace(':(', '🙁') # Return new string

# Call main function 
main()

# Test 
    # Input -> 'Happy :)', Output -> 'Happy 🙂'
    # Input -> 'Sad :(', Output -> 'Sad 🙁'