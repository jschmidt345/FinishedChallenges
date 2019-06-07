from ch2_solution import ClaimRepository 
import datetime
from prettytable import PrettyTable

class Claim_Manager:
    def __init__(self):
        self.cr = ClaimRepository()
        self.choices = {
            '1': self.view_claim,
            '2': self.enter_new_claim,
            '3': self.remove_claim,
            '4': exit
            
        }
    

    def run(self):
        while True:
            print('''
            1. view claim
            2. enter new claim
            3. remove claim
            4. exit
            ''')
            self.choice = input('Choose a number:')
            action = self.choices.get(self.choice)
            if action:
                action()
            else:
                print('not a valid choice')
    
    def view_claim(self):
        x = PrettyTable()
        x.field_names = ['Claim ID', 'Claim Type', 'Claim Description', 'Claim Amount', 'Date of Incident', 'Date of Claim', 'Validity']
        for i in self.cr.claim_list:
            x.add_row([i.ClaimID, i.ClaimType, i.Description, i.ClaimAmount, i.DateOfIncident, i.DateOfClaim, i.IsValid])
        
        print(x)
    

    def enter_new_claim(self):
        c_id = input('What is the ID of this claim? \n >')
        c_type = input('What type of Claim? \n >')
        description = input('Describe the claim? \n >')
        c_amount = input('How much is this claim? \n >$')
        year = int(input('What year did it occur? \n >'))    
        month = int(input('What month did it occur? \n >'))
        day = int(input('What day did it occur? \n >'))
        self.cr.add_claim(c_id, c_type, description, c_amount , year, month, day)

    def remove_claim(self):
        claim_id = int(input('What is the claim ID? \n >'))
        self.cr.finish_claim(claim_id)
    
        
    






if __name__ == '__main__':
    manager = Claim_Manager()
    manager.run()