# Need to move line_count function into main; just use read_file to inout and split file

"""
File: lines.py
Description: Display requested lines in a file.
"""


   
def main():
    
    lines = read_file()
    line_num = line_counter()
    print(f"There are {line_num} lines in the file.")
    while True:
        num = int(input("Which line number would you like to see?: "))
        if num == 0:
            break
        elif num > int(line_num):
            print(f"[+] Error: there are only {line_count} lines in the file.")
        else:
            print(lines[num])

def read_file():
    """Prompt user for filename and read it
        line-by-line into a list.
    """
    # file_name = input("What file would you like to read?: ")
    file_name = "frankly.txt"
    f = open(file_name, 'r')
    line_list = []
    while True:
        line = f.readline()
        if line == "":
            break
        line_list.append(line)
    return line_list

def line_counter():
    line_count == 0
    for line in lines:
        line_count += 1

    return line_count
        
        

    

if __name__ == "__main__":
    main()


    
    