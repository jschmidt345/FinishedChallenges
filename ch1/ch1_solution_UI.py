from ch1_solution import MenuRepository
from prettytable import PrettyTable



class Menu_ui:
    def __init__(self):
        self.mr = MenuRepository()
        self.choices = {
            '1': self.build_item,
            '2': self.remove_item_from_list,
            '3': self.view_list,
            '4': exit }   
        
    def run(self):
        while True: 
            print('''
            1. Create Food
            2. Delete Food
            3. View Food
            ''') 
            self.choice = input('Choose a number:')
            action = self.choices.get(self.choice)
            if action:
                action()
            else:
                print( 'not a valid choice')


    

    def build_item(self):
        mn = input("What num is this on the menu? \n >")
        mname = input('What name? \n >')
        description = input('What is the description? \n >')
        ingredients = input('What are the ingredients? \n >')
        price = input('What is the price? \n > ')
        self.mr.add_item(mn,mname, description, ingredients, price )
        print('Your item has been added')
    
    def remove_item_from_list(self):
        input_id = input('What is the meal number? \n >')
        self.mr.remove_item(input_id)
    
    def view_list(self):
        x = PrettyTable()
        x.field_names = ['Meal Number', 'Meal Name', 'Description', 'Ingredients', 'Price']

        for i in self.mr.list_of_items:
            x.add_row([i.meal_number, i.meal_name, i.description, i.ingredients, i.price])
        print(x)






    
if __name__ == '__main__':
    menu = Menu_ui()
    menu.run()