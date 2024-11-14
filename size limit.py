def check_zander_size():
    # Define the size limit for zander
    size_limit = 42
    
    # Ask the fisher for the length of the zander
    try:
        length = float(input("Enter the length of the zander in centimeters: "))
        
        # Check if the length meets the size limit
        if length < size_limit:
            # Calculate how many centimeters below the limit
            difference = size_limit - length
            print(f"The zander does not meet the size limit. Please release it back into the lake.")
            print(f"The zander is {difference:.2f} centimeters below the size limit.")
        else:
            print("The zander meets the size limit. You can keep it.")
    
    except ValueError:
        print("Please enter a valid number.")

# Call the function
check_zander_size()
