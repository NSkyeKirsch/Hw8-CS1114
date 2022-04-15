"""
Author: Noa Kirschbaum
Assignment / Part: HW8 - Q3
Date due: 2022-04-14
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""


def get_longest_word(file_name):
    longest_word = ""
    words = []
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        return longest_word

    for line in file:
        line = line.strip().split()
        words.extend(line)

    for ind in range(len(words)):
        if ind == 0:
            longest_word = words[ind]
        else:
            if len(longest_word) <= len(words[ind]):
                longest_word = words[ind]

    return longest_word

    file.close()


def main():
    file_path = "los_justos.txt"
    print(get_longest_word(file_path))


if __name__ == "__main__":
    main()
