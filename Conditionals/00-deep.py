# Take user answer 
def main():
    userInput = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    print(userAnswer(userInput))

# Check if the right answer 
def userAnswer(answer):
    answer = answer.lower()
    if answer == '42' or answer == 'forty-two' or answer == 'forty two':
        return 'Yes'
    else:
        return 'No'

# Call main function
main()

# Test 
    # Input -> '42', Output -> 'Yes'
    # Input -> 'forty-two', Output -> 'Yes'
    # Input -> 'forty two', Output -> 'Yes'
    # Input -> 'Forty Two', Output -> 'Yes'
    # Input -> '50', Output -> 'No'