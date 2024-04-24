from validator import validate_iban
from validator import validate_name
from add_users import add_user
from top_up_balance import topup_balance
#from transactions import transfer_to
from validator import check_for_iban

def main():
    
    database = {} 
    name = input("Enter your name: ").lower()
    surname = input("Enter your surname: ").lower()
    iban = input("Enter your bank account number (format TB001): ")

    if not validate_name(name, surname):
        print("Invalid name or surname. Please enter only alphabetic characters.")
        return

    if not validate_iban(iban):
        print("Invalid account number format. Please use format TB001.")
        return

      
    if iban in database and database[iban]["iban"] == iban:
        print("User already exists in the dictionary with the same account number.")
    else:
        add_user(name, surname, iban, database, )
        print("User information added to the database.")
            
    print(database)
    balance = input("Would you like to top up your balance? (yes/no): ").lower()
    if balance == "yes":
        money = float(input("Enter the amount to top up: "))
        topup_balance(name, surname, iban, money, database)
        print (database)
    
    transfer = input("Would you like to transfer money to another user? (yes/no): ").lower()
    if transfer == "yes":
        receiver_name = input("Enter receiver's name: ").lower()
        receiver_surname = input("Enter receiver's surname: ").lower()
        receiver_iban = input("Please enter receiver's' Iban: ")
        
        #if check_for_iban(receiver_iban, database):
            #print("User already exists in the database with the same account number.")
            
        
        add_user(receiver_name, receiver_surname, receiver_iban, database,)
        print("User information added to the database.")
        
        
        #print (database)
        #sender = database (name, surname)['iban']
        #transfer_amount = float(input("Please enter how much you want to transfer: "))
        #transfer_to(sender,receiver_iban, transfer_amount, database)
            
        
        
        print(database)
if __name__ == "__main__":
    main()

