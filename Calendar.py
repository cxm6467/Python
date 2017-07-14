"""
##  A basic calendar that can interact with the 
##  user by viewing, adding, deleting and
##  updating events.
##  
##  Language:  Python
##  Author:    Chris Marasco
##  Date:			 07/13/2017
##  Modules:	 sleep, time
"""

## Add specific libraries from time
from time import sleep, strftime

## User's First name
USER_FIRST_NAME = "Chris"

## Dict for the Cal
calendar = []

## Function for displaying welcome message
def welcome():
	## Welcome Message
	print("Welcome, ") + USER_FIRST_NAME + "."
		
	## Wait a second before printing date/time
	sleep(1)
	
	
	print("Today is:  "+strftime("%A %B %d, %Y"))
	print("It is now:  "+strftime("%I:%M:%S"))
	
	sleep(1)
	
	## Ask user for input
	
	print("What would you like to do, "+USER_FIRST_NAME+"?")
 
def start_calendar():
	## Welcome User
	welcome()
	
	## Only exit when the user wants to
	start = True
	
	## Use above so user can control exit
	while(start):
		user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit:  ").upper()
		
		## View Calendar
		if user_choice == "V":
			## Check if calendar is empty, if so let them know, if not print it
			if len(calendar.keys()) < 1:
				print("Sorry, your calendar is empty!")
			else:
				print(calendar)

			##  update Calendar
		elif user_choice == "U":
			#Update Info
			date = raw_input("What date?  ")
			update = raw_input("Enter the update:  ")
				
			#Update calendar
			calendar[date] = update
			
			#Temporary Success
			print("Successful update")
			print(calendar)
			
		## Add Info
		elif user_choice == "A":
			## Add Info
			event = raw_input("Enter Event:  ")
			date = raw_input("Enter Date (MM/DD/YYYY):  ")
			if len(date) > 10   or (  int(date[6:])  < int(strftime("%Y")) ):

				print("You entered an invalid date!")
						
				try_again = raw_input("Try Again?  Y for Yes, N for No:  ").upper()
				if try_again == "Y":
					continue
				elif try_again == "N":
					start = False
