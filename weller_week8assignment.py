#Brianna Weller - CIS245 Week 8 Assignment 8.1
#Bank account program with classes and functions for checking and savings accounts and their associated functions.

class BankAccount:
	# Base bank account class with attributes account number and balance. Includes base bank account functions.

	def __init__(self, accountNumber, balance):
		self.accountNumber = accountNumber
		self.balance = balance

	def getBalance(self):
		print(f'\n\tAccount Balance: ${self.balance:.2f}\n')

		if self.balance < 0:
			print(f'\n!!ATTENTION!! Your account is overdrawn!\n')

	def withdrawl(self, debit):
		self.balance = self.balance - debit
		print('Account Balance After Withdrawl:')
		self.getBalance()

	def deposit(self, credit):
		self.balance = self.balance + credit
		print('Account Balance After Deposit:')
		self.getBalance()

# Inheriting Classes
class CheckingAccount(BankAccount):
	# Checking Account child class, includes additional attributes and functions for fees and minimum balance.

	def __init__(self, accountNumber, balance, fees, minimumBalance):
		super().__init__(accountNumber, balance)
		self.fees = fees
		self.minimumBalance = minimumBalance

	def checkMinimumBalance(self):
		if self.balance < self.minimumBalance:
			print(f'\n!!WARNING!! Your account balance of ${self.balance:.2f} is below the minimum balance!\n')

		else:
			print(f'\n')

	def deductFees(self):
		self.balance = self.balance - self.fees
		print('Account Balance After Fees Deducted:')
		self.getBalance()
		self.checkMinimumBalance()

	def display(self):
		print(f'\n\tAccount Number: {self.accountNumber}\n\tBalance: ${self.balance:.2f}\n\tFees: ${self.fees:.2f}\n\tMinimum Balance: ${self.minimumBalance:.2f}')
		self.checkMinimumBalance()

class SavingsAccount(BankAccount):
	# Savings Account child class, includes additional attribute and function for interest rate.

	def __init__(self, accountNumber, balance, interestRate):
		super().__init__(accountNumber, balance)
		self.interestRate = interestRate

	def addInterest(self):
		self.balance = self.balance * ((self.interestRate / 100) + 1)
		print('Account Balance After Interest Added:')
		self.getBalance()

	def display(self):
		print(f'\n\tAccount Number: {self.accountNumber}\n\tBalance: ${self.balance:.2f}\n\tInterest Rate: {self.interestRate:.1f}%\n')


def lineSep():   # Function for line separation to format program display
	print('-------------------------------\n')

# Create savings account and checking account
account_1 = SavingsAccount('1234', 100, 2)
account_2 = CheckingAccount('5678', 25, 5, 50)

# Main function		
if __name__ == '__main__':
	active = True
	while active:
		# Prompt user to select an option to review their account or conduct a transaction
		print('Select one of the options below to proceed\n\t1) Review Savings Account Details\n\t2) Review Checking Account Details\n\t3) Make a Deposit\n\t4) Make a Withdrawl\n\t5) Deduct Fees or Add Interest\n\tEnter "q" to quit')
		value = (input('\nInput: '))

		if value == 'q':
			active = False

		elif value == '1':
			print('Savings Account Details:')
			account_1.display()

		elif value == '2':
			print('Checking Account Details:')
			account_2.display()

		elif value == '3':
			# Prompt user for deposit amount and to identify which account to deposit to.

			try:
				credit = (input('Enter amount of deposit: $'))
				credit = float(credit)

				creditToAcct = (input('Which account would you like to deposit to?\n\t1) Savings Account\n\t2) Checking Account\nInput: '))
				creditToAcct = int(creditToAcct)

			except ValueError:
 				print("Sorry, the option you selected is not recognized. Please enter a valid option.")

			else:
				if creditToAcct == 1:
					account_1.deposit(credit)

				elif creditToAcct == 2:
					account_2.deposit(credit)
					account_2.checkMinimumBalance()

				else:
					print("\nSorry, the option you selected is not recognized. Please enter a valid option.\n")

		elif value == '4':
			# Prompt user for withdrawl amount and to identify which account to withdraw funds from.

			try:
				debit = (input('Enter amount of withdrawl: $'))
				debit = float(debit)

				debitToAcct = (input('Which account would you like to make a withdrawl from?\n\t1) Savings Account\n\t2) Checking Account\nInput: '))
				debitToAcct = int(debitToAcct)

			except ValueError:
 				print("Sorry, the option you selected is not recognized. Please enter a valid option.")

			else:
				if debitToAcct == 1:
					account_1.withdrawl(debit)

				elif debitToAcct == 2:
					account_2.withdrawl(debit)
					account_2.checkMinimumBalance()
				else:
					print("\nSorry, the option you selected is not recognized. Please enter a valid option.\n")

		elif value == '5':
			# Prompt user to select account & associated transaction.

			adminAcct = (input('Which account would you like to update?\n\t1) Savings Account - Add Interest\n\t2) Checking Account - Deduct Fees\nInput: '))

			if adminAcct == '1':
				account_1.addInterest()

			elif adminAcct == '2':
				account_2.deductFees()

			else:
				print("\nSorry, the option you selected is not recognized. Please enter a valid option.\n")

		else:
			print("\nSorry, the option you selected is not recognized. Please enter a valid option.\n")

		lineSep()
