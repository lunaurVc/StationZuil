
# importning and defining-----------------------------------------------------------------------------------------------

import csv
import datetime

approved_lines = []

# requests name and email-----------------------------------------------------------------------------------------------

name = input("moderators name : ")
email = input("\nmoderators email-adress : ")

print("""\npress 1 to clear the comment and send it to the database\npress 2 to turn down the comment and delete it
please dont forget to look at the name\n""")

# opens the csv file and asigns it to a variable to be able to be used later in the code--------------------------------

with open('info.csv', 'r') as file:
    reader = csv.reader(file)
    rows = [row for row in reader]

# lets the user turn down the comment and name for every item in the csv------------------------------------------------

for lines in rows:
    print("name :", lines[0],)
    print("\ncomment :", lines[1])
    while True:
        answer = input("\ndo you approve of this comment? : ")
        if answer == "1":
            approved_lines.append(lines)
            print("comment verified\n")
            time = datetime.datetime.now()
            with open('moderation.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, email, time])
            break
        elif answer == "2":
            print("comment removed\n")
            break
        else:
            print("please input a valid number")
            continue

# notates the time of the moderation------------------------------------------------------------------------------------

time = datetime.datetime.now()

# rewrites the csv file with only the approved comments-----------------------------------------------------------------

with open('info.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(approved_lines)

# ----------------------------------------------------------------------------------------------------------------------
