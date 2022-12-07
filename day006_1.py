import string

from common import get_input

buffer = get_input(6)
# buffer = "nppdvjthqldpwncqszvftbrmjlhg"


def determine_start_marker(buffer, marker_length):
    substr = ""
    for i, char in enumerate(buffer):
        index_of_first_repeat = substr.find(char)
        if index_of_first_repeat != -1:
            substr = substr[index_of_first_repeat +1:]
            substr += char
        else:
            substr += char

        if len(substr) == marker_length:
            return i + 1


def markers(buffer, marker_length):
    l = 0
    r = 4
    substr = set(buffer[l:r+1])
    while len(substr) != 4:
        if buffer[r+1] in substr:
            r += 1
            while buffer[l] != buffer[r]:
                l += 1
        substr = set(buffer[l:r+1])
    return r

print(determine_start_marker(buffer, 14))



