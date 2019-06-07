# 3 groups of customers: past, present, future
# present = send thank you
# past = come back
# future = offer deals
from prettytable import PrettyTable

class Customer:
    def __init__(self, FirstName, LastName,status, Email):
        self.FirstName = FirstName
        self.LastName = LastName
        self.status = status
        self.Email = Email
        
        if self.status == 'current':
            self.Type = "Thank you for your work with us. We appreciate your loyalty. Heres a coupon."
        elif self.status == 'potential':
            self.Type = "We currently have the lowest rates on Helicopter Insurance!"
        else:
            self.Type = "It's been a long time since we've heard from you, we want you back"
        
    def __repr__(self):
        return f'{self.FirstName} {self.LastName} {self.status} {self.Email} {self.Type}'

        
        
    
    
        
        


class CustomerRep:
    def __init__(self):
        self.customer_list = []
        self.new_character = ''
    
    

    def create_customer(self, FirstName, LastName, status, Email):
        new_customer = Customer(FirstName, LastName, status, Email)
        self.customer_list.append(new_customer)   

    
    def read_customer(self):
        return self.customer_list
        
    def delete_first_name(self, FirstName):
        FirstName_to_remove = self._delete_first(FirstName)
        if FirstName_to_remove:
            f_loc = self.customer_list.index(FirstName_to_remove)
            self.customer_list[f_loc].FirstName = ""
            return True
        else: 
            return self.customer_list
        
    def _delete_first(self, FirstName):
        for i in self.customer_list:
            if i.FirstName == FirstName:
                return i
            else:
                None

    def delete_last_name(self, LastName):
        LastName_to_remove = self._delete_last(LastName)
        if LastName_to_remove:
            l_loc = self.customer_list.index(LastName_to_remove)
            self.customer_list[l_loc].LastName = ""
            return True
        else: 
            return self.customer_list
    
    def _delete_last(self, LastName):
        for i in self.customer_list:
            if i.LastName == LastName:
                return i
            else:
                None
    
    def delete_status(self, status):
        status_to_remove = self._delete_status(status)
        if status_to_remove:
            s_loc = self.customer_list.index(status_to_remove)
            self.customer_list[s_loc].status = ""
            return True
        else: 
            return self.customer_list

    def _delete_status(self, status):
        for i in self.customer_list:
            if i.status == status:
                return i
            else:
                None
    
    def delete_email(self, Email):
        email_to_remove = self._delete_email(Email)
        if email_to_remove:
            e_loc = self.customer_list.index(email_to_remove)
            self.customer_list[e_loc].Email = ""
            return True
        else: 
            return self.customer_list
    
    def _delete_email(self, Email):
        for i in self.customer_list:
            if i.Email == Email:
                return i
            else:
                None

    

    def update_firstname(self, FirstName, new_character):
        firstname_to_update = self._update_firstname(FirstName, new_character)
        if firstname_to_update:
            f_loc = self.customer_list.index(firstname_to_update)
            self.customer_list[f_loc].FirstName = new_character
            
            return True
        else: 
            return self.customer_list

    def _update_firstname(self, FirstName, new_character):
        for i in self.customer_list:
            if i.FirstName == FirstName:
                return i
            else:
                None

    def update_lastname(self, LastName, new_character):
        lastname_to_update = self._update_last_name(LastName, new_character)
        if lastname_to_update:
            l_loc = self.customer_list.index(lastname_to_update)
            self.customer_list[l_loc].LastName = new_character
            
            return True
        else: 
            return self.customer_list

    def _update_last_name(self, LastName, new_character):
        for i in self.customer_list:
            if i.LastName == LastName:
                return i
            else:
                None
    
    def _update_status(self, status, new_character):
        for i in self.customer_list:
            if i.status == status:
                return i
            else:
                None
    
    def update_status(self, status, new_character):
        status_to_update = self._update_status(status, new_character)
        if status_to_update:
            s_loc = self.customer_list.index(status_to_update)
            self.customer_list[s_loc].status = new_character

    def _update_email(self, email, new_character):
        for i in self.customer_list:
            if i.email == email:
                return i
            else:
                None
    
    def update_email(self, email, new_character):
        email_to_update = self._update_email(email, new_character)
        if email_to_update:
            e_loc = self.customer_list.index(email_to_update)
            self.customer_list[e_loc].email = new_character
    
    



    



    
            
            
            
            

    
