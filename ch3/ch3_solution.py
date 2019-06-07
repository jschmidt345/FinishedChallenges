# need a list of all outings, cost of all outings, total cost of all outings
# Events : golf, bowling, amusment park, concert
# Aspects : # of attendees, date, total cost per person, total cost of event
# display of all the outings
# add individual outings
# calculations:
#   display combined cost of all outings
#   display of outing costs by type 

#display all outings : event date, event cost, head count of attendee, cost per person
# 1 12-1-19 -> Bowling -> 1000.00 -> 50 -> 20 
# outing add view : 
# see cost of outings : 

#cost per outing:
# cost by type, or total cost
# conditional : list all events that matched 
# tuple input format
# use count 

class Content:
    def __init__(self, event_type, num_attendees, cost, month, day, year):
        self.event_type = event_type
        self.num_attendees = num_attendees
        self.cost = cost
        self.month = month
        self.day = day
        self.year = year
        
        
    def __repr__(self):
        return f'''
    Event                   # of Attendees         Cost            Date
    {self.event_type}                       {self.num_attendees}                ${self.cost}            {self.month}/{self.day}/{self.year}
        '''

class Content_Data:
    def __init__(self):
        self.event_list = []
    
    def show_list(self):
        return(self.event_list)
    
    def add_event(self, event_type, num_attendees, cost, month, day, year):
        new_event = Content(event_type, num_attendees, cost, month, day, year)
        self.event_list.append(new_event)
    
    def __repr__(self):
        return f'cost : {self.event_list}'
    
    def get_event_cost(self, event_type):
        total = 0
        for i in self.event_list:
            if i.event_type == event_type:
                total += i.cost
        return total
    
    def get_total_cost(self):
        total_cost = 0
        for i in self.event_list:
            total_cost += i.cost
        return total_cost

    
    def get_cost_per_person(self, event_type):
        total_cost = 0
        total_head_count = 0
        for i in self.event_list:
            if i.event_type == event_type:
                total_cost += i.cost
                total_head_count += i.num_attendees
        return total_cost / total_head_count
    
    







#event type like accident type 
#display total cost
#display cost per outing
#for i in event_list:
   #if i[1] == 'golf':
        #total += i[0]
#"i.event_type = golf"

# from pretty table import PrettyTable
#events = [('Justin team', 'win', 'all of them'),('jacob team', 'loss', '5 points')]
#x.field_names = ['team', 'outcome', 'total points']
#for i in events:
#    x.add_row(list(i))
#x  = PrettyTable()
# x.field_names('Team', 'Outcome', 'Total Points')
