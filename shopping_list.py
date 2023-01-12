# Data stucture:
# The shopping list is modeled as a dictionary keyed by product name.
# The value is another dictionary, with the following keys: "isle" and "quantity"
# Example:
#   shopping_list = { "Apple": { "isle": 1, "quantity": 5}, "Pineapple": { "isle": 3, "quantity": 15 } }
#

shopping_list = {}  # The variable for our shopping cart. Here's where all the data lives.


def add_product(name, quantity, isle):
    shopping_list[name] = {"quantity":quantity, "isle":isle}


def remove_product(name):
    del shopping_list[name]


def modify_product(name, quantity, isle=0):
    "If the parameter isle is not specified or 0, the isle will not be modified."
    if name in shopping_list.keys():
        # Modify an existing product
        shopping_list[name]["quantity"] = quantity
        if isle != 0:
            shopping_list[name]["isle"] = isle
    else:
        add_product(name, quantity, isle)


if __name__ == '__main__':
    # Create a prompt loop with the main menu
    while True:
        match(int(input("Enter 1 to Add, 2 to Remove, 3 to Modify, 4 to List, 5 to Exit"))):
            case 1:
                name = input("Please enter name of product: ")
                quantity = int(input("Enter quantity needed: "))
                isle = int(input("Enter isle where product is located: "))
                add_product(name, quantity, isle)
            case 2:
                name = input("Please enter name of product: ")
                remove_product(name)
            case 3:
                name = input("Please enter name of product: ")
                quantity = int(input("Enter quantity needed: "))
                # ask if isle has changed here?
                isle = int(input("Enter isle where product is located, or enter 0 if not changed: "))
                modify_product(name, quantity, isle)
            case 4:
                print(shopping_list)
            case 5:
                print ("Thank you and goodbye!")
                break
        print ("\n") # newline

