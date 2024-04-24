def validate_iban(iban ):
    if len(iban) != 5:
        return False
    if iban[:2 ]!= "TB":
        return False
    if not iban[2:].isdigit():
        return False
    
    return True
       
        
def validate_name(name, surname):
   if  name.isalpha() and surname.isalpha():
    return True
   else:
    return False

def check_for_iban(iban, database):
   
   for iban in database.values():
      if iban == database(iban):
         return False
   return True