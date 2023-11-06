
# importing-------------------------------------------------------------------------------------------------------------

import psycopg2
import csv

# connects to the sql database------------------------------------------------------------------------------------------

conn = psycopg2.connect(
    dbname = "mod2",
    user = "postgres",
    password = "HeavyThunderstorms1!",
    host = "localhost",
    port = "5432"
    )

# makes a cursor--------------------------------------------------------------------------------------------------------

cursor = conn.cursor()

# executes an sql query to save the values for every item in the csv file-----------------------------------------------

with open('info.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        cursor.execute(
            "INSERT INTO comments (name, comment, datetime, station) VALUES (%s, %s, %s, %s)",row
        )


with open('moderation.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        cursor.execute(
            "INSERT INTO moderation (name, email, time) VALUES (%s, %s, %s)",row
        )

# commits the changes and closes the connections------------------------------------------------------------------------

conn.commit()
cursor.close()
conn.close()

# opens the file in write mode and then passes to flush the file so the values don't get commited twice0-----------------

with open("info.csv", "w"):
    pass

with open("moderation.csv", "w"):
    pass

# print-----------------------------------------------------------------------------------------------------------------

print("your data has been commited!")

# ----------------------------------------------------------------------------------------------------------------------
