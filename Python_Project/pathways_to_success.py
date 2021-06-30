# @TODO: Import the csv library
# YOUR CODE HERE!
import csv
from pathlib import Path
from typing import Counter
csvpath = Path("pathways_success.csv")
with open(csvpath) as csvfile:
    data = csv.reader(csvfile)
    Counter= 0
    for row in data:
        Counter= Counter + 1
        print("row counter", Counter)
        print(row)
    
# @TODO: Create a path to the csv file called `quarterly_data.csv`
# YOUR CODE HERE!

# @TODO: Open the csv path, read the data, and print each row
# YOUR CODE HERE!

"""Extension.

This is an optional extension to the activity.

Create a variable above the `for` loop named `Counter`
and set it equal to zero. Then, every time a new row
is read within the `for` loop, add a value of 1 to
this variable.
"""

# @TODO: Add a row counter to the CSV data.
# YOUR CODE HERE!




print(f"This is the relative path: {csvpath}")
print(f"This is the absolute path: {csvpath.absolute()}")
