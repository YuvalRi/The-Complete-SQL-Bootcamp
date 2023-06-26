import psycopg2 as pg2
import json
import pandas as pd

def main():
    file = open("secret_info.json", encoding='utf-8')
    secret_info = json.load(file)
    conn = pg2.connect(database='exercises', user=secret_info["username"], password=secret_info["password"])
    cur = conn.cursor()
    cur.execute('SELECT * FROM cd.facilities')
    rows = cur.fetchall()

    col_names = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=col_names)
    print(df)

if __name__ == "__main__":
    main()