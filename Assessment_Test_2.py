import psycopg2 as pg2
import json
import pandas as pd

#create a function
def init():
    FILE = open("secret_info.json", encoding='utf-8')
    secret_info = json.load(FILE)
    conn = pg2.connect(database='exercises', user=secret_info["username"], password=secret_info["password"])
    return conn.cursor()

def question_1(cur):
    cur.execute("""SELECT * 
                    FROM cd.facilities""")

def question_2(cur):
    cur.execute("""SELECT name, membercost 
                    FROM cd.facilities""")

def question_3(cur):
    cur.execute("""SELECT * 
                    FROM cd.facilities 
                    WHERE membercost > 0""")

def question_4(cur):
    cur.execute("""SELECT * 
                    FROM cd.facilities 
                    WHERE membercost > 0 AND membercost < monthlymaintenance / 50""")

def question_5(cur):
    cur.execute("""SELECT * 
                    FROM cd.facilities 
                    WHERE name LIKE '%Tennis%'""")

def question_6(cur):
    cur.execute("""SELECT * 
                    FROM cd.facilities 
                    WHERE name LIKE '%2'""")

def question_7(cur):
    cur.execute("""SELECT memid, surname, firstname, joindate 
                    FROM cd.members 
                    WHERE joindate > '2012-09-01'""")

def question_8(cur):
    cur.execute("""SELECT DISTINCT surname 
                    FROM cd.members 
                    ORDER BY surname 
                    LIMIT 10""")

def question_9(cur):
    cur.execute("""SELECT joindate, surname 
                    FROM cd.members 
                    ORDER BY joindate DESC 
                    LIMIT 1""")

def question_10(cur):
    cur.execute("""SELECT COUNT(*) 
                    FROM cd.facilities
                    WHERE guestcost >= 10""")

def question_11(cur):
    cur.execute("""SELECT SUM(slots) AS Total_Slots
                   FROM cd.bookings 
                   WHERE starttime >= '2012-09-01' AND starttime <= '2012-10-01'
                   GROUP BY facid
                   ORDER BY Total_Slots""")
    
def question_12(cur):
    cur.execute("""SELECT facid,SUM(slots) AS Total_Slots
                   FROM cd.bookings
                   GROUP BY facid
                   HAVING SUM(slots) > '1000'
                   ORDER BY facid""")
    
def question_13(cur):
    cur.execute("""SELECT name,cd.bookings.starttime
                   FROM cd.facilities
                   INNER JOIN cd.bookings
                   ON cd.facilities.facid = cd.bookings.facid
                   WHERE name LIKE '%Tennis Court%'
                   AND cd.bookings.starttime >= '2012-09-21'
                   AND cd.bookings.starttime < '2012-09-22'
                   ORDER BY cd.bookings.starttime""")
    
def question_14(cur):
     cur.execute("""SELECT surname, firstname, cd.bookings.starttime
                   FROM cd.members
                   INNER JOIN cd.bookings
                   ON cd.members.memid = cd.bookings.memid
                   WHERE surname = 'Farrell' AND firstname = 'David'""")
    
def main():
    cur = init()
    question_14(cur)

    # Command for printing the output
    result = cur.fetchall()
    col_names = [desc[0] for desc in cur.description]
    df = pd.DataFrame(result, columns=col_names)
    print(df)

if __name__ == "__main__":
    main()