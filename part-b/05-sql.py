import sqlite3

# connect to SQLite db or create if it doesn't exist
c = sqlite3.connect('05-sample.db')

# create a cursor object
db = c.cursor()

# create a table
db.execute("""
create table if not exists student(
    name text,
    email varchar(50),
    mmobile integer
)""")

# insert records into student // use executemany to insert records
list = [('abcd', 'abcd@gmail.com', 1234567890),
        ('efgh', 'eghj@gmail.com', 2143658709),
        ('zxcv', 'zxcv@gmail.com', 3126459780)
        ]
db.executemany("insert into student values(?,?,?)", list)

# update values
db.execute("""update student set name='hjkl' where name='efgh';""")

# delete record
db.execute("""delete from student where name='zxcv';""")

# display all records
db.execute("""select * from student;""")
records = db.fetchall()
for row in records:
    print(row)

# commit the changes and close connection
c.commit()
c.close()

