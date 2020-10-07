"""
File: lines.py
Description: Display requested lines in a file.
"""

def main():
    line_list = read_file()
    line_num = len(line_list)
    print(f"There are {line_num} lines in the file.")
    while True:
        num = int(input("Which line number would you like to see?: "))
        if num == 0:
            break
        elif num > int(line_num):
            print(f"[+] Error: there are only {line_num} lines in the file.\n")
        else:
            print(line_list[num-1])

def read_file():
    """Prompt user for filename and read it
        line-by-line into a list.
    """
    file_name = input("What file would you like to read?: ")
    f = open(file_name, 'r')
    line_list = []
    while True:
        line = f.readline()
        if line == "":
            break
        line_list.append(line)
    return line_list
        
        

if __name__ == "__main__":
    main()


    
    
