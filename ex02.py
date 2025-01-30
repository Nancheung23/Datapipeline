import requests
import statistics
import sys
import json
import os.path
import sqlite3

"""
GENERAL INSTRUCTIONS:

Complete the implementations of the functions so that the functions 
work as described. Do not change the names (of the functions or this
file) or the parameterization in any way. Submit the completed ex02.py
to the respective assignment submission area in Moodle. 

Clean up any unnecessary code from the version to be submitted.
You can use helper functions, but remove the calls to the functions
requested to be implemented and any extra print statements (that are
not requested by the instructions) from the file to be submitted. 
(Do not worry, the functions will be called during the evaluation. 
However, if there are extra prints or calls with some other than the 
actual test data, that makes the test process unnecessarily confusing.)

You can assume the requests library is available. (Install it for 
yourself, possibly in a virtual environment (pip install requests).) 
No other assumptions should be made about the availability of external 
libraries not included in the standard Python distribution.
"""

"""
Function csv_value_count (max 1 XP)
-----------------------------------

The function uses a CSV file as its data source. The name of the file is 
provided as the parameter "file_name". (It can be expected that the file 
can be found without any specific path information in the testing environment,
so referring to the file by its name alone is sufficient for the purposes of 
this task.) You can assume that the CSV file uses UTF8 character encoding and 
a comma as the delimiter. Also, the first row of the file being a header row 
containing the column names can be assumed.

The function returns the number of occurrences of the value specified by the 
parameter "search_value" in the column whose name is given by the parameter 
"column_name".

The data in the file is naturally text, but some values can be interpreted 
as integers or floating-point numbers in addition to strings. The code should 
be able to perform the necessary conversions based on the type of the 
value of search_value and handle potential error situations to ensure that
the code works correctly. (Hint: type())

To test the functionality of the solution, you can use, for example, 
the file classroom_measurements.csv available in Moodle and try what your code
returns with, e.g., these calls:
csv_value_count('classroom_measurements.csv', 'id', 56269)
csv_value_count('classroom_measurements.csv', 'value', 23.5)
csv_value_count('classroom_measurements.csv', 'time', '09:11:44.407707')
However, it is advisable to test more comprehensively.
"""

def csv_value_count(file_name: str, 
                    column_name: str, 
                    search_value: str) -> int:
    # check file_name
    if not os.path.isfile(file_name):
        return f"Can't find file {file_name}"
    # open file
    with open(file_name) as file:
        # get first column
        names = file.readline().strip().split(",")
        # check column_name
        if (column_name in names):
            index = names.index(column_name)
            # value count
            count = 0
            for line in file:
                data = line.strip().split(",")
                if (str(data[index]) == str(search_value)):
                    count += 1
                else:
                    continue
            if (count == 0):
                return f"found no result of {search_value}"
            return count
        else:
            return f"{column_name} is not a valid value"
# print(csv_value_count("classroom_measurements.csv", 'id', 56269))
# print(csv_value_count('classroom_measurements.csv', 'value', 23.5))
# print(csv_value_count('classroom_measurements.csv', 'time', '09:11:44.407707'))

"""
Function analyze_json_from_api (max 1 XP)
-----------------------------------------

The function reads JSON content from the address 
https://www.freetogame.com/api/games (the source of the data: 
FreeToGame.com) with a normal GET request. (Hardcoding the address 
in the function is perfectly OK in this case.) 
Consider only PC games in the dataset. (You can limit the 
request to PC games only by using query parameters – see 
https://www.freetogame.com/api-doc).

Based on the data received, the function answers the following
questions:
1. How many different game genres (according to exact spellings)
does the material contain? (I.e., from how many different genres
are there games in the dataset?)
2. What is the third largest game genre in the dataset 
(measured by the number of games representing it)?
3. What is the average number of games per genre in the dataset?
4. What is the median number of games per genre in the dataset?

The function returns the answers as a list in the order of the 
questions. (The zeroth element of the list is the answer to the 
first question, and so on). The answer to question 1 is an integer
(int), the answer to question 2 is a string (str), and the other 
answers are included in the list as floating-point numbers (float).
Ensure returning the list with the correct types.
"""

def analyze_json_from_api() -> list:
    url = "https://www.freetogame.com/api/games?platform=pc"

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        # data type: id, title, thumbnail, short_Description, game_url, genre, platform, publisher, developer, release_date, freetogame_profile_url
        # question 1
        genres = set()
        for game in data:
            genres.add(game["genre"])
        genres = list(genres)
        question_1 = len(genres)
        # question 2
        data_dict = {genre: 0 for genre in genres}
        for game in data:
            if game["genre"] in genres:
                data_dict[game["genre"]] += 1
        # sort
        sorted_items = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)
        question_2 = sorted_items[2][0]
        # question 3
        total_games = sum(data_dict.values())
        question_3 = total_games / question_1
        # question 4
        question_4 = statistics.median(data_dict.values())
        return [question_1, question_2, question_3, question_4]
    except requests.exceptions.RequestException as error:
        return f"Error fetching data {error}"

# print(analyze_json_from_api())

"""
Function data_from_db (max 1 XP)
--------------------------------

The function reads data from a file-based SQLite database. 
The name of the database file (that can be assumed to be 
found without any specific path information in the testing)
is provided as the parameter "db_file".

The database is a simple one-table database with the following
structure:
- Table name: measurements
- Columns: id (INTEGER), date (TEXT), time (TEXT), type (TEXT),
        source (TEXT), value (REAL)

In order to see example values that the table measurements
could contain, consult the file classroom_measurements.csv.
(Also a database file classroom_measurements.db is available
in Moodle. The test database will be comparable to that – the
structure is the same, but the number of rows and the actual
values may differ. There are always some rows, though.)

Based on the data in the database, the function answers the 
following questions:
1. What is the minimum value of the humidity measurements
from the source 'z-02'? Answer as a float.
2. What is the average temperature? (Consider all the values
related to type 'temperature'.) Answer as a float.
3. How many rows of data are there in the table measurements? 
Answer as an int.
4. How many measurements of type 'pressure' were made before 
10:43:00 (only consider the time, not the date)? Answer as an int.

The function returns the answers as a list in the order of the 
questions. (The zeroth element of the list is the answer to the 
first question, and so on). Ensure that the types of the
elements of the list are as instructed.
"""

def data_from_db(db_file: str) -> list:
    try:
        connecton = sqlite3.connect(db_file)
        cursor = connecton.cursor()
        # min_humidity
        cursor.execute("SELECT MIN(value) FROM measurements WHERE source='z-02' AND type='humidity'")
        min_humidity = cursor.fetchone()[0]
        # Average temperature value
        cursor.execute("SELECT AVG(value) FROM measurements WHERE type='temperature'")
        avg_temperature = cursor.fetchone()[0]
        # Total number of rows in the table
        cursor.execute("SELECT COUNT(*) FROM measurements")
        total_rows = cursor.fetchone()[0]
        # Count of 'pressure' measurements before '10:43:00'
        cursor.execute("SELECT COUNT(*) FROM measurements WHERE type='pressure' AND time < '10:43:00'")
        pressure_before_1043 = cursor.fetchone()[0]
        connecton.close()
        return [float(min_humidity), float(avg_temperature), int(total_rows), int(pressure_before_1043)]
    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return None