from ch5_solution import CustomerRep
from prettytable import PrettyTable
x = PrettyTable()

class UI:
    def __init__(self):
        self.cr = CustomerRep()
        self.choices = {
            '1': self.add_customer,
            '2': self.display_customers,
            '3': self.deletion_choice,
            '4': self.update_choice,
            '5': exit
        }
    
    def run(self):
        while True:
            print('''
            1. Create Customer
            2. View Customer
            3. Delete Customer
            4. Update Customer
            5. Exit
            ''')
            self.choice = input('Choose a number:')
            action = self.choices.get(self.choice)
            if action:
                action()
            else:
                print('not a valid choice')
    
    def display_customers(self):
        
        x = PrettyTable()
        x.field_names = ['First Name', 'Last Name', 'status', 'Email', 'Message']
        
        for i in self.cr.customer_list:
           x.add_row([i.FirstName, i.LastName, i.status, i.Email, i.Type])
   
        print(x)

    
        
    
    def add_customer(self):
        firstname = input('What is the customers first name? \n >')
        lastname = input('What is the customers last name? \n >')
        status_c = (input('What type of customer? \n >'))
        email_id = input('What is the customers email address? \n >')
        self.cr.create_customer(firstname, lastname, status_c, email_id)

    def deletion_choice(self):
        deletion_choice = input('''What do you want to delete?
            firstname\n
            lastname\n
            customer status\n
            email\n >''')
        if deletion_choice == 'firstname':
            firstname = input('What first name would you like to delete? \n >')
            self.cr.delete_first_name(firstname)
        
        elif deletion_choice == 'lastname':
            lastname = (input('What last name would you like to delete? \n >'))
            self.cr.delete_last_name(lastname)
        
        elif deletion_choice == 'customer status':
            status_c = (input('What type of customer would you like to delete? \n >'))
            self.cr.delete_status(status_c)
        
        elif deletion_choice == 'email':
            email_id = input('What email would you like to delete? \n >')
            self.cr.delete_email(email_id)
        else:
            print('invalid')

    def update_choice(self):
        update_choice = input('''What do you want to update?
        firstname\n
        lastname\n
        customer status\n
        email\n > ''')
        if update_choice == 'firstname':
            firstname = input('What firstname would you like to update? \n >')
            new_first = input('What is the new firstname :')
            self.cr.update_firstname(firstname, new_first)
        if update_choice == 'lastname':
            lastname = input('What lastname would you like to update? \n >')
            new_last = input('What is the new last name :')
            self.cr.update_lastname(lastname, new_last)
        if update_choice == 'customer status':
            status = (input('What status would you like to update? \n >'))
            new_status = (input('What is the new status :'))
            self.cr.update_status(status, new_status)
        if update_choice == 'email':
            email = input('What email do you want to update? \n >')
            new_email = input('What is the new email :')
            self.cr.update_email(email, new_email)

        else:
            print('Invalid Command')
            
        
        
    
        
        





if __name__ == "__main__":
    customer_app = UI()
    customer_app.run()
