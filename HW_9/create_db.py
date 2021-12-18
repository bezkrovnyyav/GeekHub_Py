import sqlite3

def create_db():
    conn = sqlite3.connect('atm.db')
    cur = conn.cursor()

    fop = open('atm.db', 'w')
    fop.close()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
           user_id INT PRIMARY KEY,
           username TEXT,
           password TEXT,
           balance INT,
           status TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS denominations (
           denomination INT PRIMARY KEY,
           count INT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS transactions (
          transaction_id INT PRIMARY KEY,
          operation TEXT,
          username TEXT)""")
    users = [('1', 'user1', 'user1', '1500', 'Active'),
             ('2', 'user2', 'user2', '1500', 'Active'),
             ('3', 'admin', 'admin', '30000', 'Collector')
             ]
    denominations = [(10, 100),
                     (20, 100),
                     (50, 100),
                     (100, 100),
                     (200, 100),
                     (500, 100),
                     (1000, 100)
                     ]
    cur.executemany("""INSERT INTO users VALUES(?,?,?,?,?);""", users)
    cur.executemany("""INSERT INTO denominations VALUES(?,?);""", denominations)
    cur.execute("""CREATE TABLE IF NOT EXISTS transactions (
               id INT PRIMARY KEY,
               operations TEXT)
               """)
    conn.commit()

create_db()
