#Nike inventory management program

from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        pass
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        pass
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        pass
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        pass
        
        '''
        Add a code to returns a string representation of a class.
        '''
        print(f'''
Country                  {self.country}
Product                  {self.product}
Code                     {self.code}
Cost                     {self.cost}
Quantity                 {self.quantity}
Value                    {(int(self.quantity)*float(self.cost)):.2f}''')

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
my_shoes = []
#==========Functions outside the class==============
def read_shoes_data():
    pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

    try:
        with open("inventory.txt","r") as stock_file:
            row = stock_file.readlines()[1:]                               #skipping the header row
            for item in row:
                item = item.strip()
                item = item.split(",")
                my_shoes.append(item)                            #this list is used to tabulate.
                #Creating an instance of a shoe:
                shoe_object = Shoe(item[0], item[1], item[2], item[3],item[4]) 
                shoe_list.append(shoe_object)                              #Appending the shoe instance
    except FileNotFoundError:
        print("File does not exist.")  
                  
def capture_shoes():
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    
    print("\n----CAPTURE SHOE----\n")
    Country = input("Country : ") 
    Code = input("Code : ") 
    Product = input("Product : ") 
    Cost = input("Cost : ") 
    Quantity = input("Quantity : ")
     
    shoe_object = Shoe(Country, Code, Product, Cost, Quantity)
    shoe_list.append(shoe_object)                               #list with Shoe instances
    my_shoes.append([Country, Code, Product,Cost,Quantity])     #list with strings
    print("\n----SHOE CAPTURED----\n")  
       
def view_all():
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    Headers = ["Country","Code","Product","Cost", "Quantity"]
    print(tabulate(my_shoes,headers = Headers))

def re_stock():
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    shoe_quantity = []
    for item in shoe_list:
        shoe_quantity.append(int(item.quantity))        #adding all quantities to a list
    item = shoe_quantity.index(min(shoe_quantity))      #the position of the lowest quantity shoe
    print(f"Product {shoe_list[item].code} - {shoe_list[item].product} has low quantites.")
    
    restock = input("Restock? [Yes/No] \n").lower()
    if restock == "yes":
        Quantity = input("Quantity : ")
        shoe_list[item].quantity = Quantity
    
def search_shoe():
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    find_shoe = input("Enter product name : ").lower()
    found = False
    for item in shoe_list:
        #Removing all spaces in product name. Making product name lower case. Finding shoe:
        if find_shoe in item.product.replace(" ","").lower():   
            item.__str__()                              #Printing shoe found
            found = True
    if found == False:
        print("\nItem not found\n")

def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    
    #using f string notation to have 2 decimal places. 
    #source: https://java2blog.com/format-a-float-to-two-decimal-places
    for item in shoe_list:
        print(f"{item.code} - {item.product} :   {(int(item.quantity)*float(item.cost)):.2f}")'''
    box = [] 
    
    for x in shoe_list:
        box.append([x.code,x.product,(int(x.quantity)*float(x.cost)) ])

    print(f"          INVENTORY VALUATION\n")
    print(tabulate(box, headers = ["Code","Product description","Value"]))

def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    shoe_quantity = []
    for item in shoe_list:
        shoe_quantity.append(int(item.quantity))        #adding all quantities to a list
    item = shoe_quantity.index(max(shoe_quantity))      #the position of the lowest quantity shoe
    print(f"{shoe_list[item].code} - {shoe_list[item].product} is on SALE!! ")
    #Using own discretion to slash prices by 50%:
    print(f"New price @ 50% OFF: {(.5*float(shoe_list[item].cost)):.2f}")
    

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    read_shoes_data()
    menu = input(f'''
                    NIKE INVENTORY MANAGEMENT
_____________________________________________________________________
            search  | re-stock | add stock | view all | value
_____________________________________________________________________

What would you like to do?
''').lower()
    
    if menu =="add stock":
        capture_shoes()
    elif menu == "view all":
        view_all()
    elif menu == "re-stock":
        re_stock()
    elif menu=="search":
        search_shoe()
    elif menu == "value":
        value_per_item()
    elif menu == "exit":
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")
        

