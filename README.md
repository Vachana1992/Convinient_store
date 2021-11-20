# Convinient_store
Smart-Mart is a convenience store that is in Toronto, Canada. The store needs an application to use it in its daily business. The application will be written by your company for the store.

USER GUIDELINES FOR THE APPLICATION

To run the python script and connect to database, you need to set up MySQL server in your system and install python environment. 

	 To use MySQL, you need first to install it. You can install it from:
https://dev.mysql.com/downloads/installer/
	After you install MySQL, you need to install MySQL connector for Python. You can download it from: https://dev.mysql.com/downloads/connector/python/


After setting up all the requirements, run the python file in your command prompt.
1. To run the python file in your command prompt, add path for the python file and press enter.

2.Type python and file name to run. For example, here the python file name is projectPartA.py.                     should write python is projectPartA.py

Doing this runs your command and opens your Python file via your computer's installed Python program.
•	When you run the file, you will get a menu driven page in which you can select which option you want.



The Application Description:
The application consists of 5 functions:
	Registering products: Each product that the system will be dealing with must be registered. The product has the following info:
1.	Product Number
2.	Product Name
3.	Product Description
4.	Product Unit Price
	Individual Billing: When a person shops in the convenient store, the user will do the following:
1.	User will input the product number and number of units
2.	Step 1 will be repeated until all products entered
3.	At the end of the billing, the bill will be generated
4.	Consider 13% tax ALWAYS
	Sales Report: At end of the day or when requested, the system will show the following:
1.	The product Names bought
2.	Number of units bought per product
3.	Total price of the product
4.	Totals of the ALL products bought in that day
	Shipping Products to the store: User will add product to the store after being shipped to the store. The information includes the following:
1.	The product’s number
2.	The product units shipped into the store
3.	The product wholesale price
4.	Product expiry date (if exist)
	Stocking Report: Another report can be generated. The report will show the products that are about to finish. The minimum number of the product that should be in store is 10. otherwise, system will put the product on order list

APPLICATION FILE DESCRIPTION 
This Project consists of one MySql schema and one python file which include tkinter application to create GUI and 5 methods to handle each operation.
•	 Main:
Imports all required modules like mysqlconnector,tkinter,messagebox etc at the beginning of the file.
It has a menu that helps to select which operation you want to proceed.
There are five options Registration, individual billing, shipping,stock report and sales report .

1.Registering_pdcts:
This will accept all product information and stored into database “smart.db” which connected to the python file
2.Individual_ billing: 
You will get a bill  when you provide the product number and number of units in this page.
3. Shipping:
4. Sales Report:
This method has sales report which is used to display the sales report of that day. When user clicks the button it will show sales report.

5. Stock report:
