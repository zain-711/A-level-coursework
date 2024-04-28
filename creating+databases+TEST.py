from tkinter import *
import sqlite3

root = Tk()
root.title("testing databases")
#creating or connecting to a database
conn = sqlite3.connect('personal_details.db')

#creating a cursor
c = conn.cursor() 

#create table
'''
c.exectue("""CREATE TABLE details (
        name text,
        postcode integer,
        email text,
        DOB integer,
        started_driving integer

        )""")
'''

#creating submit function
def submit():
    #creating or connecting to a database
    conn = sqlite3.connect('personal_details.db')
    #creating a cursor
    c = conn.cursor()
    
    #insert into table
    c.execute("INSERT INTO details VALUES (:name, :postcode, :email, :DOB, :started_driving)",
              {
                'name': name.get(),
                'postcode': postcode.get(),
                'email' : email.get(),
                'DOB' : DOB.get(),
                'started_driving' : started_driving.get()
              })    
    #commit changes
    conn.commit()
    #closing connection
    conn.close()
