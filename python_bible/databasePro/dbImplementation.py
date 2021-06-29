import sqlite3

# to create a new database file on our disk, we need to use the connect
# method

conn = ""
if conn != "mydata.db":
    try:
        conn = sqlite3.connect("mydata.db")
        print("DB connection established")
    except:
        print("Error! Check the connection!")

#####################################################################
#                   EXECUTING STATEMENTS                             #
######################################################################


# In order to execute SQL statements, we will need to
# create a so-called cursor

c = conn.cursor()

#####################################################################
#                   CREATING TABLES                                 #
######################################################################
# table = "persons"
#
# while table:
#     if table == 'persons':
#         c.execute("""DEL TABLE persons""")
#         print("Table deleted")
#     else:
try:
    c.execute("""CREATE TABLE persons (
              first_name TEXT,
              last_name TEXT,
              age INTEGER )""")
except:
    print("Table already exists")

# statement is written but in order to really execute it, we ne need to
# commit to our connection.

#####################################################################
#                   INSERTING VALUES                                #
######################################################################
c.execute("""INSERT INTO persons VALUES
        ('John', 'Smith', 25),
        ('Anna', 'Smith', 30),
        ('Mike', 'Johnson', 40)""")

#####################################################################
#                   SELECTING VALUES                                #
######################################################################
c.execute("""SELECT * FROM persons
        WHERE last_name = 'Smith'""")


#####################################################################
#                   CLASSES AND TABLES                               #
######################################################################
class Person:
    def __init__(self, first=None, last=None, age=None):
        self.first = first
        self.last = last
        self.age = age

    def clone_person(self, result):
        self.first = result[0]
        self.last = result[1]
        self.age = result[2]


#####################################################################
#                   FROM TABLE TO OBJECT                              #
######################################################################
c.execute("""SELECT * FROM persons 
        WHERE last_name = 'Smith'""")

person1 = Person()
person1.clone_person(c.fetchone())

print(person1.first)
print(person1.last)
print(person1.age)
#####################################################################
#                   FROM OBJECT TO TABLE                               #
######################################################################
person2 = Person("Bob", "Davis", 23)

c.execute(f"""INSERT INTO persons VALUES
        ('{person2.first}', '{person2.last}', '{person2.age}')""")





#####################################################################
#                   PREPARED STATEMENTS                              #
######################################################################
person3 = Person("Kafayat", "Alabi", "50")

c.execute("INSERT INTO persons VALUES (?, ?, ?)",
          (person3.first, person3.last, person3.age))

c.execute("SELECT * FROM persons")
print(c.fetchall())

try:
    conn.execute("DROP TABLE persons")
    conn.execute("drop database mydata.db")
except sqlite3.Error as e:
    print(e)

try:
    c.execute("SELECT * FROM persons")
except sqlite3.Error as e:
    print(e)
print(c.fetchall())
conn.commit()
conn.close()
