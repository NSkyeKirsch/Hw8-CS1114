"""
Author: Noa Kirschbaum
Assignment / Part: HW8 - Q2
Date due: 2022-04-14
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def clean_up(input_file_name, characters_to_remove, output_file_name):

    out_file = open(output_file_name, 'w')

    try:
        file = open(input_file_name, 'r')
    except FileNotFoundError:
        out_file.write("INPUT FILE NOT FOUND")


    for line in file:
        out_line = line
        for item in characters_to_remove:

            out_line = out_line.replace(item, "")

        out_file.write(out_line)

    file.close()
    out_file.close()

def main():
    clean_up("the_social_contract.txt", ["a", "i", "o", "u", "e"], "clean.txt")

if __name__ == "__main__":
    main()