from tkinter import *
import sqlite3


root = Tk()
root.title("Car rentals company")

#creating or connecting to a database
conn = sqlite3.connect('personal_details.db')


#creating a cursor
c = conn.cursor() 

#create table
c.exectue("""CREATE TABLE addresses (
        name text,
        postcode integer,
        email text,
        DOB integer,
        started_driving integer

        )""")


#commit changes
conn.commit()

#closing connection
con.close()
