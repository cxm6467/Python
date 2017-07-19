"""
##  A basic calendar that can interact with the 
##  user by viewing, adding, deleting and
##  updating events.
##  
##  Language:  Python3
##  Author:    Chris Marasco
##  Date:	   07/13/2017
##  Modules:   sleep, sys and time
"""

## Add specific libraries from time
from time import sleep, strftime
import sys

## User's First name
USER_FIRST_NAME = "Chris"

## Dict for the Cal
calendar = {}

## Function for displaying welcome message
def welcome():
	## Welcome Message
	print("Welcome, ", USER_FIRST_NAME, ".")
		
	## Wait a second before printing date/time
	sleep(1)
	
	
	print("Today is:  "+strftime("%A %B %d, %Y"))
	print("It is now:  "+strftime("%I:%M:%S"))
	
	sleep(1)
	
	## Ask user for input
	
	print("What would you like to do, ", USER_FIRST_NAME, "?")
 
def start_calendar():
	## Welcome User
	welcome()
	
	## Only exit when the user wants to
	start = True
	
	## Use above so user can control exit
	while(start):
		user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit:  ").upper()
		
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
			date = input("What date?  ")
			update = input("Enter the update:  ")
				
			#Update calendar
			calendar[date] = update
			
			#Temporary Success
			print("Successful update")
			print(calendar)
			
		## Add Info
		elif user_choice == "A":
			## Add Info
			event = input("Enter Event:  ")
			date = input("Enter Date (MM/DD/YYYY):  ")
			if len(date) > 10   or (  int(date[6:])  < int(strftime("%Y")) ):

				print("You entered an invalid date!")
						
				try_again = input("Try Again?  Y for Yes, N for No:  ").upper()
				if try_again == "Y":
					continue
				else:
					start = False
			else:
				calendar[date] = event
				print("Succesful Add!")
				print(calendar)
		
		elif user_choice == "D":
			if len(calendar.keys()) < 1:
				print("Calendar is empty, silly!")
			else:
				event = input("Enter Event:  ")
				
				for e in calendar.copy():
					if event == calendar[e]:
						del calendar[e]
						print("Successful Delete")
						print(calendar)
					else:
						print("Whoops, that's not a valid date!")
						try_again = input("Try Again?  Y for Yes, N for No:  ").upper()
						if try_again == "Y":
							continue
						else:
							start = False
		elif user_choice == "X":
			start = False

		else:
			start = False
					
start_calendar()