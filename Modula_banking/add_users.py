def add_user(name, surname, iban, database,):
        database[name, surname] = {"iban": iban, "balance": 0} 
        print("test")
        return database
   
