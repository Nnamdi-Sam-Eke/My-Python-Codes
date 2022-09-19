#A program by Urelix ®
#A prototype of the working of an ATM machine
#Insert your Atm card using the keyword insert
########################/?// Importing modules and packages?//###################################
import time
from time import sleep
import random
# function to ask play again or not'
def quit():
	print('invalid pin....')
	exit()
reply = input('Enter keyword: insert::\n')
if reply == 'insert':
	time.sleep(1.7)
	print("Please wait........")
	time.sleep(3)
	print('Welcome dear customer!\n\nEnter your pin to continue.::')
else:
	print('Sorry, you can\'t go on...')
	time.sleep(2)
	print('Exiting program...')

#Enter your Atm card pin to continue
pin = (input())
if len(pin) == 4:
	time.sleep(2)
	print('What action do you want to perform?\n1.View balance\t\t2.Withdraw\n3.Transfer Money\t4.Pay bills\n5.Buy airtime\t\t6.Change pin.')
else:
	quit("Incorrect length of pin.Check and try again.")
#Choosing what action to perform
	
action = int(input())
balance = int(720500) # The current account balance is #720,500
if action == 1:
	print('Your account balance is::#'+  str(balance ))

if action ==2:
		print('How much do you want to withdraw?')
		amount = int(input('#'))
		time.sleep(1.5)
		print	('.....This Atm will not retract cash...\nTake your cash 💵💵')
		time.sleep(2)
		print('Your new balance is:::#', int(balance) - int(amount))
		
if action ==3:
	print('Enter recipient\'s account number::')
	num = int(input())
	print('choose destination bank::\n')
	bank = input('1.Uba bank\t2.Zenith bank\n3.First bank\t4.Access bank\n5.GT bank\t6.Fidelity bank\n7.Others\n:::')
	if bank == 7:
		print('8.Heritage bank\t9.Union bank\n10.Stanbic IBTC bank\t\t')
		print('How much do you want to transfer?#')
		transfer = int(input())
		time.sleep(2)
		print('Pleàse wàit!')
		time.sleep(2)
		print('Transfer successful!\nYour new account balance is#', int(balance) - int(transfer))

if action == 4:
	bill = input('What bill do you want to pay?\n1.Cable TV\t2.Light bill\n3.Utilities\n::')
	if bill ==1:
		print('1.Dstv\t2.Gotv\n3.Startimes\t4.Mytv\n5.Others.')
	if bill ==2:
		print("1.Pre-paid\t2.Post-paid")
	if bill == 3:
		print("1.Security\t2.Water\t3.Insurance\t4.Others")
if action == 5:
	time.sleep(1.5)
	Airtime =input("What network are you recharging?\n1.Mtn\t2.Airtel\t3 Glo\t4.9 Mobile\n::::")
	if Airtime == 1:
		print("Enter the amount you want to recharge::")
		amt=int(input())
		time.sleep(0.9)
		print("......................................")
		time.sleep(1.7)
		print("Enter the phone number::")
		num = int(input())
		if num < 11:
			print("Enter a correct number")
		if num > 11:
			print("Enter a correct number")
		else: 
			print("Please wait!.......\n.........Recharge successful!")
		if Airtime == 2:
			print("Enter the amount you want to recharge::")
		amt=int(input())
		time.sleep(0.9)
		print("......................................")
		time.sleep(1.7)
		print("Enter the phone number::")
		num = int(input())
		if num < 11:
			print("Enter a correct number")
		if num > 11:
			print("Enter a correct number")
		else: 
			print("Please wait!.......\n.........Recharge successful!")
			if Airtime == 3:
				print("Enter the amount you want to recharge::")
		amt=int(input())
		time.sleep(0.9)
		print("......................................")
		time.sleep(1.7)
		print("Enter the phone number::")
		num = int(input())
		if num < 11:
			print("Enter a correct number")
		if num > 11:
			print("Enter a correct number")
		else: 
			print("Please wait!.......\n.........Recharge successful!")
			if Airtime == 4:
				print("Enter the amount you want to recharge::")
		amt=int(input())
		time.sleep(0.9)
		print("......................................")
		time.sleep(1.7)
		print("Enter the phone number::")
		num = int(input())
		if num < 11:
			print("Enter a correct number")
		if num > 11:
			print("Enter a correct number")
		else: 
			print("Please wait!.......\n.........Recharge successful!")