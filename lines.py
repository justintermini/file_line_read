"""
File: lines.py
Description: Display requested lines in a file.
"""

def main():
    # Call the read_file function to create a list from file.
    line_list = read_file()
    # Get the number of lines in the list and print it .
    line_num = len(line_list)
    print(f"There are {line_num} lines in the file.")

    # Prompt user to choose a line to view. Loop until user chooses '0'.
    while True:
        num = int(input("Which line number would you like to see? "
                        "(Choose '0' to exit): "))
        if num == 0: # Exit code for program.
            break
        elif num > int(line_num): # Produce error if number is too high.
            print(f"[+] Error: there are only {line_num} lines in the file.\n")
        else: # Output line.
            print(line_list[num-1])

def read_file():
    """Prompt user for filename and read it line-by-line into a list."""
    # Prompt user for file name.
    file_name = input("What file would you like to read?: ")
    # Read file into varaible 'f'.
    f = open(file_name, 'r')
    line_list = []
    # Split up file line by line into a list, then return list variable.
    while True:
        line = f.readline()
        if line == "":
            break
        line_list.append(line)
    return line_list
        
if __name__ == "__main__":
    main()


    
    
