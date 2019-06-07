# create a menu item
# delete a menu item
# print a list of all item on the menu
# Menu class with constructos and instance attributes
# MenuRepository class that has methods needed
# Create a test class
# Create a UI file that allows the restuarant manager to add, delete and print.





class Menu:
    def __init__(self, meal_number, meal_name, description, ingredients, price):
        self.meal_number = meal_number
        self.meal_name = meal_name
        self.description = description
        self.ingredients = ingredients
        self.price = price
    def __repr__(self):
        return f'{self.meal_number}.{self.meal_name}\n{self.description}\nIngredients:{self.ingredients}\nPrice: {self.price} dollars'

class MenuRepository:
    def __init__(self):
        self.list_of_items = []

    def add_item(self,meal_number, meal_name, description, ingredients, price):
        self.list_of_items.append(Menu(meal_number, meal_name, description, ingredients, price))
    
    def remove_item(self, meal_number):
        item_to_remove = self._check_for_number(meal_number)
        if item_to_remove:
            self.list_of_items.remove(meal_number)
            return True
        else:
            return False

    def _check_for_number(self, meal_number):
        for i in self.list_of_items:
            if i.meal_number == meal_number:
                return i 
        return None
        
        
    
    def show_list(self):
        print(self.list_of_items)
    
    def __repr__(self):
        return f'{self.list_of_items}'

#class Test:
    #burger = Menu(1,'Hamburger','royal with cheese',['ground beef','cheese','lettuce','tomato'],10)
    #food_list = MenuRepository()
    #food_list.add_item(burger)
    #food_list.show_list()
    #food_list.remove_item(burger)


