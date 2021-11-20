# import tkinter module
import tkinter
import tkinter.messagebox

import mysql.connector


class MyGUI:
    def __init__(self):
        # Create the main window.
        self.bill_window = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        # Create the Canvas widget.
        self.canvas = tkinter.Canvas(self.top_frame, width=1200, height=400)

        # Display text in the center of the window.
        self.canvas.create_text(300, 10, text='BILLING SERVICE', fill='#000000')
        self.my_button = tkinter.Button(self.top_frame, text='MAIN MENU', command=self.do_something)
        self.pos = 100
        # Pack the Button.
        self.my_button.pack()
        self.my_button.place(bordermode='outside', x=10, y=10)
        # Pack the canvas.
        self.quit_button = tkinter.Button(self.top_frame, text='Quit', command=main_window.destroy)
        self.quit_button.pack()
        self.quit_button.place(bordermode='outside', x=1160, y=10)
        self.canvas.pack()
        self.canvas.create_text(870, 70, text='-----------BILL-----------')
        self.canvas.create_text(870, 85, text='Product No\t\tProduct Name\t\tQuantity\t\tUnit Price\t\tprice')
        self.canvas.create_text(870, 90,
                                text='------------------------------------------------------------------------------------------------------------------')
        self.canvas.create_text(270, 70, text='Please enter the product no: and quantity')
        self.canvas.create_text(270, 100, text='Product number')
        self.entry1 = tkinter.Entry(self.top_frame)
        self.canvas.create_window(390, 100, window=self.entry1)
        self.canvas.create_text(270, 130, text='Quantity')
        self.entry2 = tkinter.Entry(self.top_frame)
        self.canvas.create_window(390, 130, window=self.entry2)
        self.quit_button1 = tkinter.Button(self.top_frame, text='next', command=self.do_this)
        self.quit_button1.pack()
        self.quit_button1.place(bordermode='outside', x=300, y=160)
        self.quit_button2 = tkinter.Button(self.top_frame, text='final bill', command=self.do_this1)
        self.quit_button2.pack()
        self.quit_button2.place(bordermode='outside', x=300, y=190)
        self.sum = 0
        self.top_frame.pack()
        # Start the mainloop.
        tkinter.mainloop()

    def do_something(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button.')

    def do_this(self):
        self.pos += 15
        product = self.entry1.get()
        qty = self.entry2.get()
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="c0770767@vach", database="smart_mart")
        mycursor = mydb.cursor()
        sql = "INSERT INTO individual_billing VALUES(%s,%s)"
        mycursor.execute(sql, (product, qty))
        print("product added")
        mycursor.execute("""SELECT pName,pPrice FROM reg_pdcts WHERE pNo = %s""", (product,))
        record = mycursor.fetchall()
        pname = ""
        p = 0
        for x in record:
            pname = str(x[0])
            p = str(x[1])
            print(pname, p)
        mydb.commit()
        text = str(product) + "\t\t\t" + str(pname) + "\t\t\t" + str(qty) + "\t\t" + str(p) + "\t\t\t" + str(
            float(p) * int(qty))
        self.canvas.create_text(870, self.pos, text=text)
        self.sum += float(p) * int(qty)
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')

    def do_this1(self):
        self.pos += 15
        product = self.entry1.get()
        qty = self.entry2.get()
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="c0770767@vach", database="smart_mart")
        mycursor = mydb.cursor()
        sql = "INSERT INTO individual_billing VALUES(%s,%s)"
        mycursor.execute(sql, (product, qty))
        print("product added")
        mycursor.execute("""SELECT pName,pPrice FROM reg_pdcts WHERE pNo = %s""", (product,))
        record = mycursor.fetchall()
        pname = ""
        p = 0
        for x in record:
            pname = str(x[0])
            p = str(x[1])
            print(pname, p)
        mydb.commit()
        text = str(product) + "\t\t\t" + str(pname) + "\t\t\t" + str(qty) + "\t\t" + str(p) + "\t\t\t" + str(
            float(p) * int(qty))
        self.canvas.create_text(870, self.pos, text=text)
        self.sum += float(p) * int(qty)
        self.canvas.create_text(870, self.pos + 15,
                                text="------------------------------------------------------------------------------------------------------------------")
        final = "Total:\t\t\t\t\t" + str(self.sum)
        self.canvas.create_text(870, self.pos + 30, text=final)
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')


# create the main window
main_window = tkinter.Tk()


# create a function registering product to add products in the registry
# while calling this function ,from main this window will open
# this is to handle product button click
def registering_products():
    # creating a window for registering products
    register_window = tkinter.Tk()

    # provide title for this window
    register_window.title("Smart Mart Project - Product Entry")

    # creating labels and entry widget for this window
    prompt_label1 = tkinter.Label(register_window, text="Product Number:  ")
    pdct_no_entry = tkinter.Entry(register_window, width=30, borderwidth=5)

    prompt_label2 = tkinter.Label(register_window, text='Product Name: ')
    pdct_name_entry = tkinter.Entry(register_window, width=30, borderwidth=5)

    prompt_label3 = tkinter.Label(register_window, text='Product Description: ')
    pdct_desc_entry = tkinter.Entry(register_window, width=30, borderwidth=5)

    prompt_label4 = tkinter.Label(register_window, text='Unit Price: ')
    pdct_price_entry = tkinter.Entry(register_window, width=30, borderwidth=5)



    # organizing labels and entry widgets by using grid method
    prompt_label1.grid(row=2, column=5)
    pdct_no_entry.grid(row=2, column=7)

    prompt_label2.grid(row=6, column=5)
    pdct_name_entry.grid(row=6, column=7)

    prompt_label3.grid(row=8, column=5)
    pdct_desc_entry.grid(row=8, column=7)

    prompt_label4.grid(row=10, column=5)
    pdct_price_entry.grid(row=10, column=7)



    # creating and organizing button to submit the details
    productentrybutton = tkinter.Button(register_window, text="Submit", borderwidth=5, width=5,
                                        command=lambda: submit1(pdct_no_entry, pdct_name_entry, pdct_desc_entry,
                                                                pdct_price_entry))
    productentrybutton.grid(row=14, column=6)

    # creating and organizing close button
    productclosebutton = tkinter.Button(register_window, text="Close", borderwidth=5, width=5,
                                        command=lambda: close_window(register_window))
    productclosebutton.grid(row=14, column=7)

    # closing the currrent window
    register_window.mainloop();


# create a function individual billing to bill the product
# while calling this function  from main, this window will open
# function to handle billing button click


def individual_billing():
    mybill = MyGUI()


# function to handle Shipping button click
def shipping():
    # creating main window
    shipping_window = tkinter.Tk()
    shipping_window.title("Smart Mart Project - Shipping Products")

    # creating user entry fields
    prompt_label1 = tkinter.Label(shipping_window, text="Product Number: ")
    pdct_no_entry = tkinter.Entry(shipping_window, width=30, borderwidth=5)

    prompt_label2 = tkinter.Label(shipping_window, text="Number of units shipped into the store: ")
    shipped_entry = tkinter.Entry(shipping_window, width=30, borderwidth=5)

    prompt_label3 = tkinter.Label(shipping_window, text="Wholesale Price: ")
    price_entry = tkinter.Entry(shipping_window, width=30, borderwidth=5)

    prompt_label4 = tkinter.Label(shipping_window, text="Expiry Date(If any): ")
    date_entry = tkinter.Entry(shipping_window, width=30, borderwidth=5)

    # setting the positions of the fileds in window
    prompt_label1.grid(row=2, column=5)
    pdct_no_entry.grid(row=2, column=7)

    prompt_label2.grid(row=4, column=5)
    shipped_entry.grid(row=4, column=7)

    prompt_label3.grid(row=6, column=5)
    price_entry.grid(row=6, column=7)

    prompt_label4.grid(row=7, column=5)
    date_entry.grid(row=7, column=7)

    # functions to execute while clicking submit and close buttons
    productshippingbutton = tkinter.Button(shipping_window, text="Submit", borderwidth=5, width=5,
                                           command=lambda: submit_shipping(pdct_no_entry, shipped_entry, price_entry,
                                                                           date_entry))
    productshippingbutton.grid(row=14, column=6)

    shippingclosebutton = tkinter.Button(shipping_window, text="Close", borderwidth=5, width=5,
                                         command=lambda: close_window(shipping_window))
    shippingclosebutton.grid(row=14, column=12)

    shipping_window.mainloop()


# function to submit the shipping details
def submit_shipping(pdct_no_entry, shipped_entry, price_entry, date_entry):
    # getting details from user
    pdct_no = pdct_no_entry.get()
    shipping_no = shipped_entry.get()
    price = price_entry.get()
    shippingdate = date_entry.get()

    # putting default values if field is empty
    if pdct_no == "":
        pdct_no = 0
    if shipping_no == "":
        shipping_no = 0
    if price == "":
        price = 0
    else:
        price = float(price)
    if shippingdate == "":
        shippingdate = "12/12/12"

    # connecting to the database
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="c0770767@vach", database="smart_mart")
    # starting cursor
    mycursor = mydb.cursor()
    # setting sql query to pass through function
    sql = "INSERT INTO shipping VALUES(%s,%s,%s,%s)"
    mycursor.execute(sql, (pdct_no, shipping_no, price, shippingdate))
    print("product added")
    mycursor.execute("SELECT * FROM shipping")

    print_cursor(mycursor, "Showing 'shipping' table records:")
    mydb.commit()
    # resetting the data
    pdct_no_entry.delete(0, "end")
    shipped_entry.delete(0, "end")
    price_entry.delete(0, "end")
    date_entry.delete(0, "end")


    # function to handle sales report button


def sales_report():
    # Create the main window.
    sales_window = tkinter.Tk()
    top_frame = tkinter.Frame()
    # Create the Canvas widget.
    # canvas = tkinter.Canvas(top_frame, width=600, height=400)
    canvas = tkinter.Canvas(top_frame, width=1600, height=400)
    # Display text in the center of the window.
    canvas.create_text(300, 10, text='Sales Report ', fill='#000000')
    # Pack the canvas.
    quit_button = tkinter.Button(top_frame, text='Quit', command=quit)
    quit_button.pack()
    quit_button.place(bordermode='outside', x=560, y=10)
    canvas.pack()
    canvas.create_text(270, 70, text='-----------SALES REPORT-----------')
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="c0770767@vach", database="smart_mart")
    mycursor = mydb.cursor()
    mycursor.execute(
        "select reg_pdcts.pNo, reg_pdcts.pName, reg_pdcts.pDesc, sum(individual_billing.noUnits) from individual_billing inner join reg_pdcts on individual_billing.pNo=reg_pdcts.pNo group by individual_billing.pNo")
    record = mycursor.fetchall()
    num = 115
    canvas.create_text(270, num, text='Product No\tProduct Name\tDescription\tQuantity')
    canvas.create_text(270, num + 5,
                       text='-----------------------------------------------------------------------------------')
    for x in record:
        num += 15
        txt = str(x[0]) + "\t\t" + str(x[1]) + "\t\t" + str(x[2]) + "\t\t" + str(x[3])
        print(txt)
        canvas.create_text(270, num, text=txt)
    top_frame.pack()
    # Start the mainloop.
    sales_window.mainloop()


# function to handle Stock button click
def stock_report():
    stock_window = tkinter.Tk()
    stock_window.title("Smart Mart Project - Stock Report")
    top_frame = tkinter.Frame()
    # Create the Canvas widget.
    # canvas = tkinter.Canvas(top_frame, width=600, height=400)
    canvas = tkinter.Canvas(top_frame, width=600, height=400)
    # Display text in the center of the window.
    canvas.create_text(300, 10, text='Stock Report ', fill='#000000')
    # Pack the canvas.
    quit_button = tkinter.Button(top_frame, text='Quit', command=main_window.destroy)
    quit_button.pack()
    quit_button.place(bordermode='outside', x=560, y=10)
    canvas.pack()
    canvas.create_text(270, 70, text='-----------STOCK REPORT-----------')
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="c0770767@vach", database="smart_mart")
    mycursor = mydb.cursor()
    mycursor.execute("select * from shipping")
    record = mycursor.fetchall()
    num = 115
    canvas.create_text(270, num, text='Product No\tUnits\tQuantity')
    canvas.create_text(270, num + 5,
                       text='-----------------------------------------------------------------------------------')
    for x in record:
        num += 15
        txt = str(x[0]) + "\t\t" + str(x[1]) + "\t\t" + str(x[2])
        print(txt)
        canvas.create_text(270, num, text=txt)
    top_frame.pack()
    # Start the mainloop.
    stock_window.mainloop()


# function to quit from the application
# to destroy the main window
def quit():
    main_window.destroy();


# function to close the window
def close_window(self):
    self.destroy()




#function to print all the product deatils entered into the database retrieve and print in the prompt
def print_cursor(mycursor, msg):
    print()
    print(msg)

    for x in mycursor:
        print(x)

#create the function submit1 which have product deatils as its parameters
def submit1(pdct_no_entry, pdct_name_entry, pdct_desc_entry, pdct_price_entry):
    #get the product details in corresponding variables
    pdct_no = int(pdct_no_entry.get())
    pdct_name = pdct_name_entry.get()
    pdct_desc = pdct_desc_entry.get()
    pdct_price = float(pdct_price_entry.get())

    # putting default values if field is empty
    if pdct_no == "":
        pdct_no = 0
    if pdct_name == "":
        pdct_name = "nil"
    if pdct_desc == "":
        pdct_desc = "nil"
    if pdct_price == "":
        pdct_price = 0
    else:
        pdct_price = float(pdct_price)



    #connect to the mysql database by giving username and password
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="c0770767@vach", database="smart_mart")
    mycursor = mydb.cursor()
    #inmsert values into the database using query
    sql = "INSERT INTO reg_pdcts VALUES(%s,%s,%s,%s)"
    #each product value added into the database
    mycursor.execute(sql, (pdct_no, pdct_name, pdct_desc, pdct_price))
    #print a message to show product added into the database
    print("product added")
    #a message box will pop up when product successfully added to the database
    tkinter.messagebox.showinfo('Registering Products', "product added successfully")
    #show all the registered products in the console
    mycursor.execute("SELECT * FROM reg_pdcts")
    #function call for showing all the product details entered in the prompt
    print_cursor(mycursor, "Showing 'reg_pdcts' table records:")
    #commit the changes
    mydb.commit()
    # after enter a product into the database clear all the fields
    pdct_no_entry.delete(0, "end")
    pdct_name_entry.delete(0, "end")
    pdct_desc_entry.delete(0, "end")
    pdct_price_entry.delete(0, "end")


# title for main window
main_window.title("Smart Mart Project")

# title for the first front page which includes button only
labeltitle = tkinter.Label(main_window, text="Smart-Mart Convenient Store ", fg="red", bg="yellow", font=("Arial", 22))
labeltitle.place(x=300, y=80)

# button for each function
# organizing each button widget by using place method
product_button = tkinter.Button(main_window, text="Register Products", width=40, borderwidth=5,
                                command=registering_products)
product_button.place(x=300, y=150)

billing_button = tkinter.Button(main_window, text="Individual Billing", width=40, borderwidth=5,
                                command=individual_billing)
billing_button.place(x=300, y=200)

shipping_button = tkinter.Button(main_window, text="Shipping Products", width=40, borderwidth=5, command=shipping)
shipping_button.place(x=300, y=250)

sales_button = tkinter.Button(main_window, text="Sales Reports", width=40, borderwidth=5, command=sales_report)
sales_button.place(x=300, y=300)

stock_button = tkinter.Button(main_window, text="Stock Report", width=40, borderwidth=5, command=stock_report)
stock_button.place(x=300, y=350)

exit_button = tkinter.Button(main_window, text="Exit", width=40, borderwidth=5, command=quit)
exit_button.place(x=300, y=400)

main_window.mainloop()
