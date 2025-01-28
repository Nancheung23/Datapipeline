
"""
Function encode
---------------
Returns the string obtained by encoding the plaintext received as
the parameter 'text' as follows. 

Step 1) (max 1 XP): The value of the str parameter 'alphabet' is
used as the alphabet. Each letter of the plaintext is replaced by
the character found by moving forward in the alphabet by the
number of characters given by the integer parameter 'shift'.
(Naturally, if the shift (the value of the 'shift' parameter) is
negative, the movement is backwards in the alphabet (i.e., to the
left / from the end towards the beginning) by the absolute value
of the shift.) The alphabet is interpreted as circular, so that 
the character following the last character of the alphabet is 
considered to be the first character, and similarly, the last
character is considered to precede the first character. If the
boolean parameter 'simple' is True, the encoded string produced
by Step 1 is returned. Otherwise, proceed to Step 2.

Step 2) (max 1 XP, requires that Step 1 is implemented and OK):
The encoded text obtained in Step 1 is further scrambled so that
each complete, separate substring of length defined by the integer
parameter 'revlen' is reversed (that is, the order of the characters
is reversed regarding the substring) while maintaining the original
mutual order of the substrings). It can be assumed that the value
of the parameter 'revlen' is a natural number not larger than the
length of the string to be scrambled. If the length of the string
to be scrambled is not divisible by the value of the parameter
'revlen' and thus there are leftover characters at the end of the
string, these are retained as they are without reversing.
(For example, the string 'ABCDEFGH' and revlen=3 -> 'CBAFEDGH').
The scrambled string obtained by rearranging the order as described
is returned.
"""

def encode(text, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789 ',
        shift=0, revlen=3, simple=False):
    if not text:
        return ""
    strL = ""
    # simple
    for char in text:
        index = alphabet.find(char)
        if index == -1:
            strL += char
            continue
        new_index = (index + shift) % len(alphabet)
        strL += alphabet[new_index]
    if simple:
        return strL
    else:
        arr = [strL[i:i + revlen] for i in range(0, len(strL), revlen)]
        scrambled = ''.join(piece[::-1] for piece in arr[:-1]) 
        if len(arr[-1]) < revlen:
            scrambled += arr[-1]
        else:
            scrambled += arr[-1][::-1]
        return scrambled

"""
Function neighbor_count_map
(max 1 XP)
--------------------------
Takes as a parameter a list of tuples in (x, y) format,
which contain coordinate information defining the locations
of objects on a 19 * 9 character map. After reading the
locations, the function prints a representation of the
situation on the map as ASCII graphics. On the map, a
tilde (~) represents an empty area where no objects are
known to exist, and each object is marked with a number
from 0 to 8 corresponding to the number of its neighboring
objects. (Diagonal neighbors are also counted as neighbors.)
The coordinate (0, 0) is in the top-left corner of the map,
and the coordinate (18, 8) is in the bottom-right corner,
meaning y-coordinates increase downwards and x-coordinates
to the right.

Even if an object is pointed to the same place multiple times,
repetition does not alter the behavior - only one object can 
fit in one place (corresponding to one character on the map).
However, the program must not crash or malfunction if duplicate
coordinate points are given.

In addition to printing the map, the program should return a 
dictionary (dict) where the keys are tuples corresponding to
the coordinate information of the objects, and the values are
the numbers of their respective neighboring objects as integers.
(The dict does not need to include information about the neighbors
of empty map locations.)

Example:

d = neighbor_count_map([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), 
                        (5, 5), (6, 6), (7, 7), (8, 8), (2, 1),
                        (2, 0), (2, 3), (2, 4), (2, 2), (8, 4)]) 
...prints the map 
1~2~~~~~~~~~~~~~~~~
~43~~~~~~~~~~~~~~~~
~~4~~~~~~~~~~~~~~~~
~~34~~~~~~~~~~~~~~~
~~2~2~~~0~~~~~~~~~~
~~~~~2~~~~~~~~~~~~~
~~~~~~2~~~~~~~~~~~~
~~~~~~~2~~~~~~~~~~~
~~~~~~~~1~~~~~~~~~~

...and then, e.g., print(d[(2, 3)]) would print the value 3.

"""

def neighbor_count_map(object_locations):
    if not object_locations:
        return {}
    width, height = 19, 9
    map_default = [['~' for _ in range(width)] for _ in range(height)]
    object_set = set(object_locations)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),         (0, 1),
                (1, -1), (1, 0), (1, 1)]
    neighbor_dict = {}
    for x, y in object_set:
        if not (0 <= x < width and 0 <= y < height):
            continue
        neighbor_count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in object_set:
                neighbor_count += 1
        map_default[y][x] = str(neighbor_count)
        neighbor_dict[(x, y)] = neighbor_count
    for row in map_default:
        print(''.join(row))
    return neighbor_dict
