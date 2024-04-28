from tkinter import *

import sqlite3


root = Tk()
root.title("Car rentals company")

#creating a database
conn = sqlite3.connect('Customer_details.db')

#create cursor
c = conn.cursor()

#create table
c.execute("""CREATE TABLE IF NOT EXISTS personal_details (
        name text,
        postcode text,
        email text,
        YOB integer,
        experience integer
        )""") #"integer" and "text" represents the data type
#create table if not exists checks if the table was already created and creates a new one depending on that


def save_to_database():
        conn = sqlite3.connect('Customer_details.db')
        c = conn.cursor()

        #insert into table
        c.execute("INSERT INTO personal_details VALUES (:name, :postcode, :email, :YOB, :experience)",
                {
                    'name':name.get(),
                    'postcode':postcode.get(),
                    'email':email.get(),
                    'YOB':YOB.get(),
                    'experience':experience.get()
                })

        #commit changes
        conn.commit()

        #close connection
        conn.close()
        
        #clears the boxes
        name.delete(0, 'end')
        postcode.delete(0, 'end')
        email.delete(0, 'end')
        YOB.delete(0, 'end')
        experience.delete(0, 'end')

#create query function
def query():
    conn = sqlite3.connect('Customer_details.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM personal_details") #select all values
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + "\n" # converts all data to string

    query_label = Label(root, text=print_records)
    query_label.grid(row=14, column=0) #prints on the GUI using a label
    
    #commit changes
    conn.commit()

    #close connection
    conn.close()




def validation(): #validate the inputs and correct the user
        save = 0
        if len(name.get()) == 0:#If statement checks if name box is empty
            error_name.config(text="Please enter a valid name",fg = "red")
            save = save + 1
        else:
            error_name.config(text="Valid",fg = "green")

                 
        if len(postcode.get()) == 0:#If statement checks if email box is empty
            error_postcode.config(text="Please enter a valid postcode",fg = "red")
            save = save + 1
        else:
            error_postcode.config(text="Valid",fg = "green")

        
        if len(email.get()) == 0:#If statement checks if postcode is empty
            error_email.config(text="Please enter a valid email",fg = "red")
            save = save + 1
        else:
            error_email.config(text="Valid",fg = "green")

            
        try:
            int(YOB.get()) #Checks to see if the number entered is an integer
            error_YOB.config(text="Valid",fg = "green")
        except ValueError:
            error_YOB.config(text="Please enter only numbers in the format given",fg = "red")
            save = save + 1

        try: 
            int(experience.get()) #Checks to see if the number entered is an integer in experience box
            error_experience.config(text="Valid", fg = "green")
        except ValueError:
            error_experience.config(text="Please enter only numbers in the format given", fg = "red")
            save = save + 1
        
        if save > 0: # checks to see if any of the if statements changed the variable which means that the inputs by the user are incorrect
                error_message.config(text="Please make corrections before continuing", fg = "red")
        else:
                error_message.config(text='')
                save_to_database()

            


#creating a label widget
spacer_5 = Label(root, text="                           ", fg = "black", bg = "grey", width = "50", height = "3").grid(row = 0, column = 1)
title_label = Label(root, text="Welcome to Car rentals company", fg = "black", bg = "grey", width = "50", height = "3").grid(row=0, column=0)#placing labels in specific positions
sub_heading_label = Label(root, text="Step 1: enter your details").grid(row=1, column=0)
spacer_1 = Label(root, text="                           ").grid(row=2, column=0)
name_label = Label(root, text="Full name:   ").grid(row=3, column=0)
spacer_2 = Label(root, text="                           ").grid(row=4, column=0)
postcode_label = Label(root, text="Postcode:     ").grid(row=5, column=0)
spacer_3 = Label(root, text="                           ").grid(row=6, column=0)
email_label = Label(root, text="Email address:").grid(row=7, column=0)
spacer_4 = Label(root, text="                           ").grid(row=8, column=0)
YOB_label = Label(root, text="Date of birth (YYYY):").grid(row=9, column=0)
spacer_4 = Label(root, text="                           ").grid(row=10, column=0)
experience_label = Label(root, text="Years of experience (The minimum for all of our cars is one year):").grid(row=11, column=0)
error_YOB = Label(root, text = '', fg = "red")
error_YOB.grid(row=9, column=2,) #This label is only called when the user enters a string rather than an integer into the DOB box
error_experience = Label(root, text = '', fg = "red")
error_experience.grid(row=11, column=2,)
error_name = Label(root, text = '', fg = "red")
error_name.grid(row=3, column=2,)
error_postcode = Label(root, text = '', fg = "red")
error_postcode.grid(row=5, column=2,)
error_email = Label(root, text = '', fg = "red")
error_email.grid(row=7, column=2,)
error_message = Label(root, text = '', fg = "red")
error_message.grid(row= 13, column=1)

#creating input boxes for each field 
name = Entry(root, width = 20)
name.grid(row=3, column=1)
postcode = Entry(root, width = 20)
postcode.grid(row=5, column=1)

#create submit button
email = Entry(root, width = 30)
email.grid(row=7, column=1)
YOB = Entry(root, width = 10)
YOB.grid(row=9, column=1)
experience = Entry(root, width = 10)
experience.grid(row=11, column=1)


#create submit button
submit_btn = Button(root, text="Submit", command =validation)
submit_btn.grid(row=13, column=0, pady=10, padx=10)

#creating query button
query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=13, column=3, pady=10, padx=10)


#commit changes
conn.commit()

#close connection
conn.close()


root.mainloop()
