## this is single line comment
'''
this is a example of multiline comments
'''
'''
Ronaldo is goat



'''
# Initialize total sum
total_sum = 0

while True:
    try:
        # Ask the user to input numbers separated by spaces
        user_input = input("Enter numbers separated by spaces (enter 0 to stop): ").strip()

        # Split the input into a list of strings
        numbers = user_input.split()

        for num_str in numbers:
            # Convert each string to a number
            number = float(num_str)

            # Check if the number is 0
            if number == 0:
                print("The sum of all entered numbers is:", total_sum)
                exit()  # Exit the program

            # Add the number to the total sum
            total_sum += number
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter numbers separated by spaces.")


