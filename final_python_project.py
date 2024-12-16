#write a python code to be sure an individual is eligible for loan which takes the input 5 recent transactions of the person amd outputs the
#Result.

 name = input("what is your name sir/ma? ")
 bank_name = "ENOCH MICRO-FINANCE BANK"
 print(f"Hello {name} welcome to {bank_name}")
 transaction_status = str(input("have you made 5 recent transactions 'yes' or 'no' : "))
 if transaction_status == 'yes':
  print("ok")
 elif transaction_status == 'no':
  print("ok")
  exit()
 else:
    print("invalid input. please type 'yes' or 'no' ")

 #to grant loan request we have to check for 5 recent transactios 
 #first transaction
 print("we will have to confirm your last five transactions for eligibility")
 first_place_of_transaction = input("what is the name of the place you made your first recent transaction? ")
 first_transaction_worth = int(input("what is the worth of the transaction"))
 first_percentage_paid = int(input("how many percentage was paid at first instance  "))
 print()
 print()
 #this is the second transaction
 second_place_of_transaction = input("what is the name of the place you made your second recent transaction? ")
 second_transaction_worth = int(input("what is the worth of the transaction"))
 second_percentage_paid = int(input("how many percentage was paid at first instance  "))
 print()
 print()
 #this is the third transaction
 third_place_of_transaction = input("what is the name of the place you made your third recent transaction? ")
 third_transaction_worth = int(input("what is the worth of the transaction"))
 third_percentage_paid = int(input("how many percentage was paid at first instance  "))
 print()
 print()
 #this is the fourh transaction
 fourth_place_of_transaction = input("what is the name of the place you made your fourth recent transaction? ")
 fourth_transaction_worth = int(input("what is the worth of the transaction"))
 fourth_percentage_paid = int(input("how many percentage was paid at first instance  "))
 print()
 print()
 #this is the fifth transaction
 fifth_place_of_transaction = input("what is the name of the place you made your fifth recent transaction? ")
 fifth_transaction_worth = int(input("what is the worth of the transaction"))
 fifth_percentage_paid = int(input("how many percentage was paid at first instance  "))
 print()
 print()
 amount_to_borrow = int(input("how much do you wanna borow? "))
 #add up all 5 transaction percentage and divide by 5

 final_percentage = (first_percentage_paid + second_percentage_paid + third_percentage_paid + fourth_percentage_paid + fifth_percentage_paid) / 5
 print(final_percentage)

 if amount_to_borrow >= 200000 and final_percentage > 60:
     print("you are eligible to borrow money")
     exit()
 elif amount_to_borrow >= 200000 and final_percentage < 60:
     print("you are not eligible to borrow money ")     
 else: 
 exit()

# #bank_creation
print("pls create a bank account")

first_name = input("pls enter your first name")
middle_name = input("pls enter your second name")
last_name = input("pls enter your third name")
phone_number = int(input("input your phone number"))
Nin_number = int(input("enter your Nin number"))


#persons details
print(first_name)
print(middle_name)
print(last_name)
print(phone_number)
print(Nin_number)

print("creation of bank in process")
print("........")
print("........")
print("........")
print("bank successfully created")

#created by enoch
