import psycopg2 as pg2
import json
import pandas as pd


FILE = open("secret_info.json", encoding='utf-8')
secret_info = json.load(FILE)
conn = pg2.connect(database='exercises', user=secret_info["username"], password=secret_info["password"])
cur = conn.cursor()


def question_1():
    # SQL command
    cur.execute('SELECT * FROM cd.facilities')

def question_2():
    # SQL command
    cur.execute('SELECT name, membercost FROM cd.facilities')

def question_3():
    cur.execute('SELECT * FROM cd.facilities WHERE membercost > 0')

def question_4():
    cur.execute('SELECT * FROM cd.facilities WHERE membercost > 0 AND membercost < monthlymaintenance / 50')

def question_5():
    cur.execute("SELECT * FROM cd.facilities WHERE name LIKE '%Tennis%'")

def quesion_6():
    cur.execute("SELECT * FROM cd.facilities WHERE name LIKE '%2'")


def main():
    #question_1()
    #question_2()
    #question_3()
    #question_4()
    #question_5()
    #quesion_6()

    # Command for printing the output
    rows = cur.fetchall()
    col_names = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=col_names)
    print(df)

if __name__ == "__main__":
    main()