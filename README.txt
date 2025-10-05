========================================
README.txt - CardBalance Tracker Script
Author: Kristian Tokos
Date: 08.23.2025
University at Albany — Computer Science Major
========================================

DESCRIPTION:
------------
This Python script reads a user's card balance from a file, allows them to add a new purchase, and updates the remaining balance accordingly. 
It appends the new purchase to the file and recalculates the total cost of all purchases listed.

REQUIRED FILE:
--------------
CardBalance.txt — Must exist in the same directory as the script.
Format:
    Starting Balance: <float>
    Remaining Balance: <float>
    
    Purchases:
    <Purchase Name> - <Price>
    <Purchase Name> - <Price>
    ...

USAGE:
------
1. Run the script.
2. When prompted:
   - Enter "yes" to add a new purchase.
   - Provide the name and price of the purchase.
3. The script will:
   - Append the new purchase to the file.
   - Recalculate the total cost.
   - Update the remaining balance.
   - Rewrite the file with updated data.

NOTES:
------
- If the user enters "no", no changes are made.
- Malformed purchase lines (missing price or delimiter) are skipped with a warning.
- All prices must be valid float values.
- The script assumes the first line contains the starting balance and the second line will be overwritten with the new remaining balance.

EXAMPLE FILE CONTENT BEFORE RUNNING:
------------------------------------
Starting Balance: 100.00
Remaining Balance: 100.00

Purchases:
Coffee - 3.50
Book - 12.99

EXAMPLE FILE CONTENT AFTER ADDING A PURCHASE:
---------------------------------------------
Starting Balance: 100.00
Remaining Balance: 83.51

Purchases:
Coffee - 3.50
Book - 12.99
Notebook - 10.00

AUTHOR NOTES:
-------------
This script was created as part of a hands-on exploration of file I/O, string parsing, and interactive user input in Python. It reflects a modular and readable design for future extension.
