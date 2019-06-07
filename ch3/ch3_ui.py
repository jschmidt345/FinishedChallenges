from ch3_solution import Content_Data
from prettytable import PrettyTable

class AccountingOptions:
    def __init__(self):
        self.ac = Content_Data()
        self.choices = {
            '1': self.display_list_of_outings,
            '2': self.create_event,
            '3': self.event_cost,
            '4': self.total_cost,
            '5': self.cost_p_person,
            '6': exit
        
        }

    def run(self):
        while True:
            print('''
            1. Display events
            2. Create event
            3. Get cost of a specific event
            4. Get total cost
            5. Get cost per person
            6. Exit
            ''')
            self.choice = input('Choose a number:')
            action = self.choices.get(self.choice)
            if action:
                action()
            else:
                print('not a valid choice')

    def display_list_of_outings(self):
        x = PrettyTable()
        x.field_names = ['Type of Event','Attendance', 'Cost', 'Month', 'Day', 'Year']
        for i in self.ac.event_list:
            x.add_row([i.event_type, i.num_attendees, i.cost, i.month, i.day, i.year])
            print(x)
    
    def create_event(self):
        type_of_event = input('''
        What is the event type? \n
        Choices: 
        -Golf
        -Bowling
        -Amusement Park
        -Concert
        ''')
        attendance = int(input('How many people attended the event?\n >'))
        cost_of_event = int(input('How much did the event cost?\n >'))
        year = (input('What year did it take place?\n >'))
        month = (input('What month did it take place?\n >'))
        day = (input('What day did it take place?\n >'))
        self.ac.add_event(type_of_event, attendance, cost_of_event, month, day, year)
    
    def event_cost(self):
        desired_event_cost = input('''
        What event do you want to know the cost for?\n 
        Choices: 
        -Golf
        -Bowling
        -Amusement Park
        -Concert
        ''')
        print(self.ac.get_event_cost(desired_event_cost))
    
    
    def total_cost(self):
        print(self.ac.get_total_cost())

    def cost_p_person(self):
        desired_event = input('''
        What event do you want to know the cost for?\n 
        Choices: 
        -Golf
        -Bowling
        -Amusement Park
        -Concert
        ''')
        print(self.ac.get_cost_per_person(desired_event))

        

if __name__ == '__main__':
    accounting = AccountingOptions()
    accounting.run()
