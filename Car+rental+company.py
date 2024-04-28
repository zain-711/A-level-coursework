from tkinter import *
from tkinter import ttk
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

        

#creating login system
def login():
        global code
        staff = Toplevel() #fourth window
        master = Label(staff, text = "Enter the master password").grid(row=0, column=0) 
        spacer_9 = Label(staff, text = "                      ").grid(row=1, column=0)
        error_pass = Label(staff, text = '').grid(row=2, column=1)
        master_entry = Entry(staff, width = 40)
        master_entry.grid(row=2, column=0)

        def search():
                staff.destroy()
                search = Toplevel() #Opens a new window after the login screen is terminated
                search.title("Database search") #New title as this is for the staff not the user
                heading = Label(search, text="Click the button below to veiw details", fg = "black", bg = "grey", width = "50", height = "3").grid(row=0, column=0)

                #create query function
                def query():
                    conn = sqlite3.connect('Customer_details.db')
                    c = conn.cursor()

                    c.execute("SELECT *,oid FROM personal_details") #select all values
                    records = c.fetchall()
                    print_records = ''
                    for record in records:
                        print_records += str(record) + "\n" # converts all data to string

                    query_label = Label(search, text=print_records)
                    query_label.grid(row=2, column=0) #prints on the GUI using a label

                    c.execute("SELECT *,oid FROM rent_details") #select all values from second table
                    records1 = c.fetchall()
                    print_records1 = ''
                    for record1 in records1:
                        print_records1 += str(record1) + "\n" # converts all data to string

                    query_label1 = Label(search, text=print_records1)
                    query_label1.grid(row=2, column=1) #prints on the GUI using a label


                    #commit changes
                    conn.commit()

                    #close connection
                    conn.close()

                submit3 = Button(search, text="View records", command =query)
                submit3.grid(row=2, column=0)
                        
        def pass_check():
                password = str("staff_search") #The master password i chose
                if master_entry.get() == password: #Checks if what user enters is the same as the password
                        search()
                else:
                        error_pass = Label(staff, text = "Incorrect, try again", fg = "red").grid(row=2, column=1)
        
        submit2 = Button(staff, text="Submit", command =pass_check)
        submit2.grid(row=3, column=0, pady=10, padx=10)



def open():
        global res  
        top = Toplevel()
        top.title("Car rentals company")
        step2 = Label(top, text="Step 2: Choose the car you would like to rent and enter how long for in the boxes below", fg = "black", bg = "grey", width = "75", height = "3").grid(row=0, column=0)
        spacer_6 = Label(top, text="                                         ").grid(row=1, column=0)
        pick = Label(top, text="Here are the avaiable cars for your level of experience:").grid(row=2, column=0)
        spacer_7 = Label(top, text="                                         ").grid(row=3, column=0)
        rent_time_label = Label(top, text="Enter the number of weeks you would like to rent for:").grid(row=4, column=0)
        error_rent_time = Label(top,  text = '', fg = "red")
        error_rent_time.grid(row=4, column=2)
        spacer_8 = Label(top, text="                                         ").grid(row=5, column=0)
        error_check = Label(top, text = '', fg = "red")
        error_check.grid(row=6, column=1)




        conn = sqlite3.connect('Customer_details.db')
        c = conn.cursor()
        c.execute("SELECT experience,oid FROM personal_details ORDER BY rowid DESC LIMIT 1"); #Reveres the table so that the latest entry is the first in the table
        records = c.fetchone() #Fetches first entry which is now the current users data
            
        #commit changes
        conn.commit()

        #close connection
        conn.close()
        
        rent_time = Entry(top, width = 40)
        rent_time.grid(row=4, column=1)

        #Creating presets for the drop boxes so that they can be called efficiently
        cars = [
                "Volkswagen Golf 1.0",
                "Renault Clio 2007",
                "Seat Leon 1.0",
                "Skoda Citigo 1.0",
                "Volkswagen Up 1.0 75",
                "Suzuki Baleno 1.0",
                "Seat Ibiza 1.0 TSI 95"
                ]
        cars2 = [
                "Volkswagen Golf 1.0",
                "Renault Clio 2007 1.2",
                "Seat Leon 1.0",
                "Skoda Citigo 1.0",
                "Volkswagen Up 1.0 75",
                "Suzuki Baleno 1.0",
                "Seat Ibiza 1.0 TSI 95",
                "BMW, 3 SERIES, 325i M sport",
                "Mercedes slk 3L ulez",
                "Audi Quattro 3L",
                ]
        cars3 = [
                "Volkswagen Golf 1.0",
                "Renault Clio 2007 1.2",
                "Seat Leon 1.0",
                "Skoda Citigo 1.0",
                "Volkswagen Up 1.0 75",
                "Suzuki Baleno 1.0",
                "Seat Ibiza 1.0 TSI 95",
                "BMW, 3 SERIES, 325i M sport",
                "Mercedes slk 3L ulez",
                "Audi Quattro 3L",
                "Honda CR-V",
                "Subaru Forester",
                "Volkswagen Tiguan",
                "Land Rover Discovery Sport"
                ]
        cars4 = [
                "Volkswagen Golf 1.0",
                "Renault Clio 2007 1.2",
                "Seat Leon 1.0",
                "Skoda Citigo 1.0",
                "Volkswagen Up 1.0 75",
                "Suzuki Baleno 1.0",
                "Seat Ibiza 1.0 TSI 95",
                "BMW, 3 SERIES, 325i M sport",
                "Mercedes slk 3L ulez",
                "Audi Quattro 3L",
                "Honda CR-V",
                "Subaru Forester",
                "Volkswagen Tiguan",
                "Land Rover Discovery Sport",
                "Mercedes GL 2021",
                "2022 Range Rover Velar, Luxury SUV",
                "Land roverDiscovery large family SUV",
                "Ferrari Roma",
                "Ferrari 488",
                "Ferrari 812",
                "Ferrari F8"
                ]
        
        #creating drop down menus
        if records[0] <= 2:
                dropdown = ttk.Combobox(top, value = cars, width = 40)
                dropdown.grid(row=2, column=1)
        elif records[0] <= 5 and records[0] > 2:
                dropdown = ttk.Combobox(top, value = cars2, width = 40)
                dropdown.grid(row=2, column=1)
        elif records[0] > 5 and records[0] <=10:
                dropdown = ttk.Combobox(top, value = cars3, width = 40) 
                dropdown.grid(row=2, column=1)
        else:
                dropdown = ttk.Combobox(top, value = cars4, width = 40)
                dropdown.grid(row=2, column=1)

        #Saving rent_time to database
        def save_to_database():
                conn = sqlite3.connect('Customer_details.db')
                c = conn.cursor()

                c.execute("""CREATE TABLE IF NOT EXISTS rent_details (
                        rent_time integer,
                        car text,
                        postcode text
                        )""") #"integer" and "text" represents the data type
                        #create table if not exists checks if the table was already created and creates a new one depending on that

                #insert into table
                c.execute("INSERT INTO rent_details VALUES (:rent_time, :car, :postcode)",
                {
                        'rent_time':rent_time.get(),
                        'car':dropdown.get(),
                        'postcode':postcode.get()
                })


                #commit changes
                conn.commit()

                #close connection
                conn.close()
        
                #clears the boxes
                rent_time.delete(0, 'end')
                dropdown.delete(0, 'end')

        
        #opening third window
        def open_third():
                third = Toplevel()
                third.title("Car rentals company")
                thankyou = Label(third, text="Thankyou for using our service").grid(row=0, column=0)
                
                #closeswindows
                def terminate():
                        top.destroy()
                        third.destroy()
                
                terminate_button = Button(third, text = "Back to start", command =terminate)
                terminate_button.grid(row=1, column=0)


        #creating a form of validation for the week box
        def validation_2():
                        global check
                        check = 0
                        try:
                                int(rent_time.get()) #Checks to see if the number entered is an integer in experience box
                                error_rent_time.config(text="Valid", fg = "green")
                        except ValueError:
                                error_rent_time.config(text="Please enter only numbers in the format given", fg = "red")
                                check = check + 1
                        
                        if check > 0:
                                error_check.config(text="Please make corrections before continuing", fg = "red")
                        else:
                                error_message.config(text='')
                                save_to_database()
                                open_third()
                                

        button_3 = Button(top, text="Submit", command =validation_2)
        button_3.grid(row=6, column=0)
                




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
                open() #To allow for multiple funtions to occur at once when button is clicked

            


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
staff_btn = Button(root, text="Staff access", command=login)
staff_btn.grid(row=13, column=3, pady=10, padx=10)


#commit changes
conn.commit()

#close connection
conn.close()


root.mainloop()




























