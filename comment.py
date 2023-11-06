
# defining and importing things-----------------------------------------------------------------------------------------

import random
import datetime
import csv

stations_list = ["Arnhem", "Den Haag", "Nijmegen", "Utrecht", "Zutphen"]
name = ""

# idle screen-----------------------------------------------------------------------------------------------------------

print("1 for yes\n2 for no\n")
while True:
    start_yn = input("would you like to leave a comment? : ")
    if start_yn == "1":
        break
    elif start_yn == "2":
        print("\nhave a great day!\nplease step away from the console.\n")
        continue
    else:
        print("\nplease enter a valid command.\n")
        continue

# requesting name-------------------------------------------------------------------------------------------------------

while True:
    name_yn = input("\nwhould you like to enter a name? : ")
    if name_yn == "1":
        name = input("\nwhat is your name? : ")
        if 0 < len(name) < 255:
            break
        else:
            print("name must be between 1 and 255 characters")
            continue
    elif name_yn == "2":
        name = "anonymous"
        break
    else:
        print("\nplease enter a valid command.")
        continue

# requesting comment----------------------------------------------------------------------------------------------------

print("\nplease keep your comment under 140 characters.")
while True:
    comment = input("please leave your comment here : ")
    if len(comment) >= 141:
        print("please keep your comment under 140 characters")
        continue
    elif len(comment) == 0:
        print("comment cannot be empty")
        continue
    else:
        print("\nthank you for your participation!")
        break

# records time----------------------------------------------------------------------------------------------------------

time = datetime.datetime.now()

# chooses a station-----------------------------------------------------------------------------------------------------

station = stations_list[random.randint(0,4)]

# saves the information to a .csv file----------------------------------------------------------------------------------

with open('info.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, comment, time, station])

# ----------------------------------------------------------------------------------------------------------------------
