"""
Author: Noa Kirschbaum
Assignment / Part: HW8 - Q1
Date due: 2022-04-14
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def format_latin_text(unformatted_latin_text):
    output_string = unformatted_latin_text
    if len(output_string) > 0:
        output_string = output_string.upper()
        output_string = output_string.replace("U", "V")

    return output_string

def get_unformatted_text(file_name):
    #extract file
    lst_lines = []

    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        return lst_lines

    #write to new list
    for line in file:
        lst_lines.append(line.strip())

    #close file
    file.close()
    #return contents in list
    return lst_lines

def print_formatted_latin(input_file_path):
    last_part = input_file_path.rfind("/") + 1
    file_in = input_file_path[last_part:]

    lst_un_txt = get_unformatted_text(file_in)

    for item in lst_un_txt:
        print(format_latin_text(item))

def main():
    print_formatted_latin("assets/files/imperatoria_verba.txt")

if __name__ == "__main__":
    main()
